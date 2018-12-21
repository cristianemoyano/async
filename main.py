from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
