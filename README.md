# Application that exposes HTTP-based API (implemented with Python Flask)

> Handle HTTP requests to update and fetch data from the database.

## Table of contents and structure

```
├── README.md
├── api
│   ├── server.py
│   └── users.db
├── database
│   └── db.py
├── readme_images
├── requirements.txt
└── users.db
└── venv

```

## Scope:
* `api/server.py`:
```
    1. creates API with the Flask framework used;
    2. GET and POST (only application/json content type)
       methods are supported;
    3. API makes calls to Sqlite3 database for updating
       and fetching data;
    4. endpoint exposed /hello/<username> with dynamic
       lookup value for username in request data;
    5. Implemented logic for updating values in DB if the username exists
       and create a new one - if missing;
    6. Username should be a unique value;
    7. The logic for birthday delta calculation is
       applied and respective messages displayed;
```
* `api/user.db` - Sqlite3 database with the records;
* `database/db.py`:
```
    1. creates a Sqlite3 database, with the specified;
    2. creates a table in the database;
```

## Usage:
* Start the application with next commands:

```
    $ cd challenge/
    $ source venv/bin/activate
    $ cd api/
    $ ./server.py
```

* Make a POST request with sending body message as a JSON (use curl or Postman):

```
* endpoint: http://127.0.0.1:5000/hello/<username>
* request: {"dateOfBirth":"1998-01-01"}
```
![alt text](readme_images/1.png)
```
* if the same username will be used - the record will be updated:
```
![alt text](readme_images/2.png)

* Get request for a username and respective messages displayed for a birthday:
```
If birthday is today:
```
![alt text](readme_images/3.png)

```
Any other day:
```
![alt text](readme_images/4.png)
