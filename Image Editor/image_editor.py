import PIL.Image 
import tkinter as Tk
from tkinter import *
import PIL.ImageTk
import PIL.ImageEnhance as pi
from tkinter import filedialog
import os
import cv2
import random
import ttk 
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyautogui
import keyboard
import mouse

root = Tk()
root.state('zoomed')

def confuse():
    global main,im,shown_image
    if int(main.shape[1])>1400 or int(main.shape[0])>800:
        width = 700
        height = 1400
        n_img  = PIL.Image.open("1.jpg")
        n_img.thumbnail((height,width))
            
        shown_image = PIL.ImageTk.PhotoImage(n_img)
        canvas_image.configure(image=shown_image)
        canvas_image.image = shown_image

    elif int(main.shape[1])<200 or int(main.shape[0])<200:
        width = 700
        height = 1400
        n_img  = PIL.Image.open("1.jpg")
        n_img.thumbnail((height,width))
            
        shown_image = PIL.ImageTk.PhotoImage(n_img)
        canvas_image.configure(image=shown_image)
        canvas_image.image = shown_image
    else:
        image = PIL.Image.open("1.jpg")
        shown_image = PIL.ImageTk.PhotoImage(image)
        canvas_image.configure(image=shown_image)
        canvas_image.image = shown_image

def ShowImage():
    global shown_image,im,main
    im = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image",filetypes=[("JPG files",".jpg"),("PNG files",".png"),("all files",".*")])
    main = cv2.imread(im)
    cv2.imwrite("1.jpg",main)

    confuse()

def SaveImage():
    global shown_image,im,main
    files = [('All files',".*"),('PNG file',".png"),('JPG file',".jpg")]
    sav = filedialog.asksaveasfile(mode="w",filetypes = files,defaultextension=files)
    
    save1  = PIL.Image.open("1.jpg")
    save1.save(sav,'JPEG')

def ShowImage_s(val):
    global shown_image,im,main
    im = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image",filetypes=[("JPG files",".jpg"),("PNG files",".png"),("all files",".*")])
    main = cv2.imread(im)
    cv2.imwrite("1.jpg",main)

    confuse()

def SaveImage_s(val):
    global shown_image,im,main
    files = [('All files',".*"),('PNG file',".png"),('JPG file',".jpg")]
    sav = filedialog.asksaveasfile(mode="w",filetypes = files,defaultextension=files)
    
    save1  = PIL.Image.open("1.jpg")
    save1.save(sav,'JPEG')
i=1
def Brightness_plus():
    global shown_image,im,i
    i +=0.2  
    img1 = PIL.Image.open("1.jpg")
    img_b = PIL.ImageEnhance.Brightness(img1)
    img_b = img_b.enhance(i).save("1.jpg")

    confuse()
    i=1
j=1   
def Brightness_negative():
    global shown_image,im,i,j
    i -=0.1 
    img1 = PIL.Image.open("1.jpg")
    img_b = PIL.ImageEnhance.Brightness(img1)
    img_b = img_b.enhance(j).save("1.jpg")

    confuse()
    i=1
def Color_plus():
    global shown_image,im,i
    i += 0.2
    img1 = PIL.Image.open("1.jpg")
    img_b = PIL.ImageEnhance.Color(img1)
    img_b = img_b.enhance(i).save("1.jpg")

    confuse()
    i=1
def Color_negative():
    global shown_image,im,i
    i -= 0.2
    img1 = PIL.Image.open("1.jpg")
    img_b = PIL.ImageEnhance.Color(img1)
    img_b = img_b.enhance(i).save("1.jpg")

    confuse()
    i=1
def Sharpness():
    global shown_image,im,i
    i +=1
    img1 = PIL.Image.open("1.jpg")
    img_s = PIL.ImageEnhance.Sharpness(img1)
    img_s = img_s.enhance(i).save("1.jpg")

    confuse()
    i=1
def Change_BW():
    global shown_image,im,i
    img1 = cv2.imread("1.jpg")
    B_W = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("1.jpg",B_W)

    confuse()

def Change_RGB_BGR():
    global shown_image,im,i
    img1 = cv2.imread("1.jpg")
   
    negative = 1 - img1
    cv2.imwrite("1.jpg",negative)

    confuse()

def Change_BGR_RGB():
    global shown_image,im,i
    img1 = cv2.imread("1.jpg")
    RGB = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
  
    cv2.imwrite("1.jpg",RGB)

    confuse()
def Crop_s(val):
    global shown_image,im,i
    img1 = cv2.imread("1.jpg")
    if int(img1.shape[1])>1400:
        if int(img1.shape[0])>800:
            width = int(main.shape[1]/3)
            height = int(main.shape[0]/3)
            final = cv2.resize(img1,(width,height),interpolation=cv2.INTER_AREA)
            cr = cv2.selectROI(final,False,False)
            crop= final[cr[1]:cr[1]+cr[3],cr[0]:cr[0]+cr[2]]
            cv2.imwrite("1.jpg",crop)

    else:
        cr = cv2.selectROI(img1,False,False)
        crop= img1[cr[1]:cr[1]+cr[3],cr[0]:cr[0]+cr[2]]
        cv2.imwrite("1.jpg",crop)

    confuse()
