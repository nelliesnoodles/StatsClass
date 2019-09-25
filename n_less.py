# Instructions
# num is one less than the sum you wish to find
# reg is the decrement (not changed for any reason yet.  
# total is what these n + (n-1) until n reaches the minimum.
# min is the abs[]  difference between the sum and nums in the set
# max is the number of items in the ordered set.
# if the die has 20 sides, the max sum is 40, all combos above 39 should == 400 
# we need to limit combinations by max number on the sides. 
# for 6, the max would be six.
# for a 20 sided it would be 20
# i don't know how this will work in a set that is not consecutive 1 - x  numbers
# I am assuming it can not, maybe that's where our reg will come in.


def find_combo(num, total, reg, max, min):
    if num <= min:
        return total
    else:
        if num > max:
            total = total + max
        else:
            total = total + num
        num = num - reg
        return find_combo(num, total, reg, max, min)

# for possibles adding up to 7  ( 1-6 )
x = find_combo(6, 0, 1, 6, 0)
# for possibles adding up to 6 ( 1-6 )
y = find_combo(5, 0, 1, 6, 0)
b = find_combo(8, 0, 1, 6, 2)
print("sum combos <= 7 : ", x)
print("sum combos <= 6 : ", y)
print("sum combos <= 9 : ", b) 
z = find_combo(39, 0, 1, 20, 19) # for all becaues max sum is 40
a = find_combo(40, 0, 1, 20, 20) # max sum = 40
ab = find_combo(38, 0, 1, 20, 18)
print("sum combos <= 40 : ", z)
print("sum combos <= 41 : ", a)
c = find_combo(11, 0, 1, 6, 5)
print("sum combos <= 12 on six sided die = ", c)
print("sum combos <= 39 on 20 sided die = ", ab)
# max combos is (items in list)^2
# for a 6 sided die this is 36,  6 * 2 = 12, 

