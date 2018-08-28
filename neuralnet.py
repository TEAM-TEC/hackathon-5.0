import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os

seed = 1234
np.random.seed(seed)
tf.set_random_seed(seed)

dataset = pd.read_csv("test.csv")

X = dataset[dataset.columns[1:4]]
X = np.array(X,dtype='float32')

y = pd.get_dummies(dataset[dataset.columns[6]])
y = np.array(y,dtype='float32')       


#cleaning the data a bit and not allowing points greater than 12
ind_list=[]
for i in range(len(X)):
    curr = X[i]
    if(curr[0]>20 or curr[1]> 20 or curr[0]<-20 or curr[1]<-20 ):
        ind_list.append(i)
    
#creating new lists 
X = np.delete(X,ind_list,0)
y = np.delete(y,ind_list,0)

# Shuffle Data
indices = np.random.choice(len(X), len(X), replace=False)
X_values = X[indices]
y_values = y[indices]

# Creating a Train and a Test Dataset
test_size = 300
X_test = X_values[-test_size:]
X_train = X_values[:-test_size]
y_test = y_values[-test_size:]
y_train = y_values[:-test_size]

# Session
sess = tf.Session()

# Interval / Epochs
interval = 1000
epoch = 1000000

# Initialize placeholders
X_data = tf.placeholder(shape=[None, 3], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 3], dtype=tf.float32)

# Input neurons : 4
# Hidden neurons : 8
# Output neurons : 3
hidden_layer_nodes = 8

# Create variables for Neural Network layers
w1 = tf.Variable(tf.random_normal(shape=[3,hidden_layer_nodes])) # Inputs -> Hidden Layer
b1 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes]))   # First Bias
w2 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes,3])) # Hidden layer -> Outputs
b2 = tf.Variable(tf.random_normal(shape=[3]))   # Second Bias

# Operations
hidden_output = tf.nn.sigmoid(tf.add(tf.matmul(X_data, w1), b1))
final_output = tf.nn.softmax(tf.add(tf.matmul(hidden_output, w2), b2))

# Cost Function
#loss = tf.reduce_mean(-tf.reduce_sum(y_target * tf.log(final_output), axis=0))
loss = tf.keras.backend.binary_crossentropy(y_target, final_output)
loss = tf.reduce_mean(loss)
# Optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)

# Training
print('Training the model...')
for i in range(1, (epoch + 1)):
    sess.run(optimizer, feed_dict={X_data: X_train, y_target: y_train})
    if i % interval == 0:
        print('Epoch', i, '|', 'Loss:', sess.run(loss, feed_dict={X_data: X_train, y_target: y_train}))

# Prediction
print()
for i in range(len(X_test)):
    print('Actual:', y_test[i], 'Predicted:', np.rint(sess.run(final_output, feed_dict={X_data: [X_test[i]]})))


# lr = 0.001 epoch = 1000000 min_loss = 226#
# lr = 0.001 epoch = 1000000 tf.keras.backend.binary_crossentropy min_loss = very good#






    
