# StatsClass
A gathering place for all my stat's class python code.

Many math formulas are easy to use from different popular python libraries,
but for this repo, I was learning the formulas for my class, and what better way
to learn them then to figure out how to code them?
Why not.

## Standard_dev.py
Use these methods to retrieve mean, standard deviations, and z-score with your data.
## binom.py
A class with methods to find the binomial distribution  
I learned a ton from the Khan Academy courses on statistics while researching to make this code.  
Highly recommended learning resource. 
The values for class BinomDist() init:
 * total_outcome
 * number_of_events
 * probability_of
 * inverse_probability_of
 
## binom_dist.py
Comments and a link to the Khan Academy video are in the file to explain the binomial Deviation and binomial Variance.  

This runs in your command prompt and asks for values then returns the mathy bits back in print() statements.

## n_less.py
This code was created when I spotted a pattern when trying to find a solution to one of my statistic class problems.  
Once again, there are simpler ways to use math libraries to obtain these results, and I was just trying to learn by coding.  
I don't fully remember the statistics question this is based off from, but it involved finding all results of rolling two six sided dice
and when their sums would be less than 7.   
This method uses recursion, so it has limits for the combinations and sums it can find before overflowing the stack.

## normal_dist.py
Another learning tool, these methods fail to compete with scipy's superior maths.
I didn't get to the point I fully understood what was happening with my errors, or why my results were close, but still wrong. I left it in the repo, because.... why not.


## toExel.py
The class contained in this file uses xlxswriter import to get data from the command line user input and write it to an excel file.  
It is not practicle or useful particularly because it's easier just to enter the data yourself.  It was a learning experiment, and I found it useful in the process of seeing how data could be moved around to different programs.











