#Custom L1 Distance Layer module
 #Import Dependencies
import tensorflow as tf
print(tf.__version__)
from tensorflow.keras.layers import Layer
#Make Distance Layer
class L1Dist(Layer):
    def __init__(self,**kwargs):
        super().__init__()

    def call(self,input_embedding,validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)