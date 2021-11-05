# django-projects-boilerplates

Django projects templates.

- LiveReload development server
- SQLite database
- Webpack 5 setup for development and production builds
- Deployment with Whitenoise for hashing and compression

Remark: The project(s) contains Visual Studio Code settings with preconfigured tasks and launchers 

## Basic project

**Steps to setup the project:** 

1) Change to a project directory

	cd basic

2) Setup a new virtual environment for the project
	
	python -m venv ".venv"

3) Update pip from the virtual environment

	".venv/Scripts/python" -m pip install --upgrade pip setuptools

4) Install the requirements packages for the virtual environment

	".venv/Scripts/pip" install -r requirements.txt	

5) Install the node packages dependencies

	npm install --loglevel=error

6) Modify the default secret keys in files `settings/development.key` and `settings/production.key`
	
**Note:** you can generate a random secret key using the following python command.

	".venv\Scripts\python" -c "import random, string; print("""".join([random.SystemRandom().choice(""{}{}{}"".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)]))"

7) Apply migrations to create the required SQLite database tables

	".venv/Scripts/python" manage.py migrate

8) Open the project in Visual Studio Code and launch a debug session.

Note: a version of Chrome browser should be installed on the system. 

---
MIT License