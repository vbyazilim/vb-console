[![Build Status](https://travis-ci.org/vbyazilim/vb-console.svg?branch=master)](https://travis-ci.org/vbyazilim/vb-console)
![Python](https://img.shields.io/badge/python-3.8.5-green.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/vb-console.svg)](https://badge.fury.io/py/vb-console)

# vb-console

A custom Python object inspector with a fancy style.

[![asciicast](https://asciinema.org/a/RKEHksQVhQ73jf7suytdrk2nS.svg)](https://asciinema.org/a/RKEHksQVhQ73jf7suytdrk2nS)

## Installation

```bash
$ pip install vb-console
```

By default, console output is disabled. You can enable output via

- setting `ENABLE_CONSOLE` environment variable
- passing `enabled=True` keyword argument

## Usage

Let’s try with-in the python repl:

```bash
$ ENABLE_CONSOLE=1 python
```

then;

```python
Python 3.8.5 (default, Nov 17 2020, 17:58:11) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from console import console
>>> console = console(source='repl', enabled=True)
>>> console('hello', 'world')
('hello', 'world')
>>> 
```

This usage above is always better choice. Helps you to keep out un-wanted outputs
in the production environment!

Let’s try with `enabled=True`;

```bash
$ python
```

then;

```python
Python 3.8.5 (default, Nov 17 2020, 17:58:11) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from console import console
>>> console = console(source='repl', enabled=True)
>>> console.dir([1,2])
{   'internal_methods': [   '__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
                            '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
                            '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
                            '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
                            '__setitem__', '__sizeof__', '__str__', '__subclasshook__'],
    'public_attributes': ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']}
>>> 
```

In this mode, console will always be available. Here is a quick usage with
`Django`:

```python
from django.conf import settings
from console import console

console = console(source='repl', enabled=settings.DEBUG)  # will be disabled in production!
```

You have few options for console output:

- `console(object)`
- `console(object, object, object, ...)`
- `console.dir(object)`

All you need is this piece of code:

```python
# import area
from console import console

console = console(source=__name__, enabled=True)

console('hello', 'world')
console.dir([])
```

Here is an example class:

```python
class MyClass:
    """Example class"""

    klass_var1 = 1
    klass_var2 = 2
    klass_var3 = 'string'
    klass_var4 = list()
    klass_var5 = dict()
    klass_var6 = set()

    def __init__(self):
        self.name = 'Name'

    def get_name_and_method(self):
        return self.name + ' get_name_and_method'

    def _private_method(self):
        return self.name + ' _private_method'

    @property
    def admin(self):
        return True

    @staticmethod
    def statik():
        return 'Static'

    @classmethod
    def klass_method(cls):
        return 'kls'

my_class_instance = MyClass()
console.dir(my_class_instance)
```

outputs:

```python
{   'class_methods': ['klass_method'],
    'class_variables': ['klass_var1', 'klass_var2', 'klass_var3', 'klass_var4', 'klass_var5', 'klass_var6'],
    'data_attributes': ['name'],
    'internal_methods': [   '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                            '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
                            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
                            '__str__', '__subclasshook__', '__weakref__'],
    'methods': ['get_name_and_method'],
    'private_methods': ['_private_method'],
    'properties': ['admin'],
    'public_attributes': [   'admin', 'get_name_and_method', 'klass_method', 'klass_var1', 'klass_var2', 'klass_var3', 'klass_var4',
                             'klass_var5', 'klass_var6', 'name', 'statik'],
    'static_methods': ['statik']}
```

Now, let’s disable `basic` output:

```python
from console import console
console = console(source=__name__, enabled=True, basic=False)
```

outputs with header and footer. `source` gets it’s value from `__name__` and
currently the value is set to `__main__`:

```python
[__main__ : instance of MyClass | <class '__main__.MyClass'>].........................................................................
{   'class_methods': ['klass_method'],
    'class_variables': ['klass_var1', 'klass_var2', 'klass_var3', 'klass_var4', 'klass_var5', 'klass_var6'],
    'data_attributes': ['name'],
    'internal_methods': [   '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                            '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
                            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
                            '__str__', '__subclasshook__', '__weakref__'],
    'methods': ['get_name_and_method'],
    'private_methods': ['_private_method'],
    'properties': ['admin'],
    'public_attributes': [   'admin', 'get_name_and_method', 'klass_method', 'klass_var1', 'klass_var2', 'klass_var3', 'klass_var4',
                             'klass_var5', 'klass_var6', 'name', 'statik'],
    'static_methods': ['statik']}
......................................................................................................................................
```

## Options

- `source`: Name of the header if the `basic` option is set to `False`. It’s
  good idea to set to `__name__`
- `indent`: Indentation value, default is: `4`
- `width`: Output’s width. Default is set to Terminal’s current width.
- `enabled`: Default is `False`. Can be modified via `ENABLE_CONSOLE` env-var
  or setting this arg to `True`
- `seperator_char`: Default is: `.`
- `colored`: Default is `False`. Set this to `True` for colored output
- `dir_colors`: This is a `dict`, default is `dict(keys='yellow', values='default')`
- `header_color`: Default is `green`
- `footer_color`: Default is `green`
- `basic`: Default is `True`. In basic mode, header and footer are not available
- `writer`: Default is `sys.stdout`

Valid colors are: `black`, `red`, `green`, `yellow`, `blue`, `magenta`,
`cyan`, `white` and `default`


---

## Development

I’ve prepared few rake tasks:

```bash
$ rake -T

rake build           # Build package
rake bump[revision]  # Bump version
rake clean           # Remove/Delete build..
rake default         # Default task => :install
rake install         # Install package for local development purpose
rake test            # Run test
rake upload:main     # Upload package to main distro (release)
rake upload:test     # Upload package to test distro
```

Default rake task installs package locally for development purposes:

```bash
$ rake       # runs rake install
```

---

## License

This project is licensed under MIT

---

## Contributer(s)

* [Uğur "vigo" Özyılmazel](https://github.com/vigo) - Creator, maintainer

---

## Contribute

All PR’s are welcome!

1. `fork` (https://github.com/vbyazilim/django-vb-console/fork)
1. Create your `branch` (`git checkout -b my-features`)
1. `commit` yours (`git commit -am 'added killer options'`)
1. `push` your `branch` (`git push origin my-features`)
1. Than create a new **Pull Request**!

---

## Change Log

**2021-02-05**

- Re-write whole package from scracth

**2021-01-16**

- Add `output_to` param for streaming output to different targets
- Add `basic` param for simple output
- Add unit tests
- Add Travis
- Make small changes in the `console.py`

**2019-10-03**

- Fix some of the code
- Add `ENABLE_CONSOLE` environment variable
- Update README

**2019-09-29**

- Init repo!
