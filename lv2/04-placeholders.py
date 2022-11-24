import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

# example1
# create a placeholder of type float 32-bit, shape is a vector of 3 elements
a = tf.placeholder (tf.float32, shape =[ 3 ])
# create a constant of type float 32-bit, shape is a vector of 3 elements
b = tf.constant ([ 5 , 5 , 5 ], tf.float32)
# use the placeholder as you would a constant or a variable
c = a + b # Short for tf.add(a, b)

with tf.Session () as sess:
    #print ( sess.run(c)) # will fail because there is no value in placeholder
    print ( sess.run(c, feed_dict={a: [1.0, 2.0, 3.0]})) # will succeed


# example2
# create Operations, Tensors, etc (using the default graph)
a = tf.add(2, 5)
b = tf.multiply(a, 3)
# start up a `Session` using the default graph
with tf.Session() as sess:
	# define a dictionary that says to replace the value of `a` with 15
	replace_dict = {a: 15} 
	# Run the session, passing in `replace_dict` as the value to `feed_dict`
	print(sess.run(b, feed_dict=replace_dict)) # returns 45


# Example 3: TODO
# create two placeholders 'my_placeholder_a' and 'my_placeholder-b, both type float 32-bit as shape of 4 elements.
# multiply each element with corresponding element of the other (1 with 1, 2 with 2...)
# feed a dictionary of values to the placeholder
my_placeholder_a = tf.placeholder(tf.float32, shape = [4])
my_placeholder_b = tf.placeholder(tf.float32, shape = [4])
c = tf.multiply(my_placeholder_a,my_placeholder_b)

with tf.Session() as sess:
	replace_dict = {my_placeholder_a : [1,2,3,4], my_placeholder_b :[1,2,3,4]}
	print(sess.run(c, feed_dict = replace_dict))
