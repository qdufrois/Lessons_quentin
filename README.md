# Lessons API

Python 2.7 - Django 2.0 project - Quentin Dufrois

## Installation

### Copy the unzipped folder in the desired directory

### Start the virtualenv and launch the server
In the terminal:

* Go to the project directory
```
cd path/to/project_folder/
```

* Activate the environment (MacOS/Linux)
```
cd path/to/env
source env/bin/activate
```

* Then run the django server
```
python manage.py runserver
```

* Open your web browser and enter the URL displayed in the terminal (http://127.0.0.1:8000/ or http://localhost:8000/).



## The Application

This application displays an API that can be connected to a frontend application for instance. The aim is to interface data to create firm account, create subscriptions to lessons, add students to accounts. You can find below the list of the url and the expected JSON format for GET/POST requests
