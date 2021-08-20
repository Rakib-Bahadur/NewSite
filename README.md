# NewSite
A site for news article to display and serve as web api

## Environment
Please add a file named ".env" to `newsite` directory at project root with following information
$ ENDPOINT = https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&pageSize=100&page=1 
$ API_KEY = :Your api key:

## Project Setup
Note: Assuming that `Python` with version >=3.8.0 is already installed

Please execute the following command sequentially in project root
$ pip install -r requirements.txt
$ python manage.py migrate

To fetch and save the articles from newsapi.org
$ python manage.py storearticles

To run the application
$ python manage.py runserver


## How to use
1. Send GET request [a link](http://localhost:8000/newsitems) to recieve 100 most recent news article as JSON format
2. Access [a link](http://localhost:8000/newsitemlistings) to see the list of 20 most recent article and their access link
