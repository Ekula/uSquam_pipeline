## uSquam Pipeline:
Task pipelining part of our crowdsourcing platform:

## Synopsis

Running **app.py** initializes a Flask application on port **9000**, which responds to certain GET requests. We support the 3 following platforms:

1. Twitter
2. Flickr
3. Imgur
4. Elastic Search

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

Step 1: Getting started 

Download `Elastic Search` and install it.
Follow : `https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html`

Step 2: Elastic Search on Python

Use Command Prompt to start Elastic Search. Go to the location of the folder and run `elasticsearch.bat`.

Elastic Search runs on port **9200**.
If you request `http://localhost:9200/`, you will get the following output (Note: Cluster name and uuid would vary from system to system):

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

In the Check folder, `first_check.py` ensures that the above details are obtained as an output in the Python console.

Step 3: Creating nodes and testing using Postman

Please install `Postman` for API Testing and development.

Request: `GET http://localhost:9200/_cat/indices?v`
If there are no indices you will see: `health status index uuid pri rep docs.count docs.deleted store.size pri.store.size`

Run `second_check.py` from the Check folder. This will create a new index named "posts" with 3 documents.
The first document with id = 1 will be printed on the Python console.

Go to Postman and request: `http://localhost:9200/_cat/indices?v`
You will see that a new index is created called "posts" with docs.count=3.

	health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
	yellow open   posts 82B3zRjjScOyzFh3MpeErQ   5   1          3            0     18.3kb         18.3kb

Step 4: Querying using Elastic Search

Run `search_query.py` from the Query folder.
The code will print all the authors who are not "Santa Clause".
This part will ensure that the querying functionality of Elastic Search works.

Step 5: Merging the Twitter pipeline with Elastic Search

Run `app.py`
You will see this in the Python console: 
	 
	 *Running on http://localhost:9000/ (Press CTRL+C to quit)
	
After this, Go to Postman and request: `GET localhost:9000/requesters/crawlTwitter?hashtag=TUDelft&number=3`
You will obtain three tweets with hashtag TUDelft in the JSON format. The number of tweets and the hashtag can be customized.

	{
	  "results": [
	    {
	      "created_at": "Tue Apr 11 09:46:20 +0000 2017",
	      "hashtags_list": [
		"tudelft"
	      ],
	      "tweet_text": "Kijktip vanavond 20.30 @UniversiteitNL #tudelft prof Gerard van Bussel over Hoe leven we in de toekomst van 				de wind… https://t.co/HrBCuZWiuT",
	      "user_name": "Sharita_B"
	    },
	    {
	      "created_at": "Tue Apr 11 09:15:51 +0000 2017",
	      "hashtags_list": [
		"openscience",
		"TUDelft"
	      ],
	      "tweet_text": "Open Science: The National Plan and you. Save the Date: May 29 \n  # NPOS17 #openscience #TUDelft \n 					https://t.co/2xOyVy8bMv",
	      "user_name": "egonwillighagen"
	    },
	    {
	      "created_at": "Tue Apr 11 09:14:23 +0000 2017",
	      "hashtags_list": [
		"cheetah",
		"Velox7",
		"TUDelft",
		"VUAmsterdam"
	      ],
	      "tweet_text": "'This summer the #cheetah will meet it's rival': de #Velox7, gebouwd door studenten van #TUDelft en 					#VUAmsterdam… https://t.co/XcXl7AraUe",
	      "user_name": "tudelft"
	    }
	  ]
	}

Implementing Ignored Hashtag:

Go to Postman and request: `GET localhost:9000/requesters/crawlTwitter?hashtag=TUDelft&number=3&ignored_hashtag=openscience`
You will obtain the tweets with hashtag TUDelft but without hashtags openscience.

	{
	  "results": [
	    {
	      "created_at": "Tue Apr 11 09:14:23 +0000 2017",
	      "hashtags_list": [
		"cheetah",
		"Velox7",
		"TUDelft",
		"VUAmsterdam"
	      ],
	      "tweet_text": "'This summer the #cheetah will meet it's rival': de #Velox7, gebouwd door studenten van #TUDelft en 					#VUAmsterdam… https://t.co/XcXl7AraUe",
	      "user_name": "tudelft"
	    }
	  ]
	}
	
Step 6: Checking the functionality of the Pipeline combined with the Frontend:

1. Go to: http://usquam.nl/data
2. Click: Add Data Collection.
3. Click: Twitter.
4. Type the hashtag you used for testing on Postman, in my case 'TUDelft'.
5. Type the ignored hashtag, for example 'open science'.
6. Number of tweets, say 3.
7. Click Get Tweets.
8. You will get a list of all tweets in the "Inspect result" section.
