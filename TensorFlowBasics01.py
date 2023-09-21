import time as tm
start = tm.time()

import tensorflow as tf


#tensors are multidimentional arrays
#here are some ways to create simple vars in tensorflow library

#integer
integer_value = tf.constant(69)
print(integer_value)

#float
floating_value = tf.constant(3.7)
print(floating_value)

#string

string = tf.constant("w")
print(string)

#array(1d tensor)
array = tf.constant([1,2,3,4])
print(array)

#multidimentional array(2d tensor or multi-dimential array)
arrat_2d = tf.constant([[1,2,3],[6,7,6]])
print(arrat_2d)

# creating a ones matrix(all elements in the matrix are 1)
# make sure the arguments passed are in tuple form
ones_matrix = tf.ones((2,3))
print(ones_matrix)

# creating a zero matrix(all elements in the matrix are 0)
# make sure the arguments passed are in tuple form
ones_matrix = tf.zeros((2,3))
print(ones_matrix)

end = tm.time()
#computing execution time of the code
print(end-start)

