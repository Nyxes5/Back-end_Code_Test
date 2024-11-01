# Back-end Code Test

# Getting Started

(Optional) Build and activate the virtualenv for your project.

```bash
python -m venv venv
source venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Then simply apply the migrations:

```bash
python manage.py migrate
```

If you want to use the admin panel:

```bash
python manage.py createsuperuser
```


You can now run the development server:

```bash
python manage.py runserver
```

You can run the tests with:

```bash
python manage.py test
```