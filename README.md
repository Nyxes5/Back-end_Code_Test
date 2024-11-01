# Back-end Code Test
## Walkthrough

API Documentation using swagger at ``/docs``
Django admin panel (superuser needed) at ``/admin``
Django Rest Framework at ``/api``

You can use both Swagger and/or Django Rest Framework to use GET/POST request without a front-end. 

### Person
|Field|Type|Description|
|-|-|-|
|id|UUIDField|Primary key. Auto-generated unique identifier for each person.|
|name|Charfield|The person's name. Must be unique.|
|age|PositiveIntegerField|The person's age in years, as a positive integer. Must be 18+.|

### Create Person

You can create a person using POST request to ``/api/persons`` with a body:
|Field|Type|Description|
|-|-|-|
|name|Charfield|The person's name. Must be unique.|
|age|PositiveIntegerField|The person's age in years, as a positive integer. Must be 18+.|

### Search Person
You can search a person using GET request to ``/api/persons?search=<search>``.
You can search on either name or age and it doesn't have to be a perfect match as long as the search term is a substring of name or age.

## Getting Started

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