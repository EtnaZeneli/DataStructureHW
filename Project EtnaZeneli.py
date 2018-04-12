from tkinter import*
import winsound
root=Tk()
root.geometry("500x400")
frameleft=Frame(root)
frameright=Frame(root)
frametop=Frame(root)
framebottom=Frame(root)
frameleft.pack(side=LEFT)
frameright.pack(side=RIGHT)
frametop.pack(side=TOP)
framebottom.pack(side=BOTTOM)

def playSong1():
	winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
def playsong2():
	winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
def playsong3():
	winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
def playsong4():
	winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
def playsong5():
	winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)

lbl1 = Label(frameleft, text="Jazz", height = 1,width=5)
btn1 = Button(frameleft, text="Play",height = 2, width=5,command = playSong1)
lbl2 = Label(frameleft, text="Hip-Hop",height = 1, width=11)
btn2 = Button(frameleft, text="Play",height= 2,width=5,command = playsong2)
lbl3 = Label(frameleft, text="Classical Music",height=1,width=15)
btn3 = Button(frameleft, text="Play",height=2,width=5,command = playsong3)
lbl4 = Label(frameleft, text="Mixed Music Generes", height = 1,width=15)
btn4 = Button(frameleft, text="Play",height = 2, width=5,command = playsong4)
btn5 = Button(frameright, text="Shuffle Button",height = 2, width=10,command = playsong5)

lbl1.pack()
btn1.pack()
lbl2.pack()
btn2.pack()
lbl3.pack()
btn3.pack()
lbl4.pack()
btn4.pack()
btn5.pack()

mainloop()
