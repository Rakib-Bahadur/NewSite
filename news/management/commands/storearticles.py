# -*- coding:utf-8 -*-
import requests, os
from django.core.management.base import BaseCommand
from news.serializers import ArticleSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        endpoint_url = os.environ["ENDPOINT"]
        api_key = os.environ["API_KEY"]
        url = endpoint_url + "&apiKey=" + api_key
        response = requests.get(url).json()
        if response["status"] == "ok":
            i = 0
            for article in response["articles"]:
                serializer = ArticleSerializer(data=article)
                if serializer.is_valid() and serializer.create() is not None:
                    i += 1
            print(f"{i} articles saved")
        else:
            print("Can not consume newsapi.org")
