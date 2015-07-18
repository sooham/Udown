# Udown
A social app allowing students to form study sessions. Made for battlehacks 15
### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
django, tastypie. More gems to be added. If you want to install everything in a virtual environment, which is also more recommended.
```
$ virtualenv -p /usr/bin/python2.7 service-env
```
And activate it:
``` 
source service-env/bin/activate
```

* Database configuration
Before running the server, do migrations and syncdb.
```
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
```
* How to run tests
* Deployment instructions

```
python manage.py runserver
```

