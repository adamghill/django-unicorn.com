# Installation

Install `Unicorn` the same as any other Python package (preferably into a [virtual environment](https://docs.python.org/3/tutorial/venv.html)).

```shell
pip install django-unicorn
```

OR

```shell
poetry add django-unicorn
```

```{note}
If attempting to install `django-unicorn` and `orjson` is preventing the installation from succeeding, check whether it is using 32-bit Python. Unfortunately, `orjson` is only supported on 64-bit Python. More details in [issue #105](https://github.com/adamghill/django-unicorn/issues/105).
```

Next, install `Unicorn` into the Django project.

- Add `"django_unicorn",` to the `INSTALLED_APPS` array in the Django settings file (normally `settings.py`)
- Add `path("unicorn/", include("django_unicorn.urls")),` into the projects `urls.py`
- Add `{% load unicorn %}` to the top of the Django HTML template
- Add `{% unicorn_scripts %}` into the Django HTML template

Then, [create a component](components.md).
