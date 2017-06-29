#
#
#
# Makefile for monte-carlo
#
# Abhishek Chakraborty
#
#
#

all: generate

generate: generate.py methods.py
	python generate.py

edit: generate.py methods.py
	atom *.py Makefile
clean:
	rm *.pyc *.o
