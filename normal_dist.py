# Normal Distribution AKA Gaussian probability
import math
from scipy.stats import norm

#Note:  z-score is the distance from the mean and it's standard deviation?  *clarify*

def normal_deviation(a, b):
    """
    What is the standard deviation of the data point distribution?
    I need clarification on where this '12' comes in.  Why 12?
    deviation is:  the square root of ((the high value, minus the low value squared) divided by 12)
    """
    deviation = math.sqrt((b-a)**2 / 12)
    print("The deviation of this normal distribution is : ", deviation)
    return deviation

def normal_mean(a, b):
    """
    What is b and a?
    The range at which the distribution falls.
    example: 
    the number of paintings sold in a day are 5 - 100.
    a = 5,  b = 100
    
    The mu, or standard mean (center point of data) of this normal distribution:
    u = (a + b) / 2
    """
    mean = (a + b) / 2
    print("The standard mean of this normal distribution is: ", mean)
    return mean

def x_bar_Normal_distribution(a, b, n):
    """
    THIS HAS NOT BEEN TESTED.
    The deviation of the Normal distribution of a sample of means of a normal distribution.
    deviation / sqrt(number of samples)
    """
    mean = normal_mean(a, b)
    deviation = normal_deviation(a, b)
    normal_x_bar_deviation = deviation / math.sqrt(n)
    print("The standard deviation of the sample of means from the normal distribution ( [n] samples ) is: ", normal_x_bar_deviation)
    return normal_x_bar_deviation



def range_probability_cdf(mean, devi, range_low, range_high):
    """
    The formula will not work on a continuous probability.  SciPi has a built in method to do this math for us.
    I wanted to do it myself, so I could learn the math, and I did learn the formula below pretty good, but
    the formula we need to calculate a continuous probability is much more complex.
    Time to use the hammer instead of my hand.

    norm.cdf(x, loc(mean), scale(deviation))

    Formula probability density function:
    the area under the curve for a given point p(x) is:
    1 / ( 2 * pi * (mean squared) * (mathmatical number e to the power of (our z score squared)))
    1/ 2 * pi *  m**2 * e**(z**2)  
   [[e = math.exp, pi = math.pi]]
    for the range, we would take the larger area,  minus the smaller area to get the difference, which is the area just between
    these two p(x)s.
    """
    # 1 / (2 * pi * deviation**2) = x
    # e ** -((range_num - mean)**2 / 2*deviation**2 = y
    # area = y/x

    large = norm.cdf(range_high, mean, devi)
    print("scipy large area =  ", large)
    small = norm.cdf(range_low, mean, devi)
    print("scipy small area = ", small)
    range_area = large - small
    message = f"The area in range {range_low} - {range_high} is {range_area}"
    return range_area
    
def mycdf(mean, devi, range_low, range_high):
    """
    If the ranges are above the mean, we must get the inverse area.
    so if it's one deviation above, or any positive deviation above, we want 1 - results.
    
    Formula probability density function:
    the area under the curve for a given point p(x) is:
    1 / ( 2 * pi * (mean squared) * (mathmatical number e to the power of (our z score squared)))
    1/ 2 * pi *  m**2 * e**(z**2)  
    [[e = math.exp, pi = math.pi]]
    for the range, we would take the larger area,  minus the smaller area to get the difference, which is the area just between
    these two p(x)s.
    """

    devi_square = float(devi**2)
    low_e_num = math.exp(-((float(range_low) - float(mean))**2 / (2*devi_square)))
    denom = float( math.sqrt(2 * math.pi * devi_square) )
    high_e_num = math.exp(-((float(range_high) - float(mean))**2 / (2*devi_square)))
    low_area = float(low_e_num / denom)
    high_area = float(high_e_num / denom)
    if range_low > mean:
        low_area = 1 - low_area
    if range_high > mean:
        high_area = 1 - high_area
    print("my high_area = ", high_area)
    print("my low_area = ", low_area)
    under_curve = high_area - low_area
    message = f"The area under the curve for range {range_low} - {range_high} = {under_curve}"
    return under_curve
        

def test1():
    # test against excel data:
    # excel formula 1 = [=NORM.DIST(8.5, 10, 1.5, 1) => .1587
    # excel formula 2 = [=NORM.DIST(11.5, 10, 1.5, 1) => .8414
     #  ex1 - ex2 = .6827
   #range_probability_withmeandevi(mean, devi, range_low, range_high):
   area = range_probability_cdf(10, 1.5, 8.5, 11.5)
   print(area)


def test2():
    """
    compare results for my density function and using scipy's
    empirical rule says that this range should be about 95%
    """
    area = range_probability_cdf(12, 1.3, 9.4, 14.6)
    area2 = mycdf(12, 1.3, 9.4, 14.6)
    print("scipy result:", area)
    print("my result:", area2)

def test3():
    """
    compare results for my density function and using scipy's
    empirical rule says that this range should be about 64%
    """
    scipy_area = range_probability_cdf(10, 1.5, 8.5, 11.5)
    my_area = mycdf(10, 1.5, 8.5, 11.5)
    print("scipy result:", scipy_area)
    print("my result:", my_area)

#test1() -- pass
#test2() -- fail
#test3() -- fail


