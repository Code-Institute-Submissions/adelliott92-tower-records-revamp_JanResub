# Tower Records Revamp

Tower Records revamp is full stack django project and redesign of the current Tower Records website towerrecords.ie

![Tower Records Revamp Logo](/assets/images/readme/tower_records_revamp_logo.png)

You can visit the website by [clicking here](tower-records-revamp.herokuapp.com)

## Table of contents

[UX (User Experience)](#UX)

[Features](#features)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

[Known Bugs](#bugs)

[Credits](#credits)

<a name="UX"></a>
## UX (User Experience)

<a name="features"></a>
## Features

<a name="technologies"></a>
## Technologies Used

### Languagues Used

- HTML
- CSS
- Python

### Frameworks and Programs Used

- [Visual Studio Code](https://code.visualstudio.com/) - The developer used Visual Studio Code for their IDE to build the website.
- [Django](https://www.djangoproject.com/) - Django framework was used to build the application.
- [Bootstrap v5.1.3](https://getbootstrap.com/) - Bootstrap was used to make the website responsive across all devices.
- [Font Awesome v5.15.4](https://fontawesome.com/) - Font awesome was used to provide icons for the website.
- [Google Fonts](https://fonts.google.com/) - Google Fonts was was used to style text of the website.
- [Popper JS](https://popper.js.org/) - Popper JS was used with bootstrap to make site interactive.
- [Git](https://git-scm.com/) - Git was used in Visual Studio Code IDE for version control to commit and push to GitHub.
- [GitHub](https://github.com/) - GitHub was used to stored the website and website was deployed to GitHub pages to make website live.
- [Figma](https://www.figma.com/) - Figma was create to design of the wireframes and site images.

### Python Packages Used

- [asgiref 3.4.1](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.

- [dj-database-url 0.5.0](https://pypi.org/project/dj-database-url/) - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

- [Django 3.2.9](https://pypi.org/project/Django/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.

- [django-heroku 0.3.1](https://pypi.org/project/django-heroku/) - This is a Django library for Heroku applications that ensures a seamless deployment and development experience.

- [gunicorn 20.1.0](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.

- [Pillow 8.4.0](https://pypi.org/project/Pillow/) - This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

- [psycopg2 2.9.2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.

- [pytz 2021.3](https://pypi.org/project/pytz/) - This library allows accurate and cross platform timezone calculations using Python 2.4 or higher.

- [sqlparse 0.4.2](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

- [whitenoise 5.3.0](https://pypi.org/project/whitenoise/) - WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service.

<a name="testing"></a>
## Testing


- [W3C Markup Validation Service](https://validator.w3.org/) - W3C Markup tool was to validate and ensure no syntax errors in HTML for website pages.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - W3C CSS Validation tool was used to validate and ensure no syntax errors in the CSS stylesheet.
- [WebAIM Constrast Checker](https://webaim.org/resources/contrastchecker/) - WebAIM Constrast Checker tool was used to ensure contrast between foreground and background colors meets accessibility guidelines.
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) - This tool was used to ensure that web content on the website was more accessible to individuals with disabilities and meet accessibility guidelines.
- [Can I Use...](https://caniuse.com/) - It was used to check what techologies were supported in different web browser versions.
- [Coverage.py](https://docs.djangoproject.com/en/3.2/topics/testing/advanced/) - It was used for testing every single line in your python application using tests. 

<a name="deployment"></a>
## Deployment

This was project was developed in Visual Studio Code editor and git was used within Visual Studio Code to commit and push to GitHub and deploy to Heroku.

### Prerequisites

- Procfile
- requirements.txt
- runtime.txt

1. Download and install Heroku CLI [click here for install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
2. Sign up to  [Heroku.com](https://www.heroku.com/)

3. In settings.py file in your project folder ensure that you have the following set

```
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
```
4. Create the Procfile by running below command in your local CLI

```
    touch Procfile
```

5. Add the following line to Procfile

```
    web: gunicorn main.wsgi:application --log-file -
```
6. Install python packages using below command in your local CLI

```
    pip install gunicorn django-heroku
```

7. Run the following command in your local CLI in your root directory for your app to create requirements.txt which will captures all python packages that are used in your Django application.

```
    pip freeze > requirements.txt
``` 

8. In settings.py file in your project folder ensure the following lines at the top of your file.

```
    import os
    import django_heroku
```

9. Add this line following line in settings.py to activate django_heroku.

```
    django_heroku.settings(locals())
```
10. In settings.py file set the DEBUG to false when deploying the application to production.

```
    DEBUG = False
```
11. Run the following command to initialize repository

```
    git init
```

12. Run next command to stage all your files for commiting to [Heroku.com](https://www.heroku.com/).

```
    git add .
```

13. Now run last command to push your application to github.

```
    git commit -m “Deploy application”
```

14. Run next command to login to Heroku CLI which will your web browser to sign in.

```
    heroku login
```

15. Run next command to create the app in heroku and you the parameter region and set value to eu.

```
    heroku create tower_records_revamp --region eu
```
16. Now run the last command to deploy the application to Heroku

```
    git push heroku master
```

17. Your application is built and deployed to Heroku and you should see your application normally the link should display as the following

    tower-records-revamp.herokuapp.com

<a name="bugs"></a>
## Known Bugs

- Images that have been added using admin page will not load because Heroku is set to readonly and Amazon S3 still has not been setup.

- Navigation links and search don't work as they are still in the process of being setup.

<a name="credits"></a>
## Credits

### Code
- [Bootstrap v5.1.3](https://getbootstrap.com/) - Bootstrap was heavily used in this project for building the site and CSS grid on about.html and services.html

### Acknowledgements

- My mentor Excellence Ilesanmi has been really helpful for providing me with useful insights and advice on creating my website. 
- Code Institute Tutor Support and Students in Slack all have been really helpful with tips for completeting my first milestone project.