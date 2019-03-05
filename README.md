# Lessons API

Python 2.7 - Django 1.11 project - Quentin Dufrois

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

This application displays an API that can be connected to a frontend application for instance. The aim is to interface data to create firm account, create subscriptions to lessons, add students to accounts... You can find below the list of the url and the expected JSON format for GET/POST requests.

## JSON formats and URLs

```
GET account + account.students
https://localhost:8000/account/<id>
result = {'name': '...',
	'email: '...',
	'address': '...',
	'students': [
		{'first_name': '...',
		'last_name': '...',
		'birthdate': '...',
		'email': '...'},
		
		{'first_name': '...',
		'last_name': '...',
		'birthdate': '...',
		'email': '...'},
	
		...
	]}
	
======================================================
		
POST account
https://localhost:8000/account/create
data = {'name': '...',
	'email: '...',
	'password': '...',
	'address': '...'}
	
======================================================
		
POST subscription
https://localhost:8000/dashboard/create_sub
data = {'account_id': ...}
		
======================================================
		
POST subscription.status
https://localhost:8000/dashboard/update_status
data = {'subscription_id': ...,
	   'status': ...}

======================================================
		
POST lesson
https://localhost:8000/dashboard/create_lesson
data = {'subscription_id': ...,
	'date': '...',
	'description': '...'}

======================================================
		
GET subscription + subscription.lessons
https://localhost:8000/dashboard/subscription/<id>
result = {'subscritpion_id': '...',
	'status': {
		'status_id': ...,
		'name': '...'
	},
	'subscription_date': '...',
	'lessons': [
		{'lesson_id': ...,
		 'date': '...',
		 'description': '...'},
		
		{'lesson_id': ...,
		 'date': '...',
		 'description': '...'},
		
		...
	]
}

======================================================
		
POST student
https://localhost:8000/account/create_student
data = {'account_id': ...,
	'first_name': '...',
	'last_name': '...',
	'birthdate': '...',
	'email': '...'}
		
======================================================
		
POST student to lesson
https://localhost:8000/dashboard/enrol_student
data = {'student_id': ...,
	'lesson_id': ...}
		
======================================================
		
GET lesson + lesson.students
https://localhost:8000/dashboard/lesson/<id>
result = {'lesson_id': ...,
	'date': '...',
	'description': '...',
	'students': [
		{'first_name': '...',
		'last_name': '...',
		'birthdate': '...',
		'email': '...'},
		
		{'first_name': '...',
		'last_name': '...',
		'birthdate': '...',
		'email': '...'},
		
		...
	]
}
```


