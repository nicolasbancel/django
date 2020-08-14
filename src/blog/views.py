from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForm


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # Will connect to the template : <app_name>/<model_name>_list.html : because inherits from ListView

    def form_valid(self, form):
        # Prints in the terminal the content of the form in a dictionnary
        #print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # Will connect to the template : <app_name>/<model_name>_list.html : because inherits from ListView

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # No need for the queryset : this limits the choices available for the detail vie
    queryset = Article.objects.all()
    # Example : queryset could limit the ids to be greater than 1 // when all() : it's useless
    #queryset = Article.objects.filter(id__gt=1)

    def get_object(self):
        # Those are the kwargs of
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    #queryset = Article.objects.all()

    def get_object(self):
        # Those are the kwargs of
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
