# DBWorld Crawler

A simple DBWorld crawler.

https://research.cs.wisc.edu/dbworld/browse.html.

## Dependencies

```shell
pip install scrapy==1.5.1
```

## Run

```shell
git clone https://github.com/volltin/dbworld-crawler
cd dbworld-crawler
scrapy crawl dbworld -o items.json
```

## Configurations

```python
# dbworld/settings.py

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
```