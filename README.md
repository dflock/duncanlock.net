# Setting up the venv

This site is using https://docs.getpelican.com/[Pelican] & and python venv.

To setup or recreate the venv:

```console
$ rm -rf ~/venv/duncanlock.net-venv
$ python3 -m venv ~/venv/duncanlock.net-venv
$ source ~/venv/duncanlock.net-venv/bin/activate
$ pip --version
$ python --version
```

To install dependencies:

```console
$ python -m pip -r requirements-venv.txt
```

To run a debug build:

```console
$ rm -f ./cache/* && pelican --delete-output-directory --debug &> ~/tmp/pelican-debug-output.log
```
