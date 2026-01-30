
# Section 6.0

This demostrates the basic idea of unit tests for FastAPI apps,
as well as git hooks, which can gatekeep the code that is
checked in to git.

The steps are :

* Run **installPackages.sh** to install the packages
* Optionally, run **startServer.sh** to start the server
* Optionally, look at the served out JSON at http://127.0.0.1:8005/static-dict
* Optionally, look at the swagger documentation at http://127.0.0.1:8005/docs

Having established that the software is still the same, run pytest :

* Run **run_unit_tests.sh** to run the pytest unit tests defined in test_demoFastapi.py
* Note that the server does not have to be running to do that test, a test client is used in test_demoFastapi.py
* Run **generate_test_coverage.sh** to generate a coverage report in the directory coverageReport
* Look at coverageReport/demoFastapi_py.html and see that the function that was not called is untested

To look at a git hook that will disallow commits if there is an issue
with **ruff** or **pytest** :

* Look at the hook script **preCommitHook.sh** and see that it only exits with 0 if ruff and pytest pass
* Install that script as a hook with **installHook.sh** which puts the link in place
* Break the code so that ruff fails

We can cause ruff to fail by adding an unnecessary line in **demoFastapi.py** after :
```
from fastapi import FastAPI
```
So that it reads :
```
from fastapi import FastAPI
import os
```
We can then see ruff fail with **uv run ruff check**

* Similarly, break the code so that pytest fails

We can cause pytest to fail by changing the line in **demoFastapi.py**
```
"firstName": "Niles"
```
So that it reads :
```
"firstName": "Miles"
```
We can then see pytest fail with **uv run pytest -v**

* Try to commit the code with
```
git commit -a -m "This commit will fail until issues are fixed"
```
and watch the commit get rejected.

* Optionally run cleanup.sh to clean up and removeHook.sh to remove the hook link


