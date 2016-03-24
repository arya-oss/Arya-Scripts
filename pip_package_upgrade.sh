#!/bin/sh
# run script or enter command given below in terminal to
# upgrade all of the python package installed through pip
pip list | cut -f1 -d" " | pip install --upgrade
