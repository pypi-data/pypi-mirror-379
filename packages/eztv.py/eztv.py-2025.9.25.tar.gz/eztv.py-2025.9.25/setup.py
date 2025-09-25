from setuptools import setup
from eztv import __version__

with open('README.md', 'r') as readme:
    readme = readme.read()

with open('requirements.txt', 'r') as requirements:
    dependencies = [line.strip() for line in requirements
                    if '#' not in line]

setup(
    name='eztv.py',
    version=__version__,
    url='https://github.com/jenss1997/eztv-py',
    author='Jens',
    author_email='jenss1997@proton.me',
    license='MIT License',
    description="Query the EZTV site programmatically",
    keywords='eztv',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['eztv'],
    install_requires=dependencies,
    scripts=['eztv.py'],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia :: Video',
    ]
)
