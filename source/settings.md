# Settings

`Unicorn` stores all settings in a dictionary under the `UNICORN` attribute in the Django settings file. All settings are optional.

```python
# settings.py
UNICORN = {
    "MINIMIZE": True,
    "APPS": ["unicorn"],
    "SERIAL": {
        "ENABLED": False,
        "TIMEOUT": 60,
    },
    "CACHE_ALIAS": "default",
}
```

## APPS

Specify the modules to look for components. Defaults to `["unicorn",]`.

## CACHE_ALIAS

The alias to use for caching. Only used by the experimental serialization of requests for now. Defaults to `"default"`.

## MINIMIZE

Provides a way to control if the minimized version of `unicorn.min.js` is used. Defaults to `!DEBUG`.

## SERIAL

Settings for the experimental serialization of requests. Defaults to `{}`.

### ENABLED

Whether slow requests to the same component should be queued or not. Defaults to `False`.

### TIMEOUT

The number of seconds to wait for a request to finish for additional requests to queue behind it. Defaults to `60`.
