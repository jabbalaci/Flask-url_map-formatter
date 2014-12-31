Flask-url_map-formatter
==========================

Beautify the output of `app.url_map`.

The command `print(app.url_map)` displays all of the URL matching routes for the project. However,
the output is not very nice since it is not colorized. This little script adds syntax highlighting,
thus the output is much easier to read IMO.

Screenshot
------

Default output:

    $ ./view_map.py -n

Improved output:

    $ ./view_map.py

![screenshot](https://raw.githubusercontent.com/jabbalaci/Flask-url_map-formatter/master/assets/screenshot.png)

Usage
-------

Simply put this script in the same folder where your main application file
(the one that contains the line `app = Flask(__name__)`) is located.

    .
    ├── main.py                     <- main app. file
    ├── open_in_firefox.py
    ├── requirements.txt
    ├── runserver.sh
    ├── templates
    │   ├── 404.html
    │   ├── 500.html
    │   ├── base.html
    │   ├── index.html
    │   └── user.html
    ├── update_requirements.sh
    └── view_map.py                 <- put it next to the main app. file

Here my main application file is called `main.py`, thus in `view_map.py`
I import `app` from there: `from main import app`.

About
-----

* Author:  Laszlo Szathmary, 2015 (<jabba.laci@gmail.com>)
* Website: <...>
* GitHub:  <https://github.com/jabbalaci/Flask-url_map-formatter>
