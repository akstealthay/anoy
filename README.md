# Anoy

## Introduction

`Anoy` is a tagging tool built using [python-flask](http://flask.pocoo.org/) that enables you to tag documents with custom tags and export them. This is an ideal tool for a data team who wants to tag documents for training a data model.

## Table of contents

* [Installation](#installation)
* [Features](#features)
* [Issues](#issues)
* [Contributors](#contributors)
* [Mailing List](#mailing-list)
* [Creators](#creators)
* [Copyright and license](#copyright-and-license)

## Installation

The procedure of installing `Anoy` is pretty simple. Just follow the steps below.
```
$ git clone https://github.com/frictionle/anoy.git
```

Edit following variables in `app/config.py`

* `ANOY_HOME_FOLDER` : path of the directory where you want to store the application data and configuration settings.

Make `anoy` as your working directory and execute the script `start.sh`. This script will install all the dependencies and will start the server on `localhost:5000` as well.
```
$ cd anoy

$ ./start.sh
```

Hit the following URL from any browser of your choice
```
http://localhost:5000/
```

## Features

1. Tag text file

The list is very small :-( but together we can make it big. Check out how you can [contribute](#contributors).

## Issues

Have a bug or a feature request? You can find our existing and closed issues [here](https://github.com/frictionle/anoy/issues). If your problem or idea is not addressed yet, [please open a new issue](https://github.com/frictionle/anoy/issues/new).

## Contributors

Anyone with basic knowledge of [jQuery](https://jquery.com/) and [Python](https://www.python.org/) can contribute to `Anoy`.

Contributing to `Anoy` is simple. You can

1. Fix an existing bug. Browse through the complete list [here](https://github.com/frictionle/anoy/issues).
2. Have a feature idea? [share](https://github.com/frictionle/anoy/issues/new) it with us.

## Mailing List

This list is for development discussions like current issues and patch suggestions.

* Subscribe by sending an e-mail to: [frictionle-anoy+subscribe@googlegroups.com](mailto:frictionle-anoy+subscribe@googlegroups.com)
* To un-subscribe send an e-mail to: [frictionle-anoy+unsubscribe@googlegroups.com](mailto:frictionle-anoy+unsubscribe@googlegroups.com)

Visit this group at: <https://groups.google.com/forum/#!forum/frictionle-anoy>

## Creators

**Arpit Bhayani**

* <http://arpitbbhayani.github.io>

## Copyright and license
Code copyright 2015 Arpit Bhayani. Code released under [the MIT license](https://github.com/frictionle/anoy/blob/master/LICENSE).