def Crop():
    global shown_image,im,i
    img1 = cv2.imread("1.jpg")
    if int(img1.shape[1])>1400:
        if int(img1.shape[0])>800:
            width = int(main.shape[1]/3)
            height = int(main.shape[0]/3)
            
            final = cv2.resize(img1,(width,height),interpolation=cv2.INTER_AREA)
            cr = cv2.selectROI(final,False,False)
            crop= final[cr[1]:cr[1]+cr[3],cr[0]:cr[0]+cr[2]]
            cv2.imwrite("1.jpg",crop)
            
    else:
        cr = cv2.selectROI(img1,False,False)
        try:
            crop= img1[cr[1]:cr[1]+cr[3],cr[0]:cr[0]+cr[2]]
            cv2.imwrite("1.jpg",crop)
        except:
            pass
    confuse()

def Blur():
    global shown_image,im,i
    i+=1
    img1 = cv2.imread("1.jpg")
    blur_img = cv2.blur(img1,(i,i))
    cv2.imwrite("1.jpg",blur_img)

    confuse()
    i=1
def LineArt():
    global im,i,show_image
    img1 = cv2.imread("1.jpg")
    Line = cv2.Canny(img1,125,175)
    cv2.imwrite("1.jpg",Line)

    confuse()

def Flip():
    global im,i,shown_image
    img1 = cv2.imread("1.jpg")
    flip = cv2.flip(img1,-1)
    cv2.imwrite("1.jpg",flip)

    confuse()

def ShowHistogram():
    img1 = cv2.imread("1.jpg")
    plt.figure()
    plt.title("1.jpg Histogram")
    plt.xlabel('Bins')
    plt.ylabel('% 0f Pixels')
    colors = ('b','g','r')
    for i,col in enumerate(colors):
        hist = cv2.calcHist([img1],[i],None,[256],[0,256])
        plt.plot(hist,color=col)
        plt.xlim([0,256])
    plt.show()

def ShowHistogram_s(val):
    img1 = cv2.imread("1.jpg")
    plt.figure()
    plt.title("1.jpg Histogram")
    plt.xlabel('Bins')
    plt.ylabel('% 0f Pixels')
    colors = ('b','g','r')
    for i,col in enumerate(colors):
        hist = cv2.calcHist([img1],[i],None,[256],[0,256])
        plt.plot(hist,color=col)
        plt.xlim([0,256])
    plt.show()
        
def Original():
    global im,i,shown_image
    img1 = cv2.imread(im)
    cv2.imwrite("1.jpg",img1)

    confuse()
def Original_s(val):
    global im,i,shown_image
    img1 = cv2.imread(im)
    cv2.imwrite("1.jpg",img1)

    confuse()
def rotate():
    global shown_image,im,value
    new = Tk()
    State = Scale(new,from_=0,to_=90,orient=HORIZONTAL)
    State.pack()

    def rotation():
        img1 = cv2.imread("1.jpg")
        c = State.get()
        center = tuple(np.array(img1.shape[1::-1])/2)
        rotated = cv2.getRotationMatrix2D(center,c,1.0)
        result = cv2.warpAffine(img1,rotated,img1.shape[1::-1],flags = cv2.INTER_LINEAR)
        cv2.imwrite("1.jpg",result)

        confuse()
        
    btn = Button(new,text="ok",command=rotation)
    btn.pack(padx=5)
    new.mainloop()


def AddText():
    global im,i,shown_image
    img1 = cv2.imread("1.jpg")
    
    tex = Tk()
    tex.title("Edit Text")
    tex.geometry("200x370")
    lb = Label(tex,text="Enter text here")
    lb.pack()

    textbar1=Entry(tex,font=("verdana",10))
    textbar1.pack()

    lb2 = Label(tex,text="width")
    lb2.pack()
    
    textbar2=Entry(tex,font=("verdana",10))
    textbar2.pack()

    lb3 = Label(tex,text="height")
    lb3.pack()
    
    textbar3=Entry(tex,font=("verdana",10))
    textbar3.pack()

    lb4 = Label(tex,text="font-size")
    lb4.pack()
    
    textbar4=Entry(tex,font=("verdana",10))
    textbar4.pack()

    State1 = Scale(tex,from_=0,to_=255,orient=HORIZONTAL)
    State1.pack()

    State2 = Scale(tex,from_=0,to_=255,orient=HORIZONTAL)
    State2.pack()

    State3 = Scale(tex,from_=0,to_=255,orient=HORIZONTAL)
    State3.pack()

    lb5 = Label(tex,text="Thickness")
    lb5.pack()

    textbar5 = Entry(tex,font=("verdana",10))
    textbar5.pack()
    def EditText():
        text =str(textbar1.get())
        width = int(textbar2.get())
        height = int(textbar3.get())
        size = float(textbar4.get())
        thickness = int(textbar5.get())
        R = int(State1.get())
        G = int(State2.get())
        B = int(State3.get())
        final = cv2.putText(img1,text,(width,height),cv2.FONT_HERSHEY_SIMPLEX,size,(B,G,R),thickness)
        cv2.imwrite("1.jpg",final)

        confuse()
        
    btn = Button(tex,text="Ok",command=EditText)
    btn.pack(pady=5)

    plot_img = mpimg.imread("1.jpg")
    plt.figure()
    plt.imshow(plot_img)
    plt.show()
    
    tex.mainloop()

