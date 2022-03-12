# Team 2 Lasertag Project

A python lasertag application built on the [django web framework](https://www.djangoproject.com/).

To install, clone the repository and install the python dependencies listed in the requirements.txt file. This can be done with:

> pip install -r requirements.txt

Next, you will need to set up a local database for the application. Run the following command in the lasertag folder (the one containing manage.py):

> python manage.py migrate

Once this is done, the server can be started locally by running the following command in the lasertag folder:

> python manage.py runserver

The server will run on [localhost:8000](http://localhost:8000). For other management commands, see the [django documentation](https://docs.djangoproject.com/en/4.0/ref/django-admin/).