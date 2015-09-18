# Anoy [![Gitter](https://badges.gitter.im/gitterHQ/gitter.svg)](https://gitter.im/frictionle)

> The tool does not export for now. The task of export is in progress and for now you can pick any issue from the Issue section of the repository

## Introduction

`Anoy` is a tagging tool built using [python-flask](http://flask.pocoo.org/) that enables you to manually tag documents with custom tags and export them as XML documents. This is an ideal tool for a data team who wants to manually tag documents for training a data model.

## Example

Sample document
> Boggarts lavender robes, **Hermione Granger** Fantastic Beasts and Where to Find Them. Bee in your bonnet Hand of Glory elder wand, spectacles House Cup Bertie Bott’s Every Flavor Beans Impedimenta. Stunning spells tap-dancing **spider** Slytherin’s Heir mewing kittens Remus Lupin. Palominos scarlet train black robes, Metamorphimagus Niffler dead easy second bedroom. Padma and Parvati Sorting Hat Minister of Magic blue turban remember my last. Let us hit **Accio**.

For training a data model we want to tag few segments of above document with some tags. For example, we want to tag

* `Hermione Granger`  as `PERSON_NAME`
* `spider` as `ANIMAL`
* `Accio` as `SPELL`

You want tagged document to be like
>Boggarts lavender robes, `<PERSON_NAME>Hermione Granger</PERSON_NAME>` Fantastic Beasts and Where to Find Them. Bee in your bonnet Hand of Glory elder wand, spectacles House Cup Bertie Bott’s Every Flavor Beans Impedimenta. Stunning spells tap-dancing `<ANIMAL>spider</ANIMAL>` Slytherin’s Heir mewing kittens Remus Lupin. Palominos scarlet train black robes, Metamorphimagus Niffler dead easy second bedroom. Padma and Parvati Sorting Hat Minister of Magic blue turban remember my last. Let us hit `<SPELL>Accio</SPELL>`.

With **Anoy** you can do this with ease. You just need to

1. Define tags `PERSON_NAME` and `ANIMAL`
2. Select text `Hermione Granger` apply tag `PERSON_NAME`
3. Select text `spider` and apply tag `ANIMAL`.
4. Select text `Accio` and apply tag `SPELL`.
5. Export the document

## Table of contents

* [Installation](#installation)
* [Features](#features)
* [How to contribute](#how-to-contribute)
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

The list is very small :-( but together we can make it big. Check out how you can [contribute](https://github.com/frictionle/anoy/wiki/How-to-contribute).

## How to contribute

Anyone with basic knowledge of [jQuery](https://jquery.com/) and [Python](https://www.python.org/) can contribute to `Anoy`.

Contributing to `Anoy` is simple. You can

1. Fix an existing bug. Browse through the complete list [here](https://github.com/frictionle/anoy/issues).
2. Have a feature idea? [share](https://github.com/frictionle/anoy/issues/new) it with us.

There is a crisp documentation written on [How to contribute](https://github.com/frictionle/anoy/wiki/How-to-contribute); you can follow that and get started :smile:

## Issues

Have a bug or a feature request? You can find our existing and closed issues [here](https://github.com/frictionle/anoy/issues). If your problem or idea is not addressed yet, [please open a new issue](https://github.com/frictionle/anoy/issues/new).

## Contributors

This is our own "Hall Of Fame" and these are some of the most awesome people who made this project possible.

- [Arpit Bhayani](https://github.com/arpitbbhayani)

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
