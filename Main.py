import kohonen_colors as kc
import math
import random
import sys

from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("MainWindow.ui")[0]      # Load the UI

class Main(QtGui.QDialog, form_class):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.randomBtn.clicked.connect(self.randomColors)
        self.trainBtn.clicked.connect(self.trainNetwork)


        self.originalGV.setScene(QtGui.QGraphicsScene())
        self.colorsGV.setScene(QtGui.QGraphicsScene())

        #initial colors
        self.training_input = [
                [0,0,0],
                [255,255,255],
                [125,125,125],
                [255,0,0],
                [0,255,0],
                [0,0,255],
                [255,255,0],
                [255,0,255],
                [0,255,255],
                ]
        #put it in screen
        self.updateColors()


    def updateColors(self):
        size  = self.colorsGV.size()
        w     = size.width()
        h     = 20
        til   = len(self.training_input)

        size.setHeight(h * til)
        image = QtGui.QImage(w, h * til, QtGui.QImage.Format_RGB32)

        for color in range(til):
            for x in range(w):
                for y in range(h):
                    c   = self.training_input[color]
                    rgb = QtGui.QColor(c[0], c[1], c[2]).rgb()
                    image.setPixel(x, color*h + y, rgb)

        self.draw(self.colorsGV.scene(), image)

    def randomColors(self):
        qt = self.colors.value()
        self.training_input = []

        for i in range(qt):
            self.training_input.append([random.randint(0,255),
                                        random.randint(0,255),
                                        random.randint(0,255)])

        self.updateColors()


    def trainNetwork(self):
        refresh    = self.refresh.value()
        iterations = self.iterations.value()
        size       = self.imageSize.value()
        kc.aldohonen(size, iterations, self.training_input, refresh, self.callback)


    def callback(self, image, iteration):
        if (image):
            self.draw(self.originalGV.scene(), image)
        self.progress.setText(str(int((iteration+1)/self.iterations.value()*100))+"%")
        QtGui.QApplication.processEvents()



    def draw(self, scene, image):
        pixmap = QtGui.QPixmap(image.size())
        pixmap.convertFromImage(image)
        pixItem = QtGui.QGraphicsPixmapItem(pixmap)

        scene.clear()
        scene.addItem(pixItem)


app = QtGui.QApplication(sys.argv)
myWindow = Main(None)
myWindow.show()
app.exec_()
