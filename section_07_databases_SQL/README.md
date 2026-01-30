
# Section 7.0

This demostrates that FastAPI can serve things out from a database.

Notice that an SQL string is passed to the database to do the select.

Also, notice that the connection details  for the database are
put in a .env file and that there is a python module for reading .env files.
These files contain things that should not go into a public facing repo
like database passwords (although there is no password used here).

There are similar modules to deal with .env files in other languages, like Rust.

Following this practice means that if the NSF decides that it wants all
code checked into a public facing repo, we could easily comply.

The steps are :

* Run **installPackages.sh** to install the packages
* Run **startServer.sh** to start the server
* Look at the served out JSON at http://127.0.0.1:8007/static-dict
* Optionally run cleanup.sh to clean up


