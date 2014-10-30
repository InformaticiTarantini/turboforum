TurboForum
==========

TurboGears2 based forum

Installation and Setup
======================

Install ``turboforum`` using the setup.py script::

    $ cd turboforum
    $ python setup.py develop

Create the project database for any model classes defined::

    $ gearbox setup-app

Start the paste http server::

    $ gearbox serve

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ gearbox serve --reload --debug

Then you are ready to go.
