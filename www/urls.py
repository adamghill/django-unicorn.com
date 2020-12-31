from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView

from . import views

app_name = "www"

urlpatterns = [
    path("", views.index, name="index"),
    path("articles", views.articles, name="articles"),
    path("documentation", views.documentation, name="documentation"),
    re_path(r"^screencasts/(?P<name>[\w/-]+)$", views.screencasts, name="screencasts",),
    path("screencasts", RedirectView.as_view(url="/screencasts/installation")),
    re_path(r"^examples/(?P<name>[\w/-]+)$", views.examples, name="examples",),
    path("examples", RedirectView.as_view(url="/examples/todo")),
    path("sponsors", views.sponsors, name="sponsors"),
    re_path(
        r"^documentation/(?P<name>[\w/-]+)$", views.documentation, name="documentation",
    ),
    re_path(r"docs/(?P<name>[\w-]+[^/])$", views.docs_redirect),
    path("docs/", include("docs.urls")),
]
