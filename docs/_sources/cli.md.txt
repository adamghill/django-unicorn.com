# CLI

`Unicorn` provides a Django management command to create new components.

```shell
python manage.py startunicorn hello-world
```

The command will create a `unicorn` directory, and `templates` and `components` sub-directories if necessary. Underneath the `components` directory there will be a new module and subclass of `django_unicorn.components.UnicornView`. Underneath the `templates/unicorn` directory will be a example template.

The following is an example folder structure.

```
unicorn/
    components/
        hello_world.py
    templates/
        unicorn/
            hello-world.html
```
