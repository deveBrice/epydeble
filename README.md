# epydeble

epydeble is a project which goal is to display nearby bluetooth devices on a web page.

## requirements

   - python > 3.6
   - libbluetooth-dev (linux)
   - modules in requirements.txt

## how to

## Installation
- py -m pip install -r requirements.txt
  If issues with pyblues:
- Install visual studio code 2017 and choose visual build tools 2017
- clone this repository: https://github.com/pybluez/pybluez
- go to the root of folder pybluez with the terminale
- do the command py -m pip install setup.py

  no issues with pybluez
  do the command py setup.py install
  py -m pip scan.py

## Run server
- show this two lignes in app.py to the end of file
if __name__ == "__main__":
  app.run('127.0.0.1');

- run command py -m pip app.py 

The code currently provides two simple scripts:

	- `scan.py`: scan devices and store them in a json file with their ids, names, and RSSI.
	- `app.py`: simple Flask app

An devices.json file is provided as an example.
The bluetooth code in `blscan` uses PyBluez library.