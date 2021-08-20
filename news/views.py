from django.views.generic import ListView
from news.models import Article


class ArticleList(ListView):
    queryset = Article.objects.select_related("source")\
               .order_by("-published_at").all()[:20]
    model = Article
    template_name = 'news_listings.html'
