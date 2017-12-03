# Djio

Getting Started
---------------
To get up and running, simply do the following:

    $ git clone https://github.com/misteio/djio.git
    $ cd website

    # Install the requirements
    $ pip install -r requirements.txt

    # Perform database migrations
    $ python manage.py makemigrations
    $ python manage.py migrate


**NOTE**: We highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).


###Javascript Reverse URL
We use  [https://github.com/ierror/django-js-reverse](https://github.com/ierror/django-js-reverse).

For generate all your javascript URL for use it in another js file you have to:

```
$ ./manage.py collectstatic_js_reverse
```
So you can use URL from Django like this :
```
Urls['namespace:betterliving-get-house']('house', 12)
```
