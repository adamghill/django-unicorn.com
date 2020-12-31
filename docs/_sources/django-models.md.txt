# Django Models

`Unicorn` provides tight integration with Django `Models` and `Querysets` to handle typical Django workflows. There are multiple ways to integrate a Django model with a component. They all work a little differently and which option you choose to do depends on the situation.

## Class Model

Django models can be initialized similar to how basic Python objects (i.e. strings, integers, dictionaries) can be set on a component.

:::{code} html
:force: true

<!-- class-model.html -->
<div>
  <input unicorn:model.defer="book.title" type="text" id="book" />
  {{ book.title }}
  <button unicorn:click="save">Save</button>
</div>
:::

```python
# class_model.py
from django_unicorn.components import UnicornView
from books.models import Book

class ClassModelView(UnicornView):
    book = Book()

    def save(self):
        self.book.save()
```

## Instance Model

Django models can be initialized in the component's `__init__` method similar to how a "normal" class would initialize an instance variable.

```{danger}
`super().__init__(**kwargs)` **has** to be called at the end of the overriden `__init__` method.
```

:::{code} html
:force: true

<!-- instance-model.html -->
<div>
  <input unicorn:model.defer="book.title" type="text" id="book" />
  {{ book.title }}
  <button unicorn:click="save">Save</button>
</div>
:::

```python
# instance_model.py
from django_unicorn.components import UnicornView
from books.models import Book

class InstanceModelView(UnicornView):
    def __init__(self, **kwargs):
        self.book = Book()

        # super() has to be called at the end
        super().__init__(**kwargs)

    def save(self):
        self.book.save()
```

## DbModel

If there is no reason to have a class or instance attribute, then `Unicorn` also provides a `DbModel` class that ties a simple name used in the front-end to a Django model defined in the component.

`unicorn:db` can also live in a parent element and surround a group of inputs. The `unicorn:field` attribute is used for the model's fields.

:::{code} html
:force: true

<!-- db-model.html -->
<div>
  <div unicorn:db="book">
    <div>
      <input unicorn:field.defer="title" type="text" id="title" />
      {{ book.title }}
    </div>
    <div>
      <input unicorn:field.defer="description" type="text" id="description" />
      {{ book.description }}
    </div>
  </div>

<button unicorn:click="save">Save</button>

</div>
:::

```python
# db_model.py
from django_unicorn.components import UnicornView
from django_unicorn.db import DbModel
from books.models import Book

class DbModelView(UnicornView):
    class Meta:
        db_models = [DbModel("book", Book)]

    def save(self):
        pass
```

## Queryset

Binding models to a Django `Queryset` is done by setting an `unicorn:pk` attribute with the `model`'s `pk` (normally an integer in an `id` field, but could be a custom [`primary_key`](https://docs.djangoproject.com/en/stable/ref/models/fields/#django.db.models.Field.primary_key)).

```{warning}
A blank value for an `unicorn:pk` attribute signals to `Unicorn` to create a new instance of the underlying Django `model` of the queryset.
```

:::{code} html
:force: true

<!-- queryset.html -->
<div>
  <div unicorn:model="books">
    <div unicorn:pk="">
      <!-- A blank pk will create a new model when it is saved -->
      <div>
        <input unicorn:field.defer="title" type="text" id="title" />
      </div>
      <div>
        <input unicorn:field.defer="description" type="text" id="description" />
      </div>
    </div>

    {% for book in books %}
    <div unicorn:pk="{{ book.pk }}">
      <!-- Using the model's pk will save the model -->
      <div>
        <input unicorn:field.defer="title" type="text" id="title" />
        {{ book.title }}
      </div>
      <div>
        <input unicorn:field.defer="description" type="text" id="description" />
        {{ book.description }}
      </div>
    </div>
    {% endfor %}

  </div>

<button unicorn:click="save">Save</button>

</div>
:::

```python
# queryset.py
from django_unicorn.components import UnicornView
from books.models import Book

class QuerysetView(UnicornView):
books = Book.objects.none()

    def hydrate(self):
        # Using `hydrate` is the best way to make sure that QuerySets
        # are re-queried every time the component is loaded
        self.books = Book.objects.all().order_by("-id")[:5]

    def save(self):
        pass
```
