## PCC 34 - DRF

A simple API to add coding tips, inspired by @python_tip and following DRF's awesome tutorial (part 1 - 4)

To run it locally:

	git clone https://github.com/pybites/codetips
	cd codetips
	python3 -m venv venv 
	echo 'export DJANGO_ENV=local' >> venv/bin/activate
	echo 'export SECRET_KEY=some-random-string' >> venv/bin/activate
	source venv/bin/activate
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver

Go to `http://127.0.0.1:8000/tips/` in the browser and add some code tips using the user you just created.

Or use [Postman](https://www.getpostman.com/).

Or use `httpie` (included in requirements) from command line:

	http -a guest:handl3bar POST http://127.0.0.1:8000/tips/ tip="How to code in Python? >>> python -c 'import this'" (defaults to language=python)
	http -a guest:handl3bar POST http://127.0.0.1:8000/tips/ language="javascript" tip="alert('most boring codetip');"
	http -a guest:handl3bar POST http://127.0.0.1:8000/tips/ language="javascript2" tip="alert('most boring codetip');" (errors: wrong lang / no dup tip!)

Retrieve tips:

	http http://127.0.0.1:8000/tips/
	http http://127.0.0.1:8000/tips/1/
	http http://127.0.0.1:8000/users/
	http http://127.0.0.1:8000/users/1/

TODO: get it running on Heroku ...
