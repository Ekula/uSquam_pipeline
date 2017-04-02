import requests
import urllib
import json
from flask_restful import Resource
from flask import request, jsonify


# Get request to:
# host:port/requesters/crawlFlickr?tag=delft
# will return a json with the flickr posts that contain tag delft.
class FlickrCrawler(Resource):
    def get(self):
        tag = request.args.get('tag')
        number = request.args.get('number')

        if tag is not None and number is not None and number.isdigit():
            tag = str(tag)
            number = int(number)
        else:
            # Error
            return 'Wrong input parameters, try ?tag=tudelft&number=50', 404

        print 'GET request:  Requested ' + str(number) + ' flickr photos with tag: ' + str(tag) + '.'

        crawled_flickr_list = []
        page = 1
        while True:
            parameters = {
                'api_key': 'a3754000dcee5ad53eae269dd7c3b9cb',
                'format': 'json',
                'nojsoncallback': '?',
                'method': 'flickr.photos.search',
                'extras': 'url_o',
                'tags': tag,
                'per_page': 500,
                'page': page
            }
            url = 'https://api.flickr.com/services/rest/?' + urllib.urlencode(parameters)
            response = requests.get(url)
            flickr_json = response.json()

            pages = flickr_json['photos']['pages']

            for photo in flickr_json['photos']['photo']:
                if 'url_o' in photo:
                    # Reformat json to contain less properties
                    crawled_flickr = {'title': photo['title'], 'url': photo['url_o']}
                    crawled_flickr_list.append(crawled_flickr)

            # If list is not empty
            if len(crawled_flickr_list) >= number:
                return jsonify(results=crawled_flickr_list[:number])
            else:
                page += 1

            if page == pages:
                return jsonify(results=crawled_flickr_list)
