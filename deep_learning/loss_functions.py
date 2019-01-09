from utils import accuracy_score
from deep_learning.activation_functions import Sigmoid
import numpy as np

class Loss():
    def loss(self, y_true, y_pred):
        return NotImplementedError()

    def gradient(self, x, y, y_pred):
        raise NotImplementedError()

    def acc(self, y, y_pred):
        return 0


class SquareLoss(Loss):
    def __init__(self):
        pass

    def loss(self, y, y_pred):
        return 0.5*np.power((y-y_pred),2)

    def gradient(self, y, y_pred):
        return (y-y_pred)

class CrossEntropy(Loss):
    def __init__(self):
        pass

    def loss(self, y, p):
        #avoid division by zero
        p = np.clip(p, 1e-15, 1-1e-15)
        return -y*np.log(p) - (1-y)*np.log(1-p)

    def acc(self, y, p):
        return accuracy_score(np.argmax(y, axis=1), np.argmax(p, axis=1))

    def gradient(self, y, p):
        #avoid divide by zero
        p = np.clip(p, 1e-15, 1-1e-15)
        return -(y/p)+(1-y)/(1-p)

