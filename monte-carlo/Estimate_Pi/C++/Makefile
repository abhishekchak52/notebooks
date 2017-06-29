#
#
# Makefile for Monte Carlo Pi estimator
#
#	Abhishek Chakraborty
#
#

all: main

main: main.cpp method.h method.cpp
	g++ -o main main.cpp method.cpp method.h

plots:main.cpp method.h method.cpp pi_hist.py ../outputs/pi_1e6.txt
	python pi_hist.py
clean:
	rm -f a.out *.o core main

edit:
	atom main.cpp method.h method.cpp Makefile
