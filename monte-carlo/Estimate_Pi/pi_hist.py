###########################################################
# Abhishek Chakraborty 15-9-2015		              	  #
#						                             	  #
# This program calculates the mean and standard deviation #
# of the dataset specified in oscillations.txt         	  #
# Kindly ensure that oscillations.txt is in the same      #
# directory as the program			                   	  #
#							                              #
############### Analyzing ramdom errors ###################
from matplotlib import pyplot as plt
import sys



########### Function Definitions ##########################

# Defining the function to calculate the mean\
def avg(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum/float(len(numbers))

# Defining the function to calculate the standard deviation
def std_dev(scores):
    average = avg(scores)
    variance = 0
    for score in scores:
        variance += (average - score)**2
    variance /= float(len(scores))
    return variance**0.5


# Prompting correct usage
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print "Correct usage: python pi_hist.py filepath num_bins\n"
    else:
        # A bit of file I/O
        osc = open(str(sys.argv[1]),'r')
        s = osc.readlines()
        ########### Getting a usable dataset ######################
        # The data is read as strings and needs to
        # converted to floats before any math
        data = []
        for number in s:
            number = float(number)
            data.append(number)
        ########### Printing everything ###########################
        print avg(data)
        print std_dev(data)
        n,bins,ignore = plt.hist(data,int(sys.argv[2]),normed=True)
        plt.show()
