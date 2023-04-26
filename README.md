# Justlearn

## Backend project of programming private lessons website.
This project containts full rest api for website enabling teachers and students to connect in order to learn programming. It handles:
- Creating custom users
- Authenticating users
- Crating Teacher/Student profiles based on information while registering a user.
- Chat system
- Custom permissions system
- Celery tasks 
- Static/ Media Files
- Redis docker image to handle celery's functionalities.
## Used technologies:
- Python
- Django
- Docker
- Celery
- Redis
- PostgreSQL
- Django Rest Framework

Project is fully built on docker and with PostgreSQL as a database. 

Rest Api in this project is documented and  displayed with the use of drf-spectacular library and swagger.
## Available endpoints:
### User endpoints :
/api/user/
- create/ (POST)
- me/ (GET)
- me/ (PUT)
- me/ (PATCH)
- token/ (POST)
### Teachers endpoints:
/api/teachers/
- (GET)
- (POST)
- {id}/ (GET)
- {id}/ (PUT)
- {id}/ (PATCH)
- {id}/ (DELETE)
- my_profile/ (GET)
- my_profile/ (PATCH)
- my_profile/ (POST)
### Student endpoints:
/api/students/
- (GET)
- (POST)
- {id}/ (GET)
- {id}/ (PUT)
- {id}/ (PATCH)
- {id}/ (DELETE)
- my_profile (GET)
- my_profile (PATCH)
- my_profile (POST)
### Comments endpoints:
/api/comments
- -//- (GET)
- -//- (POST)
- {id}/ (GET)
### Student's problems endpoints:
/api/problems/
- (GET)
- (POST)
- {id}/ (GET)
- {id}/ (PUT)
- {id}/ (PATCH)
- {id}/ (DELETE)
### Teacher's advertisements endpoints:
/api/advertisement/
- (GET)
- (POST)
- {id}/ (GET)
- {id}/ (PUT)
- {id}/ (PATCH)
- {id}/ (DELETE)s:
### Chat between teacher and student endpoints:
api/chats
- (GET)
- {id}/ (GET)
- {id}/add_to_chat/ (POST)
- {id}/leave/ (POST)
- {id}/send_message/ (POST)
- {id}/create_chat/ (POST)
### Schema endpoints:
/api/schema


I worked on this project with my friend to test our github collaboration skills.
