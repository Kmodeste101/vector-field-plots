#!/usr/bin/python3
#some practice stuff

import numpy as np


'''
a=11
if a==1:
    print(1)
elif a==2:
    print(2)
else:
    print('A lot')


#print('procedure to generate decimals of pi from the wallis formula:')
def wallis(n):
    pi=0.0
    for i in range(1,n):
        x=(4*(i**2))
        y=(x-1)
        z=(float(x)/float(y))
        if (i == 1):
            pi=z
        else:
            pi*=z
    pi*= 2
    return pi
w=wallis(10000) #change accordingly
#print('Value for pi is:',w)

#energy is E=mc^2

#print('Function returning a value, E=mc^2:')

def energy(mass):
    energy=mass*(3.0*10**8)**2
    return energy
mass=5000 #kg
#print('energy as a function of mass, %d kg is:'%(mass), energy(mass)) #kg, change mass accordingly
'''
#mutablable type in a keyword argument

def adding_to_dic(args={'a':1,'b':2}):
    for i in args.keys():
        args[i]+=1
    print(args)
#adding_dic()  modifies the keyword argument inside the function

#adding_to_dic  prints out the modified fucntion.
 
#fibonacci
print('finobacci sequence, nth term:')
print
def fibs(n):
    #U_o=0
    #U_1=1
    if n<0:
        print('Invalid n')
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        #U_2=U_o+U_1
        return fibs(n-1)+fibs(n-2)
        
print(fibs(6))
print


print('Quicksort algorithm as implemented by wikipedia:')
print

random_array=np.random.rand(10)
print('random_array')







