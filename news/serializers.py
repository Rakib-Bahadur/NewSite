from .models import Source, Article
from rest_framework import serializers
from django.db.utils import IntegrityError


class SourceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='source_id', allow_null=True)

    class Meta:
        model = Source
        fields = ['id', 'name']


# class ArticleListSerializer(serializers.ListSerializer):
#     def create(self, item, validated_data_list):
#         articles = []

#         for validated_data in validated_data_list:
#             articles.append(self.child.create(validated_data))

#         return articles


class ArticleSerializer(serializers.ModelSerializer):
    source = SourceSerializer()
    author = serializers.CharField(allow_null=True)
    title = serializers.CharField(allow_null=True)
    description = serializers.CharField(allow_blank=True)
    url = serializers.URLField()
    urlToImage = serializers.CharField(source="url_to_image", allow_null=True)
    publishedAt = serializers.DateTimeField(source="published_at")
    content = serializers.CharField(allow_null=True)

    class Meta:
        # list_serializer_class = ArticleListSerializer
        model = Article
        fields = ["source", "author", "title", "description",
                  "url", "urlToImage", "publishedAt", "content"]

    def create(self):
        source_data = self.validated_data.pop("source")
        source, is_created = Source.objects.get_or_create(**source_data)
        try:
            article = Article.objects.create(source=source, **self.validated_data)
        except IntegrityError:
            return None
        else:
            return article
