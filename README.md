# face

> convert face images to face vectors using dlib

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple Python program that recognizes faces gives face encodings and bounding box coordinates as output

## Installation

pip install this repo.
(Note: Incompatible with Python 2.x)

```sh
pip3 install git+https://github.com/zahash/face.git
```

(or)

```sh
pip install git+https://github.com/zahash/face.git
```

## Usage example

To get help with commandline arguments

```sh
python3 -m face --help
```

Using Command-line Arguments

```sh
python3 -m face "some/folder/asdf.png"
```

Importing the package

```Python
from face import recognize
faces = recognize("some/folder/asdf.png")
```

## Development setup

Clone this repo and install packages listed in requirements.txt

```sh
pip3 install -r requirements.txt
```

## Meta

M. Zahash – zahash.z@gmail.com

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/zahash/](https://github.com/zahash/)

## Contributing

1. Fork it (<https://github.com/zahash/face/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
