# Direct View

Usually components get included in a regular Django template. However, a component (as complete view) can also be directly targeted in a `urls.py` file in situations where an additional template is not necessary.

## Template Requirements

- there must be one (and only one) element that wraps around the portion of the template that should be handled by `Unicorn`
- the wrapping element must include `unicorn:view` as an attribute
- the template must include the `unicorn_scripts` and `csrf_token` template tags (can be in a base template too)
- the template must be in the `unicorn/` folder

Similar to a class-based view, `Unicorn` components have a `as_view` function which is used in `urls.py`. Bayically, UnicornView is a TemplateView and shares its attributes and methods.

## Example

```python
# book.py
from django_unicorn.components import UnicornView

class BookView(UnicornView):
    title = ""
```

```html
<!-- book.html -->
{% load unicorn %}

<html>
  <head>
    {% unicorn_scripts %}
  </head>
  <body>
    {% csrf_token %}
    <h1>Book</h1>

    <div unicorn:view>
      <input unicorn:model="title" type="text" /><br />
      {{ title }}
    </div>
  </body>
</html>
```

```python
# urls.py
from django.urls import path
from unicorn.components.book import BookView

urlpatterns = [
    path("book", BookView.as_view(), name="book"),
]
```
