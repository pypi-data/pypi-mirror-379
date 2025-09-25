#!python
"""
Search the EZTV site

Usage:
  eztv.py (-h | --help)
  eztv.py (-t | --torrent) [--season=<season>] [--episode=<episode>] SEARCH_TERM...
  eztv.py (-t | --torrent) [--imdb_id=<imdb_id>] [--season=<season>] [--episode=<episode>]
  eztv.py (-m | --magnet) [--season=<season>] [--episode=<episode>] SEARCH_TERM...
  eztv.py (-m | --magnet) [--imdb_id=<imdb_id>] [--season=<season>] [--episode=<episode>]
  eztv.py (-j | --jsonl) [--season=<season>] [--episode=<episode>] SEARCH_TERM...
  eztv.py (-j | --jsonl) [--imdb_id=<imdb_id>] [--season=<season>] [--episode=<episode>]

Options:
  -h --help                   Show this help message.
  -t --torrent                Download torrent files for search results
  -m --magnet                 Output magnet links to stdout
  -j --jsonl                  Output search results as json lines

  -s --season=<season>        Filter results for this season
  -e --episode=<episode>      Filter results for this episode
  -d --directory=<directory>  The output directory for saving data
  --imdb_id=<imdb_id>         The IMDB ID to search for
"""
import json
import os
import re

import httpx
import requests
import requests_doh.resolver
from bs4 import BeautifulSoup
from docopt import docopt
from faker import Faker
from requests_doh.adapter import DNSOverHTTPSAdapter

__version__ = '2025.9.25'


class EZTVSearchResult:

    def __init__(self, full_title=None, torrent=None, magnet=None, session=None,  # noqa
                 id_=None, filename=None, imdb_id=None, season=None, episode=None,
                 small_screenshot=None, large_screenshot=None, seeds=None, peers=None,
                 date_released_unix=None, size_bytes=None):
        super().__init__()
        self.full_title = full_title
        self.torrent = torrent
        self.magnet = magnet
        self.id = id_
        self.filename = filename
        self.imdb_id = imdb_id
        self.season = season
        self.episode = episode
        self.small_screenshot = small_screenshot
        self.large_screenshot = large_screenshot
        self.seeds = seeds
        self.peers = peers
        self.date_released_unix = date_released_unix
        self.size_bytes = size_bytes
        self.show_name = None
        self.quality = None
        self.uploader = None
        if session:
            self.session = session
        else:
            self.session = EZTV().session
        self.infohash = None  # noqa
        self.calculate_properties()

    def as_dict(self):
        return {
            'full_title': self.full_title,
            'torrent': self.torrent,
            'magnet': self.magnet,
            'season': self.season,
            'episode': self.episode,
            'id': self.id,
            'filename': self.filename,
            'imdb_id': self.imdb_id,
            'small_screenshot': self.small_screenshot,
            'large_screenshot': self.large_screenshot,
            'seeds': self.seeds,
            'peers': self.peers,
            'date_released_unix': self.date_released_unix,
            'size_bytes': self.size_bytes
        }

    @property
    def torrent_bytes(self):
        return self.session.get(self.torrent).content

    def save_torrent(self, path):
        with open(os.path.basename(path), 'wb') as torrent:  # noqa
            torrent.write(self.torrent_bytes)

    def calculate_properties(self):
        try:
            matches = re.findall(
                r"(.*) S(\d{1,3})E(\d{1,3}) (.*)-(\S*)",
                self.full_title
            )[0]
            self.show_name = matches[0]
            self.uploader = matches[4]
            self.season = matches[1]
            self.episode = matches[2]
        except IndexError:
            pass
        self.quality = re.findall(
            'XviD|1080p|h264|WEB|x264|DDP5|720p|x265|DDP2|H 264|480p|HEVC|WEB-DL|H264|AAC2|AMZN|HDTV',
            self.full_title
        )
        try:
            self.infohash = re.findall(  # noqa
                r"magnet:\?xt=urn:btih:([0-9a-fA-F]*)",
                self.magnet or ''
            )[0].upper()  # can occur with delisted torrents
        except IndexError:
            pass

    def __repr__(self):
        return f'<{self.full_title}, {self.infohash}>'


