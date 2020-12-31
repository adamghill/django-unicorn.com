# Settings

`Unicorn` stores all settings in a dictionary under the `DJANGO_UNICORN` setting attribute in the Django settings file. All settings are optional.

```python
# settings.py
DJANGO_UNICORN = {
    "MINIMIZE": True,
    "APPS": ["unicorn"]
}
```

## MINIMIZE

Provides a way to control if the minimized version of `unicorn.min.js` is used. Defaults to `!DEBUG`.

## APPS

Specify the modules to look for components. Defaults to `["unicorn",]`.
