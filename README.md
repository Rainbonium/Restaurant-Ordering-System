Djongo setup:
- https://www.mongodb.com/compatibility/mongodb-and-django

Django documentation: 
- https://docs.djangoproject.com/en/5.0/intro/tutorial02/
- https://docs.djangoproject.com/en/5.0/intro/tutorial01/

How to run:
**FIRST cd to ~/Project/restaurantSite**

- Make sure you have python installed and working
- (python --version)
- pip install pymongo==3.12.1 (This version is required)
- pip install pytz
- pip install django
- pip install djongo


Run the server: 

**FIRST cd to ~/Project/restaurantSite**

- python manage.py runserver


**Other Commands:**

Migrate the database (Needs to be done anytime a model change is made)
- python manage.py makemigrations, python manage.py migrate

Create admin user (Only if there doesn't already exist one)
- python manage.py createsuperuser
This will allow you to create a local admin user

Sites:
- Admin: ~siteDirectory/admin to see admin portal
- Menupage: / or /menuPage
