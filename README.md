# softwareTalk_FastAPI

Slides, example code for a talk on FastAPI.

## General structure

Slides are in HTML. To run the code (optional) it is assumed that the Python
package manager uv is installed. For the speed comparison
with Rust, the Rust compiler needs to be installed. If you want to build
the sqlite databases yourself, or look at the databases,
then the sqlite3 utility needs to be installed
(although you should not have to do that).

Standard methods for installing these are available for common architectures
with a simple internet search. A reasonably recent version of
Python is required.

Within sections, there are scripts to use uv to install packages if appropriate,
and scripts to clean up the virtual environments that uv creates (and/or
any other files generated during runtime).

The first slide is index.html at the top level. Most of the documentation
is covered in the slides, hence this README is pretty brief.

Basically, start with index.html.

