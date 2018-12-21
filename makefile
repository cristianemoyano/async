rabbit:
	/usr/local/sbin/rabbitmq-server

celery:
	celery -A tasks worker --loglevel=info

request:
	python request.py