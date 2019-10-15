# Binomial mean, deviation
import math
import sys


# reference= https://www.khanacademy.org/math/ap-statistics/random-variables-ap/binomial-mean-standard-deviation/v/expected-value-of-binomial-variable
# Binomail random variable X, is understood as:
# 1) A sample set is finite
# 2) The success and fail probabilities are constant, they do not change
# 3) They probabilities are independant of one another.
def return_ints(n, p):
    try:
        n = float(n)
        p = float(p)
        return n, p
    except:
        print(" The numbers provided could not be converted into floats.  exiting...")
        sys.exit()

def binomVariance(n, p):
    """
    The variance is the squared distance from the mean. 
    See reference, I don't fully understand yet.
    This involves Burnoulli variables X and Y
    """
    variance_of_Y = p * (1- p)
    variance_of_X = n * variance_of_Y 
    print("variance of X = ", variance_of_X)
    return variance_of_X


def expected_value_of_outcome(n, p):
    """
    expected value is number of trials(n) multiplied by Probablility of outcome(p)
    In binomial distributions this is also the mean.
    There are only two outcomes, and they are assumed to 
    be independant of one another.  
    If number of trials is 500, and the probablitliy of finding a certain outcome is .02,
    500 * 0.02 = 10
    """
    expected = n * p
    print("expected value / mean = ", expected)
    return expected

def BinomDeviation(n, p):
    """
    The standard deviation of a binomial distribution is determined by the formula:
    Square root of ( number of trials(n) * probablility of outcome (p) * inverse of probablity(1 - p))
    This should also be equal to the square root of the variance of X
    Again, there are only two possible outcomes, and they are independant and exclusive.
    """
    deviation = math.sqrt(n * p * (1-p))
    variance = binomVariance(n, p)
    secondary = math.sqrt(variance)
    print("(secondary) deviation = ", secondary)
    print("secondary and primary formulas should have the same result.")
    print("(primary)  The binom deviation is : ", deviation)
    return deviation

def get_binoms():
    n = input("Number of trials = ")
    p = input("Probablity of outcome x = ")
    n, p = return_ints(n, p)
    expected = expected_value_of_outcome(n, p)
    deviation = BinomDeviation(n, p)


get_binoms()
