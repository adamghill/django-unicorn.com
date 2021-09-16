# CLI

`Unicorn` provides a Django management command to create new components. The first argument is the name of the Django app to create components in. Every argument after is the name of components that should be created.

```shell
python manage.py startunicorn unicorn hello-world
```

This example would create a `unicorn` directory, and `templates` and `components` sub-directories if necessary. Underneath the `components` directory there will be a new module and subclass of `django_unicorn.components.UnicornView`. Underneath the `templates/unicorn` directory will be a example template.

The following is an example folder structure.

```
unicorn/
    components/
        hello_world.py
    templates/
        unicorn/
            hello-world.html
```

```{note}
If you have an existing Django app, you can use that instead of `unicorn` like the example above. The management command will create the the directories and files as needed.
```
