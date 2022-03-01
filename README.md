# Flask based application Heroku deployment

## .gitignore
You must add to [.gitignore](.gitignore) all unnecesary folders and files. Especifically .env must be removed avoiding to publish sensitive data in the repository and in the deployed service.

### ⚠️Warning⚠️
If you'v allready included some of these files or folders in any commit, remove them with ```git rm --cache -r fileorfolderpath``` and make a new commit. Then **change any sensitive data in .env in a secure way** becouse the current data is allready in the old commits.

## Install a WSGI server
WSGI provides a interface for HTTP server to talk to your app. Gunicorn can provide this feature:
```bash
pip install gunicorn
```
or, in case you are using `pipenv`:
```bash
pipenv install gunicorn
```

## If you project includes a frontend or static files.

### Install Whitenoise 
```bash
pip install whitenoise
```
or, in case you are using `pipenv`:
```bash
pipenv install whitenoise
```
Then, configure Whitenoise in your Flask application:
```Python
from whitenoise import WhiteNoise
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/", index_file = True)
```
You only needs `index_file = True` parameter if you what Whitenoise to serves `index.html` files automatically. For example if you provides a frontend trough Flask.

### Copy static files
Create a `/static/` folder en your root project folder and copy static files there.

## Update requirements.txt
Ensure your [requirements.txt](requirements.txt) file include all necessary pip packages, including gunicorn.
```bash
pip freeze > requirements.txt
```
or, in case you are using `pipenv`:
```bash
pipenv run pip3 freeze > requirements.txt
```

## Create a Heroku Procfile
Now, we need to instruct Heroku about how to launch our application. We can do it using a [Procfile](Procfile) file.

Create it and put this line on it:
```Procfile
web: gunicorn main:app
```
```app``` is the name of our Flask application and [main](main.py) the module where we can import it.

## Deploy to Heroku
Now we can send our application to Heroku.
* Create a Heroku account, if you have not.
* Create a new Heroku app.
* ⚠️ In the Heroku app settings -> Config Vars, add your relevant .env variables one by one. This is a security sensitive proccess. You need to understand what are you doing.
* In the Deply Heroku app sectio, bind the Heroku app with your Flask application repository.
* Enable Automatic Deploys if you wish.
* Press Deploy Branch.

Thats all. You have your Flask application running in Internet.

## Credits:
https://codigofacilito.com/articulos/deploy-flask-heroku