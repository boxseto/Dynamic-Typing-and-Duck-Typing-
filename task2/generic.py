# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : Seto Tsz Kin
# Student ID : 1155092585
# Email Addr : 1155092585@link.cuhk.edu.hk

def addition(a, b):
    return a + b

print('generic code')
print('Dynamic typing can let argunments of different types used in same function.\nMost obvious example is addtion of two integer and floats')
print()
print('trying to add two integers, 2 and 3')
print('2 + 3 = %d' % addition(2,3))
print()
print('trying to add two floats, 1.58 and 3.76')
print('1.58 + 3.76 = %f' % addition(1.58,3.76))
