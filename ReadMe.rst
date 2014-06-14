=========
Webportal
=========

A **Webportal** to provide education material to the students.



			

Clone
-----

- Make sure your internet is working.

- User's can clone this repo by typing ::

		git clone https://github.com/khushbu14/webportal.git


Installation
------------

- Install Virtual Environment Using the following command ::

		sudo apt-get install python-virtualenv    
								    
- Create a Virtual Environment ::
			
		virtualenv /path/to/virtualenv


- Activate the virtualenv using the command ::

		source bin/activate

- Change the directory to the **webportal** project using the command ::

		cd /path/to/webportal

- Install pre-requisites Using the command ::

		pip install -r requirements.txt


Usage
-----

- Use sqlite3 (For local server)

	- Open webportal/webportal/settings.py

	- Do the following changes

		* 'ENGINE': 'django.db.backend.sqlite3',
		* 'NAME'  : 'webapp.db',
		*  Keep the 'USER' and 'PASSWORD' fields blank


- Initialize the database using the command ::

			
		python manage.py syncdb


- Start the server using the command ::

			
		python manage.py runserver

