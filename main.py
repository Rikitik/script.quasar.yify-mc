# coding: utf-8
__author__ = 'mancuniancol'

import bs4
import requests
from quasar import provider

import common

# this read the settings
settings = common.Settings()
# create the filters
filters = common.Filtering()
# create the request session
browser = requests.Session()
browser.headers[
    'User-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
browser.headers['Accept-Language'] = 'en'


def extract_magnets(data):
    results = []
    soup = bs4.BeautifulSoup(data)
    links = soup.select("div.browse-movie-bottom")
    for div in links:
        baseTitle = div.a.text  # title
        aList = div.select("div a")
        for a in aList:
            title = baseTitle + ' ' + a.text
            urlSource = a["href"]
            infoHash = urlSource[urlSource.rfind("/") + 1:-8]
            magnet = 'magnet:?xt=urn:btih:%s' % infoHash
            name = title + ' - ' + settings.name_provider
            provider.log.info(name)
            if filters.verify(name, None):
                results.append({'name': name, 'uri': magnet, 'info_hash': infoHash})
            else:
                provider.log.warning(filters.reason)
    return results


def search(query):
    return []


def search_movie(info):
    query = info['title'].encode('utf-8')
    filters.title = query
    filters.use_movie()
    if settings.time_noti > 0: provider.notify(message='Searching: ' + info['title'].title().encode("utf-8") + '...',
                                               header=None,
                                               time=settings.time_noti, image=settings.icon)
    urlSearch = settings.url
    provider.log.info(urlSearch)
    # new code
    response = browser.get(urlSearch)
    soup = bs4.BeautifulSoup(response.text)
    itemToken = soup.select("div#mobile-search-input input")
    token = itemToken[0]["value"]  # hidden token

    # Read
    provider.log.info(urlSearch)
    payload = {
        "keyword": query,
        "_token": token,
        "quality": "all",
        "genre": "all",
        "rating": "0",
        "order_by": "seeds",
    }
    provider.log.info(payload)
    response = browser.post(urlSearch + "/search-movies", data=payload)
    return extract_magnets(response.text)


def search_episode(info):
    # just movies site
    return []


# This registers your module for use
provider.register(search, search_movie, search_episode)
