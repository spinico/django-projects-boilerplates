from waitress import serve

from conf.wsgi import application

if __name__ == '__main__':
    serve(application, listen='0.0.0.0:8000', url_scheme='https')
