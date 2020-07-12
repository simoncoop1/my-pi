import filecmp
import os

#check for a calculator value of pi(3.14159265) is worked out correctly, 
#the last digit of the calculator value is ignored since it contained a
# rounded value, which would require calculating pi to more digits than
# the calculator actually displays

test_res= os.system('python3 my-spigot.py 9 > my-spt-test.txt')


if(filecmp.cmp('my-spt-test-correct.txt', 'my-spt-test.txt')):
    print("Test: PASSED")
else:
    print("Test: FAILED")
