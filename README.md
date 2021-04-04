# Jorge-Vergara-1994-08-15
Currency format exercising

## Install librarys
```console
user@user:~$ pip install -r requeriments.txt 
```

## Run API
```console
user@user:~$ python manage.py runserver
```

## Run Test
```console
user@user:~$ ./manage.py test
```
<img width="525" alt="Screen Shot 2021-04-04 at 13 49 10" src="https://user-images.githubusercontent.com/5691763/113518547-8ec10680-954c-11eb-981e-cc9a4e03f3a4.png">

## Coverage Test Report
```console
user@user:~$ coverage run --source='.' manage.py test currency_api
user@user:~$ coverage report
user@user:~$ coverage html

```

<img width="841" alt="Screen Shot 2021-04-04 at 00 03 27" src="https://user-images.githubusercontent.com/5691763/113518504-59b4b400-954c-11eb-9b9b-72a4c89cf6c7.png">

## Documentation
### url/docs


<img width="1279" alt="Screen Shot 2021-04-04 at 13 50 37" src="https://user-images.githubusercontent.com/5691763/113518571-c4fe8600-954c-11eb-96ba-3753cd52b0c3.png">

## Config MongoDB

setup.py
```py
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'currency',
    }
}
```

Insert Data to Mongo DB
```console
user@user:~$ python init_db_data.py  
```

## API

<img width="1280" alt="Screen Shot 2021-04-04 at 13 58 49" src="https://user-images.githubusercontent.com/5691763/113518765-ed3ab480-954d-11eb-8e1c-0ffeff37138c.png">

<img width="1031" alt="Screen Shot 2021-04-04 at 13 55 11" src="https://user-images.githubusercontent.com/5691763/113518773-f1ff6880-954d-11eb-9c03-8935392d41fd.png">




