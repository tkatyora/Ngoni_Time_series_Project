Wellcome To Network Management System  Web Application

Note:1.This web Application is not mobile and  tablet responsive ,it onl looks good on 1024px Laptop
    2. This web Application is only Accessed on a local server it can not be Accessed by others online
    3. The code of this Application is hosted on github


HOW TO RUN THIS APPLICATION ON YOUR LAPTOP

1. Make sure you have python on your machine ,
    run python --version on cmd to check if you have installed python
2. Create virtual environment on your machine 
    run python -m venv venv
3. Activate the virtual environment
    run source venv/scripts/Activate  (on git bash) 
            or 
    run ./venv/scripts/Activate (on cmd)

RUN THE FOLLOWING COMMANDS SEQUENCIALLY
4.git clone 
5. pip install -r requirements
6. cd Backend
7. python manage.py runserver

And Enjoy the system


INFORMATION OF THIS WEB APPLICATION

This We Application is build using the folloing technologies

Backend
Django - A Python web Framework
database - sqlite

Frontend
Django Templates
bootsrap
crisp forms

This Application contains The following modules which perfoms specific functions
This modules are Django Application

modules
1.Accounts
2.Main
3.Portal

Accounts
This modules is responsible for Managing Users , 
such as creating users ,Autentication of users ,Validation of users ,
managing users profile

log In by
1.by username 


Main
This modules is responsible for The ome page and the about page


