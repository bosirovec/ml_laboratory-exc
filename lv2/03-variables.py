import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf


#declare variables

#create variable a with scalar value
a = tf.Variable (2, name = "scalar" )

#create variable b as a vector
b = tf.Variable ([ 2 , 3 ], name = "vector" )

#create variable c as a 2x2 matrix
c = tf.Variable ([[ 0 , 1 ], [ 2 , 3 ]], name = "matrix" )

# create variable W as 784 x 10 tensor, filled with zeros
W = tf.Variable (tf.zeros([ 784 , 10 ]))

init = tf.global_variables_initializer()

with tf.Session () as sess:
	sess.run(init)
	print(c.eval())

K = tf.Variable(10)
K.assign(100)
with tf. Session() as sess:
	sess.run (K.initializer)
	print (K.eval()) 


K = tf.Variable(10)
assign_op = K.assign(100)
with tf. Session() as sess:
	sess.run (assign_op)
	print (K.eval())


# Example 2: TODO
# create a variable 'my_var' whose original value is 2
# assign 2 * 'my_var' to 'my_var' and run that assign op twice 

my_var = tf.Variable(2)
assign_op = my_var.assign(2*my_var)
with tf. Session() as sess:
	sess.run (my_var.initializer)
	sess.run (assign_op)
	sess.run (assign_op)

	print (my_var.eval())

