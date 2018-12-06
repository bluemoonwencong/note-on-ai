import tensorflow as tf
a = tf.constant(5, name='input_a')
b = tf.constant(3, name='input_b')
c = a + b
d = a * b
e = c + d
sess = tf.Session()
ans = sess.run(e)
print(ans)
writer = tf.train.SummaryWriter('./my_graph', sess.graph)
tensorboard --logdir='my_graph'

