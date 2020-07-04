# backend_FTL

Django restAPI to display users with their activity periods.

Setup Instructions

### Steps

1. Django Environment Setup

    `python -m venv env_name` 
     
    `source env_name/bin/activate`
     
    `pip install -r requirements.txt`

2. Run Server

     `python manage.py migrate --sync-db`
    
    > *to migrate all the migrations*
      
     
    `python manage.py insert_data`

     > *to insert sample data of users and activity.*

     > *use --length 100 (1-1000 _default:100_)to customize the No. of data should be inserted*

    `python manage.py runserver`
     > *to run the server*


### Environment Variables

|   VARIABLE NAME	|   DESCRIPTION	|
|---	|---	|
|   DEBUG_VALUE	 |   Debug value depending on dev or prod env	|
|   SECRET_KEY	|   Secret Key for the Django Application	|

### Usage

`admin/`

`^users/$ [name='user-list']`

`^users/(?P<pk>[^/.]+)/$ [name='user-detail']`