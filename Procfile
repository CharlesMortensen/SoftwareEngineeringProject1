release: python3 lasertag/manage.py migrate
web: cd lasertag && daphne -b 0.0.0.0 -p $PORT lasertag.asgi:application