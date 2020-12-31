# Polling

`unicorn:poll` can be added to the root `div` element of a component to have it refresh the component automatically every 2 seconds. The polling is smart enough that it won't poll when the page is inactive.

```python
# polling.py
from django.utils.timezone import now
from django_unicorn.components import UnicornView

class PollingView(UnicornView):
    current_time = now()
```

```html
<!-- polling.html -->
<div unicorn:poll>{{ current_time }}</div>
```

A method can also be specified if there is a specific method on the component that should called every time the polling fires. For example, `unicorn:poll="get_updates"` would call the `get_updates` method instead of the built-in `refresh` method.

To define a different refresh time in milliseconds, a modifier can be added as well. `unicorn:poll-1000` would fire the `refresh` method every 1 second, instead of the default 2 seconds.

```html
<!-- polling_every_five_seconds.html -->
<div unicorn:poll-5000="get_updates">
  <input unicorn:model="update" type="text" id="text" />
  {{ update }}
</div>
```
