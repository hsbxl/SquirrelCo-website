# SquirrelCo :

Squirrelco is the name of the internet provider project of the hackerspace. As we grow, we will add stuff that we do.

This django site is the base template for our publicity. This might become an extranet for other hackerspaces or other entities as we grow.


## How to run in dev :

```shell
virtualenv -p python3.11 venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

# When running in debug False :
```shell
./manage.py collectstatic
./manage.py runserver --insecure
```

# CSS : 
To install the CSS bundler : 
```shell
npm install -D tailwindcss
npx tailwindcss init
```

To update CSS files (they use the tailwinds framework)
```shell
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css
```