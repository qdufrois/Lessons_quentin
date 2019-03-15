# Lessons API

Python 2.7 - Django 1.11 project - Quentin Dufrois

## Installation

### Copy the unzipped folder in the desired directory

### Start the virtualenv, set the database and launch the server
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

* You have to create a MySQL-type database and connect it to the application (via the file settings.py), then apply the migrations
```
python manage.py makemigrations
python manage.py migrate
```

* All the data will come from the POST requests, except for the Status model instances, that you should add as follow in the python shell (feel free to adapt the names to your needs)
```
python manage.py shell
>>> from dashboard.models import Status
>>> Status.objects.create(name='Active')
>>> Status.objects.create(name='Paused')
>>> Status.objects.create(name='Cancelled')
>>> quit()
```
* Then run the django server
```
python manage.py runserver
```
* While opening your brower, a homepage generated with DRF Docs should then be accessible at http://127.0.0.1:8000/ or http://localhost:8000/

* NB: a permission system regulates the API, you have to create a (super)user, and log in, either in the admin or via the browsable API

## The Application

This application displays an API that can be connected to a frontend application for instance. The aim is to interface data to create firm account, create subscriptions to lessons, add students to accounts and lessons... You can find below the list of the url and the expected JSON format for GET/POST/PUT/PATCH/DELETE requests.

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

POST student
https://localhost:8000/account/create_student
data = {'account_id': ...,
	'first_name': '...',
	'last_name': '...',
	'birthdate': '...',
	'email': '...'}
	
======================================================

DELETE student
https://localhost:8000/account/delete_student/<id>

=====================================================
		
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
https://localhost:8000/dashboard/subscription_lessons/<id>
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

======================================================

PUT, PATCH lesson locked
https://localhost:8000/dashboard/lock_lesson/<id>
data = {'locked': ...}

======================================================

GET account + account.subscriptions
http://localhost:8000/dashboard/subscriptions/<account_id>

result = {'name' : '...',
		  'email': '...',
		  'subcriptions': [
			  {'subscription_id': ...,
			  'status': {'status_id': ...,
			  			'name': '...'}
			  },
			  
			  {'subscription_id': ...,
			  'status': {'status_id': ...,
			  			'name': '...'}
			  },
			  
			  ...
		 ]
	}

======================================================

GET status
http://localhost:8000/dashboard/all_status

result = [
	    {
		"status_id": ...,
		"name": ...
	    },
	    {
		"status_id": ...,
		"name": ...
	    },
	    
	    ...
	]

```


