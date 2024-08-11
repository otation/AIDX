import tensorflow as tf
import numpy as np

x = np.ones(6).reshape(1, 2, 1, 3)
y = np.ones(6).reshape(2, 1, 3, 1)
tf.add(x, y).shape.as_list()
