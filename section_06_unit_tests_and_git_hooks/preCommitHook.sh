#!/bin/bash

# Script that runs unit tests and ruff code tests.
# Can be used as a git hook. To do that it needs
# to be installed as a hook with :
#
# $ cd ../.git/hooks/
# $ ln -sf ../../section_06_unit_tests_and_git_hooks/preCommitHook.sh pre-commit
#
# Once this is installed as a pre commit hook, both
# unit tests and ruff code check have to pass for
# git to accept a commit. Hook scripts have to exit
# with 0 status for the requested action to go ahead.
# It's also possible to have pre-push hooks, I just like
# pre-commit hooks more.

# Make sure we're in the right directory.
if [ -d section_06_unit_tests_and_git_hooks ]
then
 cd section_06_unit_tests_and_git_hooks
fi

# Run unit tests. Exit with status if they fail.
# They fail if they have non-zero status.
echo Running unit tests...
uv run pytest -v
status="$?"
if [ "$status" -ne 0 ]
then
 echo Unit tests failed, exiting
 exit $status
fi

# Run ruff code checks - similar, exit if they fail.
echo
echo Running code checks...
uv run ruff check
status="$?"
if [ "$status" -ne 0 ]
then
 echo Code check failed, exiting
 exit $status
fi

# If we made it to here, we passed.
# We can exit with 0 status
# which means that the commit can go ahead.
echo
echo Passed unit tests and code check
exit 0

