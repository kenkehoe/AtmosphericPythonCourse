# Here are some notes on making a Pythong package

## Flat vs. source
The first thing to think about with the Python package is will this code be installable. Chances are if it is good code then some day (or initially) you will want to make the package installable. So take the time to think about and build out the file/directory/module strucutre.

Remeber that when there are folders in a Python package they translate into sub-modules when importing the package. For example the datetime package has a typical import like this:

<pre>
from datetime import datetime, date
date.today()
</pre>

This means the top level directory is called _datetime_ with a file called _datetime_ and _date_. In those files there is a method called _today_. 

