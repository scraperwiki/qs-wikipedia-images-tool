#!/usr/bin/env python
import sys
import json
import requests
import scraperwiki

response = requests.get("http://en.wikipedia.org/w/api.php?action=query&list=allimages&aiprop=url|user|timestamp|size|mime&ailimit=100&format=json&aifrom=%s" % sys.argv[1])

data = json.loads(response.text)

images = data['query']['allimages']
scraperwiki.sqlite.save(['name'], images, 'images')
