# carbonChallenge

**Coding challenge using Python and the Django web framework**

Why "tiffany"? Because an opal is a gemstone that unfolds its full value only after being processed by manufacturers.
These processed and valuable opals get distributed by Tiffany.

## 1.1. Getting Started

**Prerequisites**

- [python3.8](https://www.python.org/downloads/release/python-383/)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [postman](https://www.postman.com/downloads/) optional

## 1.1.1. Start application

**Local approach**
<br>
If you want to run the backend server in a local environment using pipenv, change to the project directory and run:

```shellscript
pipenv install
cd carbonChallenge && python manage.py migrate && python manage.py init_usage_types
```

**Container approach**
<br>
Assuming you want to run the server in a docker container, just run:

```shellscript
docker build -t carbon_challenge .
docker run --rm -d -p 8000:8000 carbon_challenge
```

Congrats! the carbonChallenge backend should now be up and running :ok_hand:
<br>
<br>

## 1.1.2. Creating users and run application

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

## 1.3. Sorting & Filtering

By default, usage objects are ordered by the field "usage_at" in descending order.
<br>
To change the default behavior, provide the URL query parameter "sorting".<br>
Examples:

- ...?sorting=amount will order usages by amount ascending<br>
- ...?sorting=-amount will order usages by amount descending<br>
  <br>

Filtering can be done by just using the model fields:

- amount
- usage_at
- usage_type
- user

To filter by date range, pass the two URL query parameter "time_range_from" and "time_range_to".<br>
Examples:

- ...?time_range_from=2021-08-01&time_range_to=2021-08-31<br>
  <br>

## 1.4. Tests

To run the test cases and get a coverage report, just run:

```shellscript
coverage run --source='.' manage.py test
coverage report
```

## 1.5. Further notes

Implementation took about 5 hour, including postman and readme.
<br>
A frontend is not included due to vacation days and a bit of workload on the following working day.
