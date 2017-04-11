## uSquam Pipeline:
Task pipelining part of our crowdsourcing platform

## Synopsis

Running **app.py** initializes a Flask application on port **9000**, which responds to certain GET requests. We support the 3 following platforms:

1. Twitter
2. Flickr
3. Imgur

## Twitter

We use the free version of Twitter API and therefore multiple requests need to be made to crawl a large number of Tweets. 1 request corresponds to 100 Tweets, which means that crawling many Tweets can be slow.

Example GET request: `localhost:9000/requesters/crawlTwitter?hashtag=TUDelft&number=2`

This request will crawl twitter, search for tweets containing hashtag "TUDelft" and return 2 Tweets in the following json format:

	{
	  "results": [
		{
		  "created_at": "Sun Apr 02 15:00:00 +0000 2017",
		  "hashtags_list": ["TUDelft"],
		  "tweet_text": "Sold out on campus! Please join Professor Pieter Jan Stappers in #TUDelft",
		  "user_name": "delftxdesign"
		},
		{
		  "created_at": "Sun Apr 02 04:33:11 +0000 2017",
		  "hashtags_list": ["RobotWise", "RoboBusiness"],
		  "tweet_text": "Visit #RobotWise @TUSExpo 19-21April #RoboBusiness",
		  "user_name": "Niels_W"
		}
	  ]
	}

## Flickr

We use the free version of Flickr API and therefore multiple requests need to be made to crawl a large number of posts. 1 request corresponds to 500 Flickr posts, which means that crawling many Flickr posts can be slow.

Example GET request: `localhost:9000/requesters/crawlFlickr?tag=TUDelft&number=3`

This request will crawl Flickr, search for posts containing tag "TUDelft" and return 3 posts in the following json format:

	{
	  "results": [
		{
		  "title": "Save for work shoes",
		  "url": "https://farm3.staticflickr.com/2949/33400403062_324e1ca7e3_o.jpg"
		},
		{
		  "title": "Lanternim",
		  "url": "https://farm3.staticflickr.com/2671/33113823605_bec45d1a38_o.jpg"
		},
		{
		  "title": "Arquitetura",
		  "url": "https://farm4.staticflickr.com/3698/33113820415_0e929e63ce_o.jpg"
		}
	  ]
	}

## Imgur

Example GET request: `localhost:9000/requesters/crawlImgur?album=0f3pD`

This request will crawl Imgur, search for all images contained in the given album (http://imgur.com/a/0f3pD) and return links to those images in the following json format:

	{
	  "results": [
		{
		  "url": "http://i.imgur.com/FlLO0xt.jpg"
		},
		{
		  "url": "http://i.imgur.com/2qpgba7.jpg"
		},
		{
		  "url": "http://i.imgur.com/5N63bTx.jpg"
		}
	  ]
	}

## Elastic Search

Elastic Search
Getting started - Download Elastic Search and install it.
Follow : `https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html`

Elastic Search runs on port 9200. If you request `http://localhost:9200/`, you will get the following output (names would depend on the system):

	{
	  "name" : "z1QNFxg",
	  "cluster_name" : "elasticsearch",
	  "cluster_uuid" : "a0NRUbsnRkmeDztsXJ477Q",
	  "version" : {
	    "number" : "5.2.2",
	    "build_hash" : "f9d9b74",
	    "build_date" : "2017-02-24T17:26:45.835Z",
	    "build_snapshot" : false,
	    "lucene_version" : "6.4.1"
	  },
	  "tagline" : "You Know, for Search"
	}
	
