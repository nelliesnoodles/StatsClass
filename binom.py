# variables=>
# pk = probablity of event happening
# pki = probability of event not happening(inverse)
# n = number of events we wish to account for ( How many times is event going to happen?)
# t = total number of events outcomes ( coin toss has 2 possible event outcomes)
# We'll make this in a separate function under the hood => (total possible events/outcomes) = tp
import math



class BinomDist(object):
    def __init__(self, total_outcomes, number_of_events, probability_of, inverse_probability_of):
        self.t = total_outcomes #how many times we flip the coin
        self.n = number_of_events
        self.pk = probability_of 
        self.pki = inverse_probability_of 
        self.tk = None
        self.comb = None
    
    def test_init(self):
        self.find_tk()
        self.find_factorial_comb()
        attributes = [self.t, self.n, self.pk, self.pki, self.tk, self.comb]
        names = ['total_outcomes=t', 'number_of_events=n', 'probability_of=pk', 'inverse_probability_of=pki', 'total_possible=tk', 'combitoral=comb']
        i = 0
        for item in attributes:
            name = names[i]
            try: 
                float(item)
            except:
                print("ERROR with: ", name)
                print("Was unable to convert attribute to a float.")
            i += 1
                
        print("Initiate values test complete")

    def find_tk(self):
      
        tk = self.t ** self.n
        self.tk = tk
        print("BinomDist tk set to: ", self.tk)

    def find_factorial_comb(self):
        t_fact = math.factorial(self.t)
        n_fact = math.factorial(self.n)
        t = self.t
        n = self.n
        comb = t_fact / (n_fact * math.factorial(t-n))
        print("BinomDist comb set to: ", comb)
        self.comb = comb


    def find_binomial_distribution(self):
        self.find_tk()
        self.find_factorial_comb()
        # the hairy bits
        f_of_x = self.comb * (self.pk ** self.n) * (self.pki**(self.t-self.n))
        print("the function of x = ", f_of_x)


       

def test1():
    # attributes: BinomDist(total outcomes, event seeked, probability of event, inverse of probablility of event)
    new = BinomDist(5, 2, 0.5, 0.5)
    new.test_init()

def test2():
    new = BinomDist(5, 2, 0.5, 0.5)
    #new.test_init()
    answer = new.find_binomial_distribution()
    return answer

def test3():
    """ Test against the Excel formula """
    # to-do, make function to write results into excel
    new = BinomDist(10, 5, .1, .9)
    mine = new.find_binomial_distribution()

test3()