def AddText_s(val):
    global im,i,shown_image
    img1 = cv2.imread("1.jpg")
    
    tex = Tk()
    tex.title("Edit Text")
    tex.geometry("200x370")
    lb = Label(tex,text="Enter text here")
    lb.pack()

    textbar1=Entry(tex,font=("verdana",10))
    textbar1.pack()

    lb2 = Label(tex,text="width")
    lb2.pack()
    
    textbar2=Entry(tex,font=("verdana",10))
    textbar2.pack()

    lb3 = Label(tex,text="height")
    lb3.pack()
    
    textbar3=Entry(tex,font=("verdana",10))
    textbar3.pack()

    lb4 = Label(tex,text="font-size")
    lb4.pack()
    
    textbar4=Entry(tex,font=("verdana",10))
    textbar4.pack()

    State1 = Scale(tex,from_=0,to_=255,orient=HORIZONTAL)
    State1.pack()

    State2 = Scale(tex,from_=0,to_=255,orient=HORIZONTAL)
    State2.pack()

    State3 = Scale(tex,from_=0,to_=255,orient=HORIZONTAL)
    State3.pack()

    lb5 = Label(tex,text="Thickness")
    lb5.pack()

    textbar5 = Entry(tex,font=("verdana",10))
    textbar5.pack()
    def EditText():
        text =str(textbar1.get())
        width = int(textbar2.get())
        height = int(textbar3.get())
        size = float(textbar4.get())
        thickness = int(textbar5.get())
        R = int(State1.get())
        G = int(State2.get())
        B = int(State3.get())
        final = cv2.putText(img1,text,(width,height),cv2.FONT_HERSHEY_SIMPLEX,size,(B,G,R),thickness)
        cv2.imwrite("1.jpg",final)

        confuse()
        
    btn = Button(tex,text="Ok",command=EditText)
    btn.pack(pady=5)

    plot_img = mpimg.imread("1.jpg")
    plt.figure()
    plt.imshow(plot_img)
    plt.show()
    
    tex.mainloop()
canvas_image = Label(root,bg="black",width="1100",height="650")
canvas_image.pack(anchor=CENTER)

menu = Menu(root)
root.config(menu=menu)


    
menu.add_cascade(label="Open",command=ShowImage,accelerator='ctrl+o')
menu.add_cascade(label="Save",command=SaveImage,accelerator='ctrl+s')

new = Menu(menu)
new.add_command(label="+",command=Brightness_plus)
new.add_command(label="-",command=Brightness_negative)
menu.add_cascade(label="Brightness", menu=new)

color_for = Menu(menu)
color_for.add_command(label="+",command=Color_plus)
color_for.add_command(label="-",command=Color_negative)
menu.add_cascade(label="Color",menu=color_for)

types = Menu(menu)
types.add_command(label="BGR TO RGB",command=Change_BGR_RGB)
types.add_command(label="BGR TO BW",command=Change_BW)
types.add_command(label="RGB TO BGR",command=Change_RGB_BGR)
types.add_command(label="Line Art",command=LineArt)
types.add_command(label="Original",command=Original,accelerator='ctrl+z')
menu.add_cascade(label="Convert",menu=types)

menu.add_cascade(label="Crop",command=Crop,accelerator='ctrl+c')

transform = Menu(menu)
transform.add_command(label="Rotate",command=rotate,accelerator='ctrl+r')
transform.add_command(label="Flip",command=Flip)
transform.add_command(label="Blur",command=Blur)
transform.add_command(label="Sharpness",command=Sharpness)
menu.add_cascade(label="Transform",menu=transform)

edit_text= Menu(menu)
edit_text.add_command(label="Add Text",command=AddText)

menu.add_cascade(label="Text",menu=edit_text,accelerator='ctrl+t')
menu.add_cascade(label="Show Histogram",command=ShowHistogram)

root.bind_all("<Control-c>",Crop_s)
root.bind_all("<Control-s>",SaveImage_s)
root.bind_all("<Control-o>",ShowImage_s)
root.bind_all("<Control-h>",ShowHistogram_s)
root.bind_all("<Control-t>",AddText_s)
root.bind_all("<Control-z>",Original_s)

root.title("Image_editor")
root.geometry("1400x1000")


root.mainloop()


        
