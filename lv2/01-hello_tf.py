
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

# Example_1: Simple TensorFlow program
print ("\n ======== Hello World TensorFlow =================")

# Phase 1: assemble a graph
a = tf.constant(3)
b = tf.constant(4)
x = tf.add (a, b)


# Phase 2: use a session to execute operations in the graph
with tf.Session() as sess:
	print (sess.run(x))
# TODO_1: Create a summary writer, add the 'logs' to the event file.
#         Try TensorBoard.
	writer = tf.summary.FileWriter("./graphs",sess.graph)
writer.close()
# TODO_2: Name the ops

