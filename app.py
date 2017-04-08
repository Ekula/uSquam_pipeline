from flask import Blueprint
from flask_restful import Api

from flask import Flask
from flask_bcrypt import Bcrypt
from flask import jsonify
from flask.json import JSONEncoder
from bson import json_util
from mongoengine.base import BaseDocument
from mongoengine.queryset.base import BaseQuerySet

from Pipeline.twitter import TwitterCrawler

from Pipeline.flickr import FlickrCrawler

from Pipeline.imgur import ImgurCrawler


class MongoEngineJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseDocument):
            return json_util._json_convert(obj.to_mongo())
        elif isinstance(obj, BaseQuerySet):
            return json_util._json_convert(obj.as_pymongo())
        return JSONEncoder.default(self, obj)


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
# Twitter
api.add_resource(TwitterCrawler, '/requesters/crawlTwitter/')
# Flickr
api.add_resource(FlickrCrawler, '/requesters/crawlFlickr/')
# Imgur
api.add_resource(ImgurCrawler, '/requesters/crawlImgur/')

app = Flask(__name__)
app.json_encoder = MongoEngineJSONEncoder
app.register_blueprint(api_bp)
app.bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return jsonify({'status': 200, 'success': True})


app.run(host='localhost', port=9000)
