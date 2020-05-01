#Project: Tweetme-2 (Twitter Clone)

>**YouTube Channel:** CodingEntrepreneurs
>
>**Video:** Create a Twitter-like App with Python Django JavaScript and React. Full TUTORIAL
>
>**URL:** https://www.youtube.com/watch?v=f1R_bykXHGE
>
>**GitHub:** https://github.com/codingforentrepreneurs/Tweetme-2

>**Resources:**
>- https://www.codingforentrepreneurs.com/t/setup


##**Notes:**

- **AJAX** - Asynchronous JavaScript Requests, allows Django and React 
to communicate without reloading a webpage
- **JavaScript Clients** - React, VueJS, AngularJS
- **-m** - https://docs.python.org/3.1/using/cmdline.html
- Put a **period** at the end of 'startproject' to create a Django project 
in the same directory as the pipfiles without **subdirectories**:
    >django-admin startproject new_project **.**
- **PyCharm Run Config:** After setting up the project with pipenv,
create a run config by going to 'Settings>Project: PROJECT_NAME>Python Interpreter',
select existing interpreter and add the Pipenv project interpreter.
Now you should be able to run the server using PyCharm's run interface.
- **Pylint** - Install with Pipenv to pifile dev-packages:
    >pipenv install pylint --dev

- To run Pylint:
    >pylint <MODULE/DIRECTORY>
- **id** is automatically added by Django as the first field to a model.
User added fields follow in the model's creation,
    >id = models.AutoField(primary_key=True)