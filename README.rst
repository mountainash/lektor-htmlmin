lektor-htmlmin
--------------
|Pypi|

HTML minifier for Lektor that automatically minifies generated .html files.

Uses `htmlmin <https://github.com/mankyd/htmlmin>`_ and looks for .html files,
minifying them as part of the build process.

Installing
##########

You can install the plugin with Lektor's installer::

    lektor plugins add lektor-htmlmin


Or by hand, adding the plugin to the packages section in your lektorproject file::

    [packages]
    lektor-htmlmin = 1.0


Usage
#####

To enable minification, pass the `htmlmin` flag when starting the development
server or when running a build::

    lektor build -O my_build_folder -f htmlmin


When the flag is present, htmlmin will overwrite all HTML files in the output
directory with their minified counterparts.

*Note:* The htmlmin plugin currently minifies every file in the project after a build.
Not just files that have been changed. This should have no ill effects, but
might increase build times if there are many files to minify.


.. |Pypi| image:: https://img.shields.io/pypi/v/lektor-htmlmin.svg?maxAge=3600&style=flat-square
   :target: https://pypi.python.org/pypi/efesto
