Webportal
=========

|	Webportal for providing education related study material to the students.

Usage
=====

- Make sure you are connected to internet.

- Install pip Using the following command:

			+-------------------------------+
			|				|
			|  sudo apt-get install pip	|
			|				|
			+-------------------------------+

- Install Virtual Environment Using the following command:

			+-------------------------------+
			|				|
			|  pip install virtualenv	|
			|				|
			+-------------------------------+

- Create a Virtual Environment:
			
			+-------------------------------+
			|				|
			|virtualenv virtualenv_name	|
			|				|
			|cd virtualenv_name		|
			|				|
			+-------------------------------+


- Check if python is installed in the system , open terminal and type python It shows which version of python is installed.
  Otherwise use command

			+---------------------------------------------------------------------------------------+
			|											|
			| 											|
			|											|
			|											|
			|											|													
			|	sudo apt-get install python-pip							|			    
			|											|
			+---------------------------------------------------------------------------------------+

- Install pre-requisites Using the command:

		
	
			+---------------------------------------+
			|					|
			|  pip install -r requirements.txt	|
			|					|
			+---------------------------------------+


Clone
=====

- Clone this repository:

	- git clone https://github.com/khushbu14/webportal/

- Install database for server using the command:

			+---------------------------------------+
			|					|
			|apt-get install mysql-server		|
			|					|
			|apt-get install python-mysqldb		|
			|					|
			+---------------------------------------+

	Or use pip to install mysql

			+-------------------------------+
			|				|
			|				|
			|pip install mysql-python	|
			|				|
			|				|
			+-------------------------------+
			
- To use Sqlite (For local server)

	- Open webportal/webportal/settings.py

	- Do the following changes

		* 'ENGINE': 'django.db.backend.sqlite3',
		* 'NAME'  : 'webapp.db',
		*  remove user and password.

- Start the server using the command

			+-------------------------------+
			|				|
			|				|
			|python manage.py runserver	|
			|				|
			|				|
			+-------------------------------+

