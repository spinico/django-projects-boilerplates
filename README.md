# django-projects-boilerplates

Django projects templates.

- TypeScript
- LiveReload development server
- SQLite database
- Webpack 5 setup for development and production builds
- Deployment with Whitenoise for hashing and compression

**Remark**: the project(s) contains Visual Studio Code settings with preconfigured tasks and launchers. 

## Basic project

**Steps to setup the project:** 

1) Change to a project directory:
	
	```
	cd basic
	```

2) Setup a new virtual environment for the project
	
	```
	python -m venv ".venv"
	```

3) Update pip from the virtual environment

	```
	".venv/Scripts/python" -m pip install --upgrade pip setuptools
	```

4) Install the requirements packages for the virtual environment

	```
	".venv/Scripts/pip" install -r requirements.txt	
	```

5) Install the node packages dependencies

	```
	npm install --loglevel=error
	```

6) Modify the default secret keys in files `settings/development.key` and `settings/production.key`
	
	**Note:** you can generate a random secret key using the following python command.

	```
	".venv\Scripts\python" -c "import random, string; print("""".join([random.SystemRandom().choice(""{}{}{}"".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)]))"
	```

7) Apply migrations to create the required SQLite database tables

	```
	".venv/Scripts/python" manage.py migrate
	```

8) Open the project in Visual Studio Code and launch a debug session.

**Note**: a version of Chrome browser should be installed on the system. 

---
        
## [MIT](http://opensource.org/licenses/MIT) License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.