aldryn-quote
============

Easy to use quote plugin for [Aldryn Cloud](https://www.divio.com/) and [django CMS](http://www.django-cms.org/).

Requirements
------------

* Django 1.7 or higher
* django CMS 3.0 or higher

Installation
------------

1. Run the following commands in the given order:

    ```bash
    pip install -e git+https://github.com/philipp-x/aldryn-quote#egg=aldryn-quote
    ```

2. Add `aldryn_quote` to your `INSTALLED_APPS`:

    ```python
    # settings.py
    INSTALLED_APPS += [
        'aldryn_quote',
    ]
    ```

3. To sync the `aldryn-quote` models to the database run:

    ```bash
    python manage.py migrate aldryn_quote
    ```

Additional style choices
------------------------

1. Within the `templates/aldryn_quote/plugins` folder, create a subfolder with a name of your choice.

2. Make sure your template is called `quote.html` and copy it to the subfolder created in step 1.

3. Add the name of your subfolder to a tuple called `QUOTE_STYLES`:

    ```python
    # settings.py
    QUOTE_STYLES = (
        'subfolder',
    )
    ```
