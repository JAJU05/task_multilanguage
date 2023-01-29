from django.views.generic import ListView, TemplateView

from home.models import Blog, Category


class IndexListView(ListView):
    queryset = Blog.objects.all()
    template_name = 'index.html'
    context_object_name = 'blogs'


class BaseView(TemplateView):
    template_name = 'base.html'
