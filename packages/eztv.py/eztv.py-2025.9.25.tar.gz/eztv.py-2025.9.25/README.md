# eztv.py

Install eztv.py with the following command:

```bash
python3 -m pip install eztv.py
```

This command downloads all torrents matching the search terms to the current directory

```bash
eztv.py --torrents search terms
```

Or if you prefer a line-separated list of magnet links:

```bash
eztv.py --magnet search terms
```

## Other packages and their issues

There are several other packages that provide an eztv API.
Most of these are broken and no longer maintained.

This package (`eztv.py`) offers:

- API access
- Search functionality
- DNS over HTTPS to avoid ISP blocks
- Command line usage
- Python library usage

| language            | package                                        | status | last update | EZTV API | EZTV search                                                     | DNS over HTTPS | CLI | Library |
|---------------------|------------------------------------------------|--------|-------------|----------|-----------------------------------------------------------------|----------------|-----|---------|
| Python              | https://pypi.org/project/eztv/                 | broken | 2010-03-20  | 🚫       | 🚫                                                              | 🚫             | 🚫  | ✅️      |
| Python              | https://pypi.org/project/ezflix/               | broken | 2020-08-28  | ?        | ?                                                               | ?              | ✅️  | ✅️      |
| Javascript          | https://www.npmjs.com/package/eztv-api-pt      | broken | 2017-09-29  | ?        | ?                                                               | ?              | ?   | ?       |
| Javascript + Python | https://www.flexget.com/Plugins/eztv           | works  | 2025-07-23  | ✅️       | partial, by iterating over all entries and filtering on IMDB id | ?              | ?   | ?       |
| Python              | https://github.com/PaulSec/API-EZTV.it         | ?      | 2016-06-29  | ?        | ?                                                               | ?              | ?   | ?       |
| Python              | https://pypi.org/project/eztv-py/              | ?      | 2025-09-14  | ✅️       | ✅️                                                              | ✅️             | ✅️  | ✅️      |
| Golang              | https://pkg.go.dev/github.com/odwrtw/eztv      | ?      | ?           | ?        | ?                                                               | ?              | ?   | ?       |
| Golang              | https://pkg.go.dev/github.com/keeb/go-eztv-api | ?      | ?           | ?        | ?                                                               | ?              | ?   | ?       |

If nothing unexpected occurs, I plan to maintain this package for a long time.

