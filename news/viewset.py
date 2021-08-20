from rest_framework import viewsets, response

from .serializers import ArticleSerializer
from .models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.order_by('-published_at')
    serializer_class = ArticleSerializer

    def list(self, request):
        queryset = self.get_queryset()[:100]
        serializer = ArticleSerializer(queryset, many=True)
        return response.Response(serializer.data)
