import os, os.path
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

#Getting list of images in images directory 
def getListOfImages():
    imgs = []
    path = os.getcwd() + "\images"
    print(path)
    valid_images = [".jpg",".jpeg",".png"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(f)
    return imgs

imgs = getListOfImages()
originalImagePath = ""
    
#Tkinter stuff
root = Tk()

root.title("My program")
root.geometry("800x800")

lb = Listbox(root, width = 200, selectmode = SINGLE)

for i in range(len(imgs)):
    lb.insert(i, imgs[i])
lb.grid(row = 0, columnspan = 6)



#functions that are called when a particular button is clicked
def clickedOriginal():
    img = Image.open(originalImagePath)
    img.thumbnail((400, 400))
    originalImg = ImageTk.PhotoImage(img)
    myLabel.config(image = originalImg)
    myLabel.image = originalImg


def clickedLeft():
    img = Image.open(originalImagePath)
    img.thumbnail((400, 400))
    img = np.asarray(img)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    numRows, numCols, colors = img.shape

    halfPoint = numCols//2

    imgLeft = Image.fromarray(img[:,0:halfPoint])
    
    leftImg = ImageTk.PhotoImage(imgLeft)
    myLabel.config(image = leftImg)
    myLabel.image = leftImg
    
def clickedRight():
    img = Image.open(originalImagePath)
    img.thumbnail((400,400))
    
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = np.asarray(img)
    
    numRows, numCols, colors = img.shape

    halfPoint = numCols//2
    imgRight = Image.fromarray(img[:, halfPoint:])
    
    rightImg = ImageTk.PhotoImage(imgRight)
    myLabel.config(image = rightImg)
    myLabel.image = rightImg


def invertImage():
    img = Image.open(originalImagePath)
    img.thumbnail((400, 400))
    img = np.asarray(img)
    
    numRows, numCols, colors = img.shape

    for row in range(0, numRows):
        for col in range(0, numCols):
            img[row][col][0] = 255 - img[row][col][0]
            img[row][col][1] = 255 - img[row][col][1]
            img[row][col][2] = 255 - img[row][col][2]
    invertedImg = Image.fromarray(img)
    invertedImg = ImageTk.PhotoImage(invertedImg)
    myLabel.config(image = invertedImg)
    myLabel.image = invertedImg


def removeRed():
    img = Image.open(originalImagePath)
    img.thumbnail((400, 400))
    img = np.asarray(img)
    
    numRows, numCols, colors = img.shape

    for row in range(0, numRows):
        for col in range(0, numCols):
            img[row][col][0] = 0 #Make the red pixel value 0 for all pixels 
           
    redImg = Image.fromarray(img)
    redImg = ImageTk.PhotoImage(redImg)
    myLabel.config(image = redImg)
    myLabel.image = redImg
    
def selectItem():
    global originalImagePath
    originalImagePath = "images\\" + lb.get(ANCHOR)
 

#Creating the buttons
buttonOriginal = Button(root,text = "See original image",command = clickedOriginal)
buttonOriginal.grid(row = 1, column = 1)

buttonLeft = Button(root,text = "See left half of image", command = clickedLeft)
buttonLeft.grid(row = 1, column = 2)

buttonRight = Button(root,text = "See right half of image",  command = clickedRight)
buttonRight.grid(row = 1, column = 3)

buttonInvert = Button(root,text = "See inverted version of image",  command = invertImage)
buttonInvert.grid(row = 1, column = 4)

buttonRemoveRed = Button(root,text = "Remove red colour from image",  command = removeRed)
buttonRemoveRed.grid(row = 1, column = 5)


btnSelect = Button(root, text='Select image', command = selectItem)
btnSelect.grid(row = 1, column = 0)

myLabel = Label(root)
myLabel.grid(row = 2, columnspan = 6)    

root.mainloop() #Main event loop

