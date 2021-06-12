# git-squash #
A git command that lets you squash all commits in a feature branch into one
commit.

## Usage ##
`git-squash <upstream-branch>`

## Build Instructions ##
Setup a virtual env with:

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements-dev.txt
pip-sync requirements-dev.txt requirements.txt
```

Then run

```
python setup.py bdist_pex
```

to get a binary.
