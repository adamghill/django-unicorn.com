# Django Models

`Unicorn` provides tight integration with Django `Models` and `Querysets` to handle typical Django workflows. There are multiple ways to integrate a Django model with a component. They all work a little differently and which option you choose to use depends on the situation.

## DbModel

One way to use Django models is by utilizing the `DbModel` class that provides a way from the front-end to refer to a Django model. The value of the `unicorn:db` attribute refers to the first argument when constructing a `DbModel` and `unicorn:field` is used for the model's field that should be bound to the input.

Another benefit of `DbModel` is that it enables the use of the [`$model`](actions.md#model) special action variable.

:::{code} html
:force: true

<!-- db-model.html -->
<div>
  <div>
    <input unicorn:db="book" unicorn:field.defer="title" type="text" id="title" />
    {{ book.title }}
  </div>
  <div>
    <input unicorn:db="book" unicorn:field.defer="description" type="text" id="description" />
    {{ book.description }}
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
        print("A new book will be created automatically")
        pass
```

`unicorn:db` can also live in a parent element and surround a group of `unicorn:field` inputs.

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

`unicorn:pk` can be used so that an existing model is updated instead of a new model is created. More information about `unicorn:pk` is in [queryset](#queryset).

:::{code} html
:force: true

<!-- db-model.html -->
<div>
  <div unicorn:db="book">
    <div unicorn:pk="1">
      <div>
        <input unicorn:field.defer="title" type="text" id="title" />
        {{ book.title }}
      </div>
      <div>
        <input unicorn:field.defer="description" type="text" id="description" />
        {{ book.description }}
      </div>
    </div>
  </div>
  <button unicorn:click="save">Save</button>
</div>
:::

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

````{note}
Type hints can also be used to instantiate the model as expected.

```python
# class_model.py
from django_unicorn.components import UnicornView
from books.models import Book

class ClassModelView(UnicornView):
    book: Book = None

    def save(self):
        self.book.save()
```

````

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
