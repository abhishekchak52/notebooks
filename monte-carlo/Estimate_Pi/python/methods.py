""" Defines functions for generate.py """
import sys
import numpy
import mpmath
# Constants
mpmath.dps = 15 # decimal precision of 15 digits
DATA_SIZE = 10**5
#sample_size = 10**5


def generate_random_points(SIZE):
    """ Genrates many many random points in a unit square. """
    points = numpy.random.uniform(mpmath.mpf('0'),mpmath.mpf('1'),(SIZE,2))
    return points

def check_inside_quadrant(point):
    """ Checks if a given point is inside the quadrant of a unit circle. """
    return point[0]**2+point[1]**2<1

def count_point_ratio(point_list,sample):
    """ Counts the ratio of the number of points inside the circle to the total number of points. """
    count = 0
    points_inside = 0
    for point in point_list:
        if check_inside_quadrant(point) == True:
            points_inside += 1
        count += 1
    pi =  4*mpmath.mpf(points_inside)/mpmath.mpf(count)
    out_to_file(pi,sample)

def out_to_file(pi,size):
    """ Places the calculated value of pi in a .txt file """
    NUM_DIGITS = int(numpy.log10(size))
    filepath = "./outputs/"
    filename = "pi_1e"+str(NUM_DIGITS)+'.txt'
    output = open(filepath+filename,'a')
    output.write(str(pi)+'\n')
    output.close()
