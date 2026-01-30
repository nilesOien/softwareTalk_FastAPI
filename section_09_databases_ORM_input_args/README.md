
# Section 9.0

We now run something like a real server.

We connect to a database that has about 6 weeks of H-Alpha file
listings. We take input arguments that let us filter by site
code and time range. There is more than one API end point.

One end point simply delivers the file listing.

Another end point groups them and delivers counts of files.
The grouping can be done either by hour or by day.

ruff can be used to check the code with **uv run ruff check**

pytest unit tests can be run with **pytest -v**

The steps are :

* Run **installPackages.sh** to install the packages
* Run **startServer.sh** to start the server


* Optionally run cleanup.sh to clean up


