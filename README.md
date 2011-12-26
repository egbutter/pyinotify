# Pyinotify

* License          : MIT
* Project URL      : [http://github.com/egbutter/pyinotify](http://github.com/egbutter/pyinotify)
* Project Wiki     : [http://github.com/egbutter/pyinotify/wiki](http://github.com/egbutter/pyinotify/wiki)
* Original pyinot. : [http://github.com/seb-m/pyinotify](http://github.com/seb-m/pyinotify)
* Original watcher : [https://bitbucket.org/briancurtin/watcher](https://bitbucket.org/briancurtin/watcher)


## Dependencies

* Linux > 2.6.13 
* Win > 2000/NT
* Python > 2.4


## Install

### Install from the distributed tarball

    # Choose your Python interpreter: either python, python2.6, python3.1,..
    # Replacing XXX accordingly, type:
    $ pythonXXX setup.py install

### Or install it with `easy_install` (currently seems to be available only for Python2)

    # Install easy_install
      $ apt-get install setuptools
    # Or alternatively, this way
      $ wget http://peak.telecommunity.com/dist/ez_setup.py
      $ python ez_setup.py
    # Finally, install Pyinotify
      $ easy_install pyinotify


## Watch a directory

Install pyinotify and run this command from a shell:

    $ python -m pyinotify -v /my-dir-to-watch
