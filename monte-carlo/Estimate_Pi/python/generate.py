""" Generates values of pi using Monte-Carlo methods and stores the output in a .txt file. """
from methods import *

if __name__ == "__main__":
    if len(sys.argv) == 2:
        sample_size = 10**int(sys.argv[1])
        for i in range(DATA_SIZE):
            count_point_ratio(generate_random_points(sample_size),sample_size)
    else:
        print "Usage: python generate.py SAMPLE_SIZE"
