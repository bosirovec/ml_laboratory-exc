import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

# Example_1: Create constants of scalar or tensor values
print ("\n##########################################")
print ("########## Constants: Example 1 ##########")
print ("##########################################")

a = tf.constant([2, 2], name='a')
b = tf.constant([[0, 1], [2, 3]], name='b')
with tf.Session() as sess:
    print(sess.run(a))
    print(sess.run(b))


# Example_2: Create tensors whose elements are of a specific value
print ("\n##########################################")
print ("########## Constants: Example 2 ##########")
print ("##########################################")

#creates a tensor of shape, and all elements will be zeros (when ran in session)
x = tf.zeros([2, 3], tf.int32) 
y = tf.zeros_like(x, optimize=True)

print('x: ', x)
print('y: ', y)

with tf.Session() as sess:
    y = sess.run(y)
    print(y)

# TODO: Create two new tensors using ones_like and fill. Use x for ones_like and [2, 3] for fill.
tensor1 = tf.ones_like(x)
tensor2 = tf.fill([2,3],2)

# Example_3: Create constants that are sequences
print ("\n##########################################")
print ("########## Constants: Example 3 ##########")
print ("##########################################")


with tf.Session() as sess:
    print(sess.run(tf.linspace(9.0, 13.0, 5)))
    print(sess.run(tf.range(5)))

# TODO: Try creating random constants using e.g. random normal, random_shuffle
const1 = tf.random_normal([3,3])
const2 = tf.random_shuffle(10)

# Example_4: Example math operations
print ("\n##########################################")
print ("############ MathOps: Example 4 ##########")
print ("##########################################")

a = tf.constant([3, 6])
b = tf.constant([2, 2])

with tf.Session() as sess:
    print (sess.run(tf.add(a, b)))  
    print (sess.run(tf.add_n([a, b, b])))

    print (sess.run(tf.multiply(a,b)))
    print (sess.run(tf.div(a,b)))
    print (sess.run(tf.mod(a,b)))
    a = tf.reshape(a,[2,1])
    b = tf.reshape(b,[1,2])
    print (sess.run(tf.matmul(a,b)))

''' TODO: try following ops and discuss results
 multiply(x,y) - element-wise multiplication
 matmul(x,y) - Multiplies matrix a by matrix b, producing a * b.
 div(x,y) - Divides x / y elementwise
 mod(x,y) - Returns element-wise remainder of division.
'''
    