print("hello world | Python");

"""
#int data types
a = 10;
b = 20;
print (a + b);

#flot data types
x = 5.60;
y = 6.69;
print (x + y);

#string data types
name = 'Sudesh Kumar';
print (name);

#list data types
a = [1,2,3,4,5,0,9];
print(a);
a.sort();
print (a);
a.reverse();
print(a);
"""

#array 
import array as arr;

#int array
numbers = arr.array('i',[1,2,3,4,5,6]);
print(numbers);

numbers = arr.array('f',[1,2,3,4,5.60,7.50]);
print(numbers);

import numpy as np;
numbers = np.array([1,2,5,3,4,6,7], dtype='float');
print(numbers);

int_numbers = np.array([1,2,3,4,5,6],dtype='int');
print(int_numbers);

print('print max element',numbers.max());
print('print max element',int_numbers.min());

