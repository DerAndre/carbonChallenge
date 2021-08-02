# carbonChallenge

**Coding challenge using Python and the Django web framework**

Why "tiffany"? Because an opal is a gemstone that unfolds its full value only after being processed by manufacturers.
These processed and valuable opals get distributed by Tiffany.

## 1.1. Getting Started

**Prerequisites**

- [python3.8](https://www.python.org/downloads/release/python-383/)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [postman](https://www.postman.com/downloads/) optional

```shellscript
git clone <>
pipenv install
cd carbonChallenge && python manage.py migrate && python manage.py init_usage_types
```

Congrats! the carbonChallenge backend should now be up and running :ok_hand:
<br>
<br>

**Creating users and run application**

To actually use the app you'll want to create at least one user. To do so, there are several ways.<br>
To create a simple user:

```shellscript
python manage.py create_user
```

To create an admin user:

```shellscript
python manage.py create_superuser
```

<br>

Or just use the API and post some JSON to endpoint:
**/auth/users/**

```shellscript
curl -X POST -H "Content-Type: application/json" \
    -d '{"username": "user", "password": "yourSuperSecurePassword!"}' \
    127.0.0.1:8000/auth/users/
```

As you'll see, hopefully, a new user was successfully created! :raised_hands:
<br>
Find out what other urls are available, for instance, to authenticate against the app, using a JWT token (it's 127.0.0.1:8000/auth/jwt/create/).

```shellscript
python manage.py show_urls
```

<br>
Nowadays, many people don't like using tools like curl that much (not judging). Therefore, there is a little postman collection **(carbonChallenge.postman_collection.json)** in the repo you can use to play around with the API.

## 1.2. Data

### 1.2.1. User model

| Field | Type   |
| ----- | ------ |
| id    | long   |
| name  | string |

Actually the django user model to easily support user creation and password handling ([django users](https://docs.djangoproject.com/en/3.2/topics/auth/default/#user-objects))
<br>
<br>

### 1.2.2. Usage model

| Field         | Type                 |
| ------------- | -------------------- |
| id            | long                 |
| user_id       | id (FK user)         |
| usage_type_id | long (FK usage type) |
| usage_at      | datetime             |
| amount        | float                |

### 1.2.3. UsageType model

| Field  | Type   |
| ------ | ------ |
| id     | long   |
| name   | string |
| unit   | string |
| factor | float  |

## 1.3. Tests

To run the test cases and get a coverage report, just run:

```shellscript
coverage run --source='.' manage.py test
coverage report
```

## 1.4. Further notes

Implementation took about 5 hour, including postman and readme.
<br>
A frontend is not included due to vacation days and a bit of workload on the following working day.
