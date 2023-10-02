# Troubleshooting

## Disallowed MIME type error on Windows

Apparently Windows system-wide MIME type configuration sometimes won't load up JavaScript modules in certain browsers. The errors would be something like `Loading module from “http://127.0.0.1:8000/static/js/unicorn.js” was blocked because of a disallowed MIME type (“text/plain”)` or `Failed to load module script: The server responded with a non-JavaScript MIME type of "text/plain".`

One suggested solution is to add the following to the bottom of the settings file:

```python
# settings.py

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
```

See this [Windows MIME type detection pitfalls](https://www.taricorp.net/2020/windows-mime-pitfalls/) article, this [StackOverflow answer](https://stackoverflow.com/a/16355034), or [issue #201](https://github.com/adamghill/django-unicorn/issues/201) for more details.

## `mount` being called more than expected
## Child and parent relationships not working as expected

`Unicorn` uses the Django cache to store information about components. The [local memory cache](https://docs.djangoproject.com/en/stable/topics/cache/#local-memory-caching) can be used with the local development server, but any other type of deployment requires either [database](https://docs.djangoproject.com/en/stable/topics/cache/#database-caching), [redis](https://docs.djangoproject.com/en/stable/topics/cache/#redis), or [memcached](https://docs.djangoproject.com/en/stable/topics/cache/#memcached) to be set up.
