from annoying.decorators import render_to
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
@render_to("www/index.html")
def index(request):
    return {}


@cache_page(60 * 15)
@render_to("www/articles.html")
def articles(request):
    return {}


@cache_page(60 * 15)
@render_to("www/screencasts.html")
def screencasts(request):
    return {}


@cache_page(60 * 15)
@render_to("www/sponsors.html")
def sponsors(request):
    return {}


@cache_page(60 * 15)
def documentation(request, name="introduction"):
    template_name = f"www/documentation/{name}.html"
    return render(request, template_name)
