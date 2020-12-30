# FAQ

## Do I need to learn a new frontend framework for `Unicorn`?

Nope! `Unicorn` gives you some magical template tags and HTML attributes to sprinkle in normal Django HTML templates. The backend code is a simple class that ultimately derives from `TemplateView`. Keep using the same Django HTML templates, template tags, filters, etc and the best-in-class Django ORM without learning another new framework of the week.

## Do I need to build an entire API to use `Unicorn`?

Nope! `Django REST framework` is pretty magical on its own, and if you will need a mobile app or other use for a REST API, it's a great set of abstractions to follow REST best practices. But, it can be challenging implementing a robust API even with `Django REST framework`. And I wouldn't even attempt to build an API up from scratch unless it was extremely limited.

## Do I need to need to install GraphQL to use `Unicorn`?

Nope! GraphQL looks like an awesome technology for specific use-cases and solves some pain points around creating a RESTful API. But, it is another peiece of technology to wrestle with.

## Do I need to run an annoying separate node.js process or learn any tedious Webpack configuration incantations to use `Unicorn`?

Nope! `Unicorn` <a href="{% url 'www:documentation' name='installation' %}">installs</a> just like any normal Django package and is seamless to implement. There <em>are</em> a few "magic" attributes to sprinkle into a Django HTML template, but other than that it's just like building a regular server-side application.

## Does this replace Vue.js or React?

Nope! In some cases, you might need to actually build an <span title="single-page application">SPA</span> in which case `Unicorn` really isn't that helpful. In that case you might have to invest the time to learn a more involved frontend framework. Read [Using VueJS alongside Django](https://tkainrad.dev/posts/use-vuejs-with-django/) for one approach.

## Isn't calling an AJAX endpoint on every input slow?

Not really! `Unicorn` is ideal for when an AJAX call would already be required (such as hitting an API for typeahead search or update data in a database). If that isn't required, the [lazy](actions.md#lazy) and [debounce](actions.md#debounce) modifiers can also be used to prevent an AJAX call on every change.

## But, what about security?

`Unicorn` follows the best practices of Django and requires a <a href="https://docs.djangoproject.com/en/stable/ref/csrf/#how-it-works">CSRF token</a> to be set on any page that has a component. This ensures that no nefarious AJAX POSTs can be executed. `Unicorn` also creates a unique component checksum with the Django <a href="https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY">secret key</a> on every data change which also ensures that all updates are valid.

## What browsers does `Unicorn` support?

`Unicorn` mostly targets modern browsers, but the project would appreciate any PRs to help support legacy browsers.

## How to make sure that the new JavaScript is served when a new version of `Unicorn` is released?

`Unicorn` works great with <a href="https://whitenoise.evans.io/en/stable/">whitenoise</a>'s ability to serve static assets with a filename based on a hash of the file. <a href="http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support">CompressedManifestStaticFilesStorage</a> works great for this purpose and is used by <a href="https://www.django-unicorn.com/">django-unicorn.com</a> for this very purpose. Example code can be found at <a href="https://github.com/adamghill/django-unicorn.com/blob/cb79932/project/settings.py#L72">https://github.com/adamghill/django-unicorn.com/</a>.
