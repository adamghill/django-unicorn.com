# Advanced

## Class properties

### template_name

By default, the component name is used to determine what template should be used. For example, `hello_world.HelloWorldView` would by default use `unicorn/hello-world.html`. However, you can specify a particular template by setting `template_name` in the component.

```python
# hello_world.py
from django_unicorn.components import UnicornView

class HelloWorldView(UnicornView):
    template_name = "unicorn/hello-world.html"
```

## Instance properties

### request

The current `request` is available on `self` in the component's methods.

```python
# hello_world.py
from django_unicorn.components import UnicornView

class HelloWorldView(UnicornView):
    def __init__(self, *args, **kwargs):
        super.__init__(**kwargs)
        print("Initial request that rendered the component", self.request)

    def test(self):
        print("callMethod request to re-render the component", self.request)
```

## Custom methods

Defined component instance methods with no arguments are made available to the Django template context and can be called like a property.

```python
# states.py
from django_unicorn.components import UnicornView

class StateView(UnicornView):
    def all_states(self):
        return ["Alabama", "Alaska", "Arizona", ...]
```

```html
<!-- states.html -->
<div>
  <ul>
    {% for state in all_states %}
    <li>{{ state }}</li>
    {% endfor %}
  </ul>
</div>
{% endverbatim %}
```

:::{tip}
If the method is intensive and will be called multiple times, it can be cached with Django's <a href="https://docs.djangoproject.com/en/stable/ref/utils/#django.utils.functional.cached_property">`cached_property`</a> to prevent duplicate API requests or database queries. The method will only be executed once per component rendering.
:::

```python
# states.py
from django.utils.functional import cached_property
from django_unicorn.components import UnicornView

class StateView(UnicornView):
    @cached_property
    def all_states(self):
        return ["Alabama", "Alaska", "Arizona", ...]
```

## Instance methods

### \_\_init\_\_()

Gets called when the component gets constructed for the very first time. Note that constructed components get cached to reduce the amount of time discovering and instantiating them, so `__init__` only gets called the very first time the component gets rendered.

```python
# hello_world.py
from django_unicorn.components import UnicornView

class HelloWorldView(UnicornView):
    name = "original"

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.name = "initialized"
```

### mount()

Gets called when the component gets initialized or [reset](actions.md#reset).

```python
# hello_world.py
from django_unicorn.components import UnicornView

class HelloWorldView(UnicornView):
    name = "original"

    def mount(self):
        self.name = "mounted"
```

### hydrate()

Gets called when the component data gets set.

```python
# hello_world.py
from django_unicorn.components import UnicornView

class HelloWorldView(UnicornView):
    name = "original"

    def hydrate(self):
        self.name = "hydrated"
```

### updating(name, value)

Gets called before each property that will get set.

### updated(name, value)

Gets called after each property gets set.

### updating\_{property_name}(value)

Gets called before the specified property gets set.

### updated\_{property_name}(value)

Gets called after the specified property gets set.

### calling(name, args)

Gets called before each method that gets called.

### called(name, args)

Gets called after each method gets called.

## Meta

Classes that derive from `UnicornView` can include a `Meta` class that provides some advanced options for the component.

### exclude

By default, all public attributes of the component are included in the context of the Django template and available to JavaScript. One way to protect internal-only data is to prefix the atteibute name with `_` to indicate it should stay private.

```python
# hello_state.py
from django_unicorn.components import UnicornView

class HelloStateView(UnicornView):
    _all_states = (
        "Alabama",
        "Alaska",
        ...
        "Wisconsin",
        "Wyoming",
    )
```

Another way to prevent that data from being available to the component template is to add it to the `Meta` class's `exclude` tuple.

```python
# hello_state.py
from django_unicorn.components import UnicornView

class HelloStateView(UnicornView):
    all_states = (
        "Alabama",
        "Alaska",
        ...
        "Wisconsin",
        "Wyoming",
    )

    class Meta:
        exclude = ("all_states", )
```

### javascript_exclude

To allow an attribute to be included in the the context to be used by a Django template, but not exposed to JavaScript, add it to the `Meta` class's `javascript_exclude` tuple.

```html
<!-- hello-state.html -->
<div>
  {% for state in all_states %}
  <div>{{ state }}</div>
  {% endfor %}
</div>
```

```python
# hello_state.py
from django_unicorn.components import UnicornView

class HelloStateView(UnicornView):
    all_states = (
        "Alabama",
        "Alaska",
        ...
        "Wisconsin",
        "Wyoming",
    )

    class Meta:
        javascript_exclude = ("all_states", )
```
