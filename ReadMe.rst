# Webportal
  Webportal for providing education related study material to the students.

## Usage

#. Make sure you are connected to internet.

#. Install pip::
    Use the following command to install pip
        sudo apt-get install pip

#. Install Virtual Environment::
    Use the following command to install virtualenv
        pip install virtualenv
        
#. Create a virtual environment::

    * virtualenv virtualenv_name
    * cd virtualenv_name

#. Check if python is installed in the system::

    * Open terminal and type python. It shows if the python version installed.
    * Otherwise use command 
          sudo apt-get install python-pip

#. Install pre-requisites::
    Use command 
        pip install -r requirements.txt

## Clone

#. Clone this repository::
        git clone https://github.com/khushbu14/webportal

## Install database for server

### Use the following command

    * apt-get install mysql-server 
    * apt-get install python-mysqldb

   Or use pip to install mysql

    * pip install mysql-python

### To use Sqlite(For local server)
    
    * gedit webportal/webportal/settings.py
    * Do the following changes
     
         * 'ENGINE': 'django.db.backend.sqlite3',
	 * 'NAME' : 'webapp.db',
	 * remove user and password.

## Run Server

### python manage.py runserver

    