class EZTV:
    def __init__(self):
        requests_doh.resolver.add_dns_provider(
            "cloudflare_ip",
            'https://104.16.249.249/dns-query',
            switch=True)
        requests_doh.resolver.set_resolver_session(
            httpx.Client(verify=False,
                         headers={"Host": "cloudflare-dns.com"}))

        doh = DNSOverHTTPSAdapter(provider="cloudflare_ip")

        self.session = requests.Session()
        self.faker = Faker()
        self.session.headers = {
            "User-Agent": self.faker.user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
        }
        self.session.mount('https://', doh)
        self.session.mount('http://', doh)  # noqa

    def search(self, query):  # season, episode, quality filtering
        query = query.replace(' ', '-').lower()
        self.session.get(f'https://eztvx.to/search/{query}')
        result = self.session.post(f'https://eztvx.to/search/{query}',
                                   params={"layout": 'def_wlinks'})  # noqa

        hits_page = BeautifulSoup(result.content, features='html.parser')
        hits = hits_page.find_all('a', {'class': 'epinfo'})  # noqa

        for hit in hits:
            title = hit.get('title', hit.get('alt', ''))
            hit = self.session.get(f'https://eztvx.to{hit.get("href")}')
            torrent, magnet = None, None  # noqa
            for link in BeautifulSoup(hit.content, features='html.parser').find_all('a'):
                link = link.get('href', '')
                if link.startswith('magnet:'):
                    magnet = link  # noqa
                if link.endswith('.torrent'):
                    torrent = link  # noqa
            yield EZTVSearchResult(title, torrent, magnet, self.session)

    def get_torrents(self, imdb_id=None, **kwargs):
        if imdb_id is not None:
            kwargs['imdb_id'] = imdb_id
        returned = 0
        kwargs['page'] = 1
        while returned == 0 or returned < response.json()['torrents_count']:  # noqa
            response = self.session.get('https://eztvx.to/api/get-torrents', params=kwargs)
            for result in response.json()['torrents']:
                returned += 1
                yield EZTVSearchResult(
                    result['title'],
                    result['torrent_url'],
                    result['magnet_url'],
                    id_=result['id'],
                    filename=result['filename'],
                    imdb_id=result['imdb_id'],
                    season=result['season'],
                    episode=result['episode'],
                    small_screenshot=result['small_screenshot'],
                    large_screenshot=result['large_screenshot'],
                    seeds=result['seeds'],
                    peers=result['peers'],
                    date_released_unix=result['date_released_unix'],
                    size_bytes=result['size_bytes'],
                    session=self.session,
                )
            kwargs['page'] = kwargs['page'] + 1


def magnet(args, filters):
    if args.get('SEARCH_TERM'):
        results = EZTV().search(' '.join(args['SEARCH_TERM']))
    else:
        results = EZTV().get_torrents(imdb_id=args.get('--imdb_id', None), **args)
    for result in results:
        if all(filter_(result) for filter_ in filters):
            print(result.magnet)


def torrent(args, filters):
    torrent_directory = args.get('--directory', '.') or '.'
    if args.get('SEARCH_TERM'):
        results = EZTV().search(' '.join(args['SEARCH_TERM']))
    else:
        results = EZTV().get_torrents(imdb_id=args.get('--imdb_id', None), **args)
    for result in results:
        if all(filter_(result) for filter_ in filters):
            if result.torrent:
                result.save_torrent(os.path.join(torrent_directory, result.torrent))


def jsonl(args, filters):
    if args.get('SEARCH_TERM'):
        results = EZTV().search(' '.join(args['SEARCH_TERM']))
    else:
        results = EZTV().get_torrents(imdb_id=args.get('--imdb_id', None), **args)
    for result in results:
        if all(filter_(result) for filter_ in filters):
            print(json.dumps(result.as_dict()))


def main():
    args = docopt(__doc__)
    filters = []
    if args.get('--season'):
        filters.append(lambda x: int(x.season) == int(args['--season']))
    if args.get('--episode'):
        filters.append(lambda x: int(x.episode) == int(args['--episode']))
    if args['--magnet']:
        magnet(args, filters)
    elif args['--torrent']:
        torrent(args, filters)
    elif args['--jsonl']:
        jsonl(args, filters)
    else:
        print("If this statement is reached, our docopt docstring is malfunctioning.")


if __name__ == '__main__':
    main()
