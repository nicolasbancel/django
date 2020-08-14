from django.urls import path
from .views import (ArticleCreateView,
                    ArticleListView,
                    ArticleDetailView,
                    ArticleUpdateView,
                    ArticleDeleteView)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('update/<int:id>', ArticleUpdateView.as_view(), name='article-update'),
    path('delete/<int:id>', ArticleDeleteView.as_view(), name='article-delete'),
    # If we use the ID, getting error message : Generic detail view ArticleDetailView must be called with either an object pk or a slug in the URLconf.
    #path('<int:id>', ArticleDetailView.as_view(), name='article-detail')
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail')

]
