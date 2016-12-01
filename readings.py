import numpy

import loaddata


import sys

## Here's just a comment describing what this script does
def main():

 	filename='data/inflammation-01.csv'

	data = loaddata.load(filename)

	print(filename)

	print(data.mean(axis=1))



main()
