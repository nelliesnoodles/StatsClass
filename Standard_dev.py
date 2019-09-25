###   Standard deviations (population and sample)
###   Z-score

import math
nums = [82, 77, 68, 42, 79, 91, 55, 68, 75, 83]
def standard_deviation(alist, to_print=True):
    # formual to get the standard deviation of a population
    if to_print:
        print("*   mean and standard deviation of a population    *")
    total = 0
    population_size = len(nums)
    
    for item in alist:
        total = total + item
    mean = total/population_size
    if to_print:
        print(f"MEAN = {mean}")
    total = 0
    for item in alist:
        # Here's where I use absolute value to simplify the formula
        x = abs(mean - item) 
        total = total + x

    deviation = total/len(alist)
    if to_print:
        print(f"Standard Deviation (Population) = {deviation}")
    #  The mean can be useful for my class, but feel free to eliminate it from the return
    if to_print:
        print("*    End method standard_deviation()      *\n")
    return deviation, mean


def standard_deviation_sample(alist):
    # Get the standard deviation of a sample
    # this is where all the squared business comes in.
    print("*     standard_deviation() of a sample     *")
    total = 0
    sample_size = len(nums)
    
    for item in alist:
        total = total + item
    mean = total/sample_size
    print(f"MEAN = {mean}")
    total = 0
    for item in alist:
        x = (mean - item) ** 2
        total = total + x
    
    n = len(alist)
    deviation = total/(n - 1)
    sample_deviation = math.sqrt(deviation)
    print(f"Standard Sample Deviation = {sample_deviation}")
    print("*      END standard_deviation_sample()     *\n")
    return sample_deviation


def z_score(value, alist=nums):
    #standard_dev, mean = standard_deviation(nums)
    # formula:(value -mean_of_set_of_alist) / deviation
    
    """
    Since I have my standard_deviation() formula returning the mean of our list,
    we can use that to get the mean and deviation.  
    If you want to change this data set (nums) you can copy paste your data in to a new list,
    and pass that in as alist.  z_score(value, alist=yourlist)
    *The nums list is to demonstrate these methods.
    to_print = False is keeping the print statements from filling this part with the print data
    from the standard_deviation method. Change it to to_print=True to have that data printed with z-score
    """
    print("\n*get z-score of a value from a data set z-score() *")
    
    
    deviation, mean = standard_deviation(alist, to_print=False)
    z_score = (value - mean) / deviation
    print(f"z-score = ", z_score) # note the variable z_score uses underscore, and z-score uses dash. 
    print("*    END z-score()     *\n")


def test():
    #  see the methods in action 
    standard_deviation(nums)
    standard_deviation_sample(nums)
    # for z-score put in a value that is relational to the list of numbers.
    z_score(32.5)

test()