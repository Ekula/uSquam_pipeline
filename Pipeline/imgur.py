import requests
from flask import request, jsonify
from flask_restful import Resource


# Get request to:
# host:port/requesters/crawlTweets?hashtag=tudelft&number=3
# will return a json with the last 3 tweets that contain #tudelft.
class ImgurCrawler(Resource):
    def get(self):
        album = request.args.get('album')

        if album is not None:
            album = str(album)
        else:
            # Error
            return 'Wrong input parameters, try ?album=0f3pD', 404

        # Successful request
        print 'GET request:  Requested Imgur album: ' + album + '.'

        client_id = '7ca45dece8d5588'
        response = requests.get('https://api.imgur.com/3/album/' + album + '/images',
                                headers={'Authorization': 'Client-ID ' + client_id})
        response_json = response.json()

        image_urls_list = []
        for item in response_json['data']:
            crawled_image = {'url': item['link']}
            image_urls_list.append(crawled_image)

        # If list is not empty
        if image_urls_list:
            return jsonify(results=image_urls_list)
        else:
            return None, 404
