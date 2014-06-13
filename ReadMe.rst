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

	- Open webportal/webportal/settings.py and do the following changes ::

		DATABASES = {
	    		'default': {
			 'ENGINE': 'django.db.backend.sqlite3',
			 'NAME'  : 'webapp.db',
			 'USER': '',
			 'PASSWORD': '',
			 'HOST': '',                      
			 'PORT': '',
			 }
		}


- Initialize the database using the command ::

			
		python manage.py syncdb


- Start the server using the command ::

			
		python manage.py runserver

License
-------

GNU GPL Version 3, 29 June 2007.

Please refer this `link <http://www.gnu.org/licenses/gpl-3.0.txt>`_
for detailed description.

