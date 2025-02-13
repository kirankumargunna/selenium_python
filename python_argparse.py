# The argparse module allows you to create user-friendly command-line interfaces.
# It helps you define arguments and options for a script and automatically generates help messages.

import argparse

# create an Argument Parser object
parser=argparse.ArgumentParser(description="A script to demonstrate argument parser in command line ")

parser.add_argument("--name",type=str,required=True,help="enter your name")
parser.add_argument("--age",type=int,required=True,help="enter your age")
parser.add_argument("--city",type=str,required=False,default='UNKNOWN',help="enter your name")

args=parser.parse_args()
print(type(args))
args=vars(args)
print(type(args))

for key,value in args.items():
    print(key," : ", value)


# python_argparse.py [-h] --name NAME --age AGE [--city CITY]

# PS D:\selenium_python> python python_argparse.py -h
# usage: python_argparse.py [-h] --name NAME --age AGE [--city CITY]
#
# A script to demonstrate argument parser in command line
#
# options:
#   -h, --help   show this help message and exit
#   --name NAME  enter your name
#   --age AGE    enter your age
#   --city CITY  enter your name
# PS D:\selenium_python>
