from annoying.decorators import render_to
from django.shortcuts import render


@render_to("www/index.html")
def index(request):
    return {}


@render_to("www/articles.html")
def articles(request):
    return {}


def documentation(request, name="introduction"):
    template_name = f"www/documentation/{name}.html"
    return render(request, template_name)
