# Justlearn

## Backend project of programming private lessons website.
### Used technologies:
- Python
- Django
- Docker
- Celery
- Redis
- PostgreSQL
- Django Rest Framework

### Project handles:
- Creating custom users
- Authenticating users via token authentication
- Adding items to favorites
- Sending notifications via email
- Custom permissions system
- Celery tasks 
- Redis docker image to handle celery's functionalities.

Project is fully built on docker and with PostgreSQL as a database. 

Rest Api in this project is documented and  displayed with the use of drf-spectacular library and swagger.
## Available endpoints:
### Comps endpoints :
/api/comps/
- (GET)
- (POST)
- {id}/ (GET)
- {id}/ (PUT)
- {id}/ (PATCH)
- {id}/ (DELETE)
- {id}/favorite (POST)
### User Favorites endpoints:
/api/user-favorites/
- (GET)
- (POST)
- {id}/ (GET)
- {id}/ (PUT)
- {id}/ (PATCH)
- {id}/ (DELETE)
### User endpoints:
/api/user/
- create/ (POST)
- me/ (GET)
- me/ (PUT)
- me/ (PATCH)
- token/ (POST)

### Schema endpoints:
/api/schema

