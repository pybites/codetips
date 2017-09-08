## PCC 34 - DRF

A simple API to add coding tips, inspired by @python_tip and following DRF's awesome tutorial (part 1 - 4)

To run it locally:

	git clone https://github.com/pybites/codetips
	cd codetips
	python3 -m venv venv && source venv/bin/activate
	cd src
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver

Go to `http://127.0.0.1:8000/tips/` in the browser and add some code tips using the user you just created.

Or use [Postman](https://www.getpostman.com/).

Or use `httpie` (included in requirements) from command line:

	http -a user:pass POST http://127.0.0.1:8000/tips/ language="javascript" tip="yet another tip 33" 
	http -a user:pass POST http://127.0.0.1:8000/tips/ tip="yet another tip 34" (defaults to language=python)

Retrieve tips:

	http http://127.0.0.1:8000/tips/
	http http://127.0.0.1:8000/tips/1/
	http http://127.0.0.1:8000/users/
	http http://127.0.0.1:8000/users/1/

App is also on Heroku: [https://pybites-tips.herokuapp.com/](https://pybites-tips.herokuapp.com/)

Maybe we should add tips for real, ping us for a user (or we'll add registration over time ...)

Have fun.
