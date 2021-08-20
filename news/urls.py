from django.urls import include, path
from rest_framework import routers

from .views import ArticleList
from .viewset import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'newsitems', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('newsitemlistings/', ArticleList.as_view(), name='newitemlistings'),
]
