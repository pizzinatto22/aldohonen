import numpy as np
import pylab
import random

from PIL.ImageQt import ImageQt
from pybrain.structure.modules import KohonenMap
from PyQt4 import QtGui
from scipy import misc



def som2image(som, size):
    data = np.zeros( (size,size,3), dtype=np.uint8 )
    x = 0
    y = 0
    for i in som.neurons:
        for j in i:
            data[x][y] = j

            y += 1
            if (y >= size):
                y = 0
                x += 1

    return ImageQt(misc.toimage(data))

def aldohonen(size, iterations, training_input, refresh_rate, callback):
    som = KohonenMap(3, size)

    #just changing initial neurons weight from 0~1 to 0~255
    for i in som.neurons:
        for j in i:
            for k in range(len(j)):
                j[k] *= 255

    training_size = len(training_input) - 1

    for i in range(iterations):
        # one forward and one backward (training) pass
        som.activate(training_input[random.randint(0,training_size)])
        som.backward()

        #just draw som in our Qt View
        if (i % refresh_rate == 0):
            image = som2image(som, size)
            callback(image, i)
        else:
            callback(None, i)

    callback(som2image(som, size), iterations - 1)
