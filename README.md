Djio
===

Getting Started With Docker
---------------

### Requirements:
We use  [Docker](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/).
#### Build Image
    $ docker-compose build
#### Mount Image
    $ docker-compose up
Then you can access to this application with : http://localhost

You can change port and host, by changing Nginx Configuration (config/nginx/djio.conf)
  
Getting Started Without Docker
---------------
To get up and running, simply do the following:

    $ git clone https://github.com/misteio/djio.git
    $ cd website

    # Install the requirements
    $ pip install -r requirements.txt

    # Perform database migrations
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Collect static files
    $ python manage.py collectstatic --noinput
    
    # Create User Admin for BackOffice
    $ python manage.py createadmin
    
    # Launch app
    $ python manage.py runserver

Then you can access to this application with : http://localhost:8000

**NOTE**: We highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).


Package configuration and what you should know
---------------

#### Javascript Reverse URL
We use  [https://github.com/ierror/django-js-reverse](https://github.com/ierror/django-js-reverse).

For generate all your javascript URL for use it in another js file you have to:

```
$ ./manage.py collectstatic_js_reverse
```
So you can use URL from Django like this :
```
Urls['namespace:betterliving-get-house']('house', 12)
```
