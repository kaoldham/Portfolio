'''
##############################################################################
Prompt:
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1",
"42", and other "good" numbers have been lording it over the poor minions who
are stuck with more boring IDs. To quell the unrest, Commander Lambda has
tasked you with reassigning everyone new, random IDs based on her Completely
Foolproof Scheme. 

She's concatenated the prime numbers in a single long string:
"2357111317192329...". Now every minion must draw a number from a hat. That
number is the starting index in that string of primes, and the minion's new ID
number will be the next five digits in the string. So if a minion draws "3",
their ID number will be "71113". 

Help the Commander assign these IDs by writing a function answer(n) which takes
in the starting index n of Lambda's string of all primes, and returns the next
five digits in the string. Commander Lambda has a lot of minions, so the value
of n will always be between 0 and 10000.

Test cases
==========

Inputs:
    (int) n = 0
Output:
    (string) "23571"

Inputs:
    (int) n = 3
Output:
    (string) "71113"

Constraints
===========
Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd,
pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
'''
def re_id(n):
    # Generate a list of prime numbers up to 100,000, which is more than
    # sufficiently long to generate new IDs for values of n up to 10,000.
    str_prime = prime_list(100000)

    # return characters at indeces [n, n+5)
    return str_prime[n:n+5]

def prime_list(m):
    # return an empty string if requesting list of primes <= 1.
    if m<=1: primes=""
    elif m==2: primes="2"
    else:
        primes = "2"
        # generate list of all odd numbers up to next potential prime
        # just odds because evens will not be prime.
        s=list(range(3,m+1,2))

        # find square root and half of potential prime to limit factors to test
        # i.e. if nothing below the sqrt is a factor, nothing above the sqrt
        # will be a factor either
        mroot = m ** 0.5

        # initial conditions for cycling through s
        i=0
        p=3

        # cycle through range, removing non-primes and their multiples by
        # setting the values at those indeces = 0 (i.e. Sieve of Eratosthenes
        # logic)
        while p <= mroot:
            if s[i]:
                j=(p*p-3)//2
                s[j]=0
                while j<len(s):
                    s[j]=0
                    j+=p
            i=i+1
            p=2*i+3
        # append all non-zero elements in s
        for y in s:
        	if y:
        		primes = primes+str(y)

    return primes
# Ask user for the starting index to use (aka a value for n to use in the re_id
# function)
starting_index = int(input("Please enter an integer between 0 to 10000, inclusive: "))

# print the ID generated using the starting index the user provided
print("\n######################################")
print("Your new ID is "+ re_id(starting_index)+".")
print("######################################\n")