# Installation

Install `Unicorn` the same as any other Python package (preferably into a virtual environment).

```shell
pip install django-unicorn
```

OR

```shell
poetry add django-unicorn
```

Next, install `Unicorn` into the Django project.

- Add `"django_unicorn",` to the `INSTALLED_APPS` array in the Django settings file (normally settings.py)
- Add `path("unicorn/", include("django_unicorn.urls")),` into the project's urls.py
- Add `{% load unicorn %}` to the top of the Django HTML template
- Add `{% unicorn_scripts %}` into the Django HTML template

Then, [create a component](installation).
