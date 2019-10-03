![Python](https://img.shields.io/badge/python-3.7.3-green.svg)
[![PyPI version](https://badge.fury.io/py/vb-console.svg)](https://badge.fury.io/py/vb-console)

# vb-console

A custom Python object inspector with style.

## Installation and Usage

```bash
$ pip install vb-console
```

By default, console output is disabled. You can enable output via setting
the `ENABLE_CONSOLE` environment variable. Launch Python reply:

```bash
$ ENABLE_CONSOLE=1 python
```

then;

```python
Python 3.7.3 (default, Jul  6 2019, 07:47:04) 
[Clang 11.0.0 (clang-1100.0.20.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from console import console
>>> console = console(source=__name__) 
>>> console('Hello World')
[__main__]*****************************************************************************
('Hello World',)
***************************************************************************************

>>> console.dir([1,2,3])
[__main__ : instance of list | <class 'list'>]*****************************************
{   'internal_methods': [   '__add__', '__class__', '__contains__', '__delattr__', 
                            '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
                            '__ge__', '__getattribute__', '__getitem__', '__gt__', 
                            '__hash__', '__iadd__', '__imul__', '__init__', 
                            '__init_subclass__', '__iter__', '__le__', '__len__', 
                            '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
                            '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
                            '__setattr__', '__setitem__', '__sizeof__', '__str__', 
                            '__subclasshook__'],
    'public_attributes': [  'append', 'clear', 'copy', 'count', 'extend', 'index', 
                            'insert', 'pop', 'remove', 'reverse', 'sort']}
***************************************************************************************
```

You have few options for console output:

- `console(object)`
- `console(object, object, object, ...)`
- `console.dir(object)`

You can custom `console` instance;

```python
from console import console

# default/basic
console = console(source=__name__)

# set screen width and indentation
console = console(
    source=__name__,
    indent=8,
    width=64,
)

# set color mode
console = console(
    source=__name__,
    color='yellow',
)

# inline color
console('hello', 'world', [1, 2, 3], color='red')
```

Valid colors are:

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `default`

Defaults are;

- `width` is `79`
- `indent` is `4`
- `seperator_char` is `*`
- `color` is `yellow`

Example of complex object inspection:

```python
class MyClass:
    klass_var1 = 1
    klass_var2 = 2

    def __init__(self):
        self.name = 'Name'

    def start(self):
        return 'method'

    @property
    def admin(self):
        return True

    @staticmethod
    def statik():
        return 'Static'

    @classmethod
    def klass_method(cls):
        return 'kls'

mc = MyClass()

console.dir(MyClass)
```

Output:

```bash
[__main__ : MyClass | <class 'type'>]*******************************************
{   'class_methods': ['klass_method'],
    'internal_methods': [   '__class__', '__delattr__', '__dict__', '__dir__',
                            '__doc__', '__eq__', '__format__', '__ge__',
                            '__getattribute__', '__gt__', '__hash__',
                            '__init_subclass__', '__le__', '__lt__',
                            '__module__', '__ne__', '__new__', '__reduce__',
                            '__reduce_ex__', '__repr__', '__setattr__',
                            '__sizeof__', '__str__', '__subclasshook__',
                            '__weakref__'],
    'property_list': ['admin'],
    'public_attributes': ['klass_var1', 'klass_var2'],
    'public_methods': ['__init__', 'start'],
    'static_methods': ['statik']}
*******************************************************************************
```

More;

```python
console.dir(mc)
```

Output:

```bash
In [6]: console.dir(mc)                                                         
[__main__ : instance of MyClass | <class '__main__.MyClass'>]*******************
{   'instance_attributes': ['name'],
    'internal_methods': [   '__class__', '__delattr__', '__dict__', '__dir__',
                            '__doc__', '__eq__', '__format__', '__ge__',
                            '__getattribute__', '__gt__', '__hash__',
                            '__init__', '__init_subclass__', '__le__', '__lt__',
                            '__module__', '__ne__', '__new__', '__reduce__',
                            '__reduce_ex__', '__repr__', '__setattr__',
                            '__sizeof__', '__str__', '__subclasshook__',
                            '__weakref__'],
    'public_attributes': [   'admin', 'klass_method', 'klass_var1',
                             'klass_var2', 'start', 'statik']}
********************************************************************************
```

Standard objects:

```python
console.dir(dict)
```

Output:

```bash
[__main__ : dict | <class 'type'>]**********************************************
{   'internal_methods': [   '__class__', '__contains__', '__delattr__',
                            '__delitem__', '__dir__', '__doc__', '__eq__',
                            '__format__', '__ge__', '__getattribute__',
                            '__getitem__', '__gt__', '__hash__', '__init__',
                            '__init_subclass__', '__iter__', '__le__',
                            '__len__', '__lt__', '__ne__', '__new__',
                            '__reduce__', '__reduce_ex__', '__repr__',
                            '__setattr__', '__setitem__', '__sizeof__',
                            '__str__', '__subclasshook__'],
    'public_attributes': [   'clear', 'copy', 'fromkeys', 'get', 'items',
                             'keys', 'pop', 'popitem', 'setdefault', 'update',
                             'values']}
********************************************************************************
```

### Using with Django

`console` also checks for Django’s `DEBUG` settings value: `settings.DEBUG`.
Example usage for Django project;

```python
from django.views.generic.base import TemplateView

from console import console

console = console(source=__name__)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        console('kwargs', kwargs)
        console.log(kwargs)
        return kwargs
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

**2019-10-03**

- Fix some of the code
- Add `ENABLE_CONSOLE` environment variable
- Update README

**2019-09-29**

- Init repo!
