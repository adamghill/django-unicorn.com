# Unicorn

```{toctree}
:caption: Introduction
:maxdepth: 2
:hidden:

installation
faq
changelog
```

```{toctree}
:caption: Documentation
:maxdepth: 2
:hidden:

components
templates
django-models
actions
validation
redirecting
loading-states
polling
advanced
settings
cli
```

```{toctree}
:caption: Development
:maxdepth: 2
:hidden:

PDF <https://www.django-unicorn.com/docs/unicorn-0.13.0.pdf>
GitHub <https://github.com/adamghill/django-unicorn>
Sponsor <https://github.com/sponsors/adamghill>
```

`Unicorn` is a reactive component framework that progressively enhances a normal Django view, makes AJAX calls in the background, and dynamically updates the DOM. It seamlessly extends Django past its server-side framework roots without giving up all of its niceties or re-building your website.

## Related projects

`Unicorn` stands on the shoulders of giants, in particular [morphdom](https://github.com/patrick-steele-idem/morphdom) which is integral for merging DOM changes.

A few inspirational projects in other languages and frameworks.

- [Livewire](https://laravel-livewire.com/), a full-stack framework for the PHP web framework, Laravel.
- [LiveView](https://github.com/phoenixframework/phoenix_live_view), a library for the Elixir web framework, Phoenix, that uses websockets.
- [StimulusReflex](https://docs.stimulusreflex.com), a library for the Ruby web framework, Ruby on Rails, that uses websockets.
- [Hotwire](https://hotwire.dev), "is an alternative approach to building modern web applications without using much JavaScript by sending HTML instead of JSON over the wire". Uses AJAX, but can also use websockets.

Some Python packages which aim to solve similar problems as `Unicorn`.

- [Reactor](https://github.com/edelvalle/reactor/), a port of Elixir's `LiveView` to Django. Especially interesting for more complicated use-cases like chat rooms, keeping multiple browsers in sync, etc. Uses Django channels and websockets to work its magic.
- [Flask-Meld](https://github.com/mikeabrahamsen/Flask-Meld), a port of `Unicorn` to Flask. Uses websockets.
- [Sockpuppet](https://sockpuppet.argpar.se/), a port of Ruby on Rail's `StimulusReflex`. Requires Django channels and websockets.
- [Django inertia.js adapter](https://github.com/zodman/inertia-django) allows Django to use <a href="https://inertiajs.com">inertia.js</a> to build an SPA without building an API.
- [django-components](https://gitlab.com/Mojeer/django_components), which provides declarative and composable components for Django, inspired by JavaScript frameworks.
- [django-page-components](https://github.com/andreyfedoseev/django-page-components), a minimalistic framework for creating page components and using them in your Django views and templates.
