from annoying.decorators import render_to
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect


@cache_page(60 * 15)
@csrf_protect
@render_to("www/index.html")
def index(request):
    return {}


@cache_page(60 * 15)
@render_to("www/articles.html")
def articles(request):
    return {}


@cache_page(60 * 15)
def screencasts(request, name="installation"):
    template_name = f"www/screencasts/{name}.html"
    return render(request, template_name)


@cache_page(60 * 15)
@render_to("www/sponsors.html")
def sponsors(request):
    return {}


@cache_page(60 * 15)
@csrf_protect
def documentation(request, name="introduction"):
    template_name = f"www/documentation/{name}.html"
    return render(request, template_name)
