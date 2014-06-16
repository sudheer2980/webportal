=========
Webportal
=========

A **Webportal** to provide education material to the students.

(Summer Internship 2014, Indian Institute of Technology, Bombay)

Clone
-----

- Make sure your Internet is working.
- Clone this repo by typing ::

    git clone https://github.com/khushbu14/webportal.git


Installation
------------

- Install Virtual Environment using the following command ::

    sudo apt-get install python-virtualenv

- Create a Virtual Environment ::

    virtualenv /path/to/virtualenv

- Activate the virtualenv using the command ::

    source /path/to/virtualenv-name/bin/activate

- Change the directory to the `webportal/` project using the command ::

    cd /path/to/webportal

- Install pre-requisites using the command ::

    pip install -r requirement.txt

  or you can also type ::

    easy_install `cat requirement.txt`


Usage
-----

- Using sqlite3 (For local server only). We recommend to use `MySQL` for
  server. See `settings.py` file for usage.

  Open `webportal/webportal/settings.py` file and do the following changes ::

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backend.sqlite3',
        'NAME'  : 'webportal.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }


- Initialize the database using the command ::

    cd /path/to/webportal
    python manage.py syncdb

- Start the server using the command ::

    python manage.py runserver


Documentation
-------------

To generate docs:

- Make sure you have Python `Sphinx` installed(See `requirements.txt`
  file)

- Change to `docs/` directory ::

    cd docs

- Export `DJANGO_SETTINGS_MODULE` ::

    export DJANGO_SETTINGS_MODULE=webportal.settings

- Generate HTML ::

    make html

  and browse `docs/_builds/html/index.html` file from Web Browser

- Generate PDF(Optional)

  Make sure you have `latex` installed. ::

    make latexpdf

  PDF file will be generated inside `docs/_builds/latex` directory.

Contributing
------------

- Never edit the master branch.
- Make a branch specific to the feature you wish to contribute on.
- Send us a pull request.
- Please follow `PEP8 <http://legacy.python.org/dev/peps/pep-0008/>`_
  style guide when coding in Python.

License
-------

GNU GPL Version 3, 29 June 2007.

Please refer this `link <http://www.gnu.org/licenses/gpl-3.0.txt>`_
for detailed description.
