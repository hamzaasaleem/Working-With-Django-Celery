# Django Celery Demo

# Project Details

## Django Project 
    
    Address: 127.0.0.1
    Redis Running on Port:8000
    url: 127.0.0.1:8000

## Celery Broker 

    Redis Running on Port:6379
    url: 127.0.0.1:6379
    
## Monitoring Tool - Flower
    
    Running on Port: 5566
    Default URL: http://127.0.0.6:5566

## Task Scheduler - Beat
    
    1- Celery Beat is used to send Email after Every 10 minutes
    2- You can change the interval from database visiting 127.0.0.1:8000/admin after running the server
    



# Steps to Start the Project
## Setting up ENV
    1- python -m venv venv
    2- source venv/bin/activate (for LINUX) | venv/Scripts/activate (For Windows)
    3- pip install -r requirements.txt
    
## Running server

    1- python manage.py migrate
    
    Create Django Admin by following Steps
    1- python manage.py createsuperuser
    2- fillup the form and continue to next
    
    After creating super user run the following command:
    1- python manage.py runserver

## Start Celery
    Run the Following Command:
    1- celery -A django-celery-demo worker -l INFO

## Start Flower - Monitoring Tool
    Run the Following Command:
    1- celery -A django-celery-demo flower  --address=127.0.0.1 --port=5566

## Start Beat - Periodically Scheduler
    First of all you need to setup the Beat Scheduler in Database follow the commands to get it done
    1- localhost:8000/admin/
    2- Enter the Credentials of your Super User
    3- Login
    4- You will see a Section Named " PERIODIC TASKS "
    5- Under that section there is a table named " Intervals "
    6- Click on it and add a new interval
    7- This is basically the delay in each email to send
    8- Now you need to select the task from the table named " Periodic tasks "
    9- Open it up and add a new task.... Give it a name
    10- In " Task (registered) " field you need to select " app.task.send_email_task " from the dropdown
    11- leave the reset and find " Interval Schedule " field and select the interval from there
    12- Save it 
    
    Now, 
    Run the Following Command in your new Terminal to start the Beat:
    1- celery -A django-celery-demo beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# Environment File
create a .env file in the root directory and copy the following into it

```
SECRET_KEY=kL_3lnHnr-73PFeeuhdfPjPSqr7KxAhbC3EwlIe7MMDmwlRFFeaGRZd7ZYYrSXtfypk
DATABASE_URL='sqlite:///db.sqlite3'
CELERY_BROKER_URL='redis://127.0.0.1:6379'
CELERY_BACKEND='redis://127.0.0.1:6379'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = <email here>
EMAIL_HOST_PASSWORD = <password here>
```

# All DONE!! :)