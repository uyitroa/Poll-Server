# Poll-Server
Requirement: pymongo, mongodb, python3.6, django2, djangorestframework

pymongo:
```
pip3 install pymongo
```

mongodb (on os x): 
```
brew install mongo
```

django2:
https://docs.djangoproject.com/en/2.0/releases/2.0/

python3.6 (or later):
https://www.python.org/downloads/

djangorestframework:
```
pip3 install djangorestframework
```

django-cors-headers:
```
pip3 install django-cors-headers
```


Also you will need folder `data/db` to store data with mongo
```
mkdir data
mkdir data/db
```

To start the server:
```
mongod
python3 runserver.py
```
