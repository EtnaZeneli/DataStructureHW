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
SearchaBar= Label(root, text="Search")
Searchbar=Entry(root)
SearchaBar.pack()
Searchbar.pack()

def MusicCategories():
    Seachbare= Searchbar.get()
    if (Seachbare== "Playlist One"):
        def playsong0():
            winsound.PlaySound('n.wav',winsound.SND_FILENAME)
        def playsong1():
            winsound.PlaySound('t.wav',winsound.SND_FILENAME)
        def playsong2():
            winsound.PlaySound('e.wav',winsound.SND_FILENAME)
        def playsong3():
            winsound.PlaySound('a.wav',winsound.SND_FILENAME)
        def playsong4():
            winsound.PlaySound('g.wav',winsound.SND_FILENAME)
        def playsong5():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        def playsong6():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        def playsong7():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
            
        lbl1 = Label (root, text = "List of Playlist 1")
        btn0 = Button(frameleft, text="Song 1", height = 10, width = 20, command = playsong0)
        btn1 = Button(frameleft, text="Song 2", height = 10, width = 20, command = playsong1)
        btn2 = Button(frameleft, text="Song 3", height = 10, width = 20, command = playsong2)
        btn3 = Button(frameleft, text="Song 4",height = 10, width = 20, command = playsong3)
        btn4 = Button(frameright, text="Song 5", height = 10, width = 20, command = playsong4)
        btn5 = Button(frameright, text="Song 6", height = 10, width = 20, command = playsong5)
        btn6 = Button(frameright, text="Song 7", height = 10, width = 20, command = playsong6)
        btn7 = Button(frameright, text="Song 8", height = 10, width = 20, command = playsong7)
        lbl1.pack() 
        btn0.pack() 
        btn1.pack() 
        btn2.pack() 
        btn3.pack() 
        btn4.pack() 
        btn5.pack() 
        btn6.pack() 
        btn7.pack() 

    elif(Seachbare=="Playlist Two"):
        
        def playsong01():
            winsound.PlaySound('g.wav',winsound.SND_FILENAME)
        def playsong11():
            winsound.PlaySound('n.wav',winsound.SND_FILENAME)
        def playsong21():
            winsound.PlaySound('a.wav',winsound.SND_FILENAME)
        def playsong31():
            winsound.PlaySound('t.wav',winsound.SND_FILENAME)
        def playsong41():
            winsound.PlaySound('e.wav',winsound.SND_FILENAME)
        def playsong51():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        def playsong61():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        def playsong71():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        lbl11 = Label (root, text = "List of Playlist 2")
        btn01 = Button(frameleft, text="Song 1", height = 10, width = 20, command = playsong01)
        btn11 = Button(frameleft, text="Song 2", height = 10, width = 20, command = playsong11)
        btn21 = Button(frameleft, text="Song 3", height = 10, width = 20, command = playsong21)
        btn31 = Button(frameleft, text="Song 4", height = 10, width = 20, command = playsong31)
        btn41 = Button(frameright, text="Song 5", height = 10, width = 20, command = playsong41)
        btn51 = Button(frameright, text="Song 6", height = 10, width = 20, command = playsong51)
        btn61 = Button(frameright, text="Song 7", height = 10, width = 20, command = playsong61)
        btn71 = Button(frameright, text="Song 8",height = 10, width = 20, command = playsong71)
    
        lbl11.pack() 
        btn01.pack() 
        btn11.pack() 
        btn21.pack() 
        btn31.pack() 
        btn41.pack() 
        btn51.pack() 
        btn61.pack() 
        btn71.pack()
        
    elif(Seachbare=="Playlist Three"):
        
        def playsong02():
            winsound.PlaySound('t.wav',winsound.SND_FILENAME)
        def playsong12():
            winsound.PlaySound('n.wav',winsound.SND_FILENAME)
        def playsong22():
            winsound.PlaySound('a.wav',winsound.SND_FILENAME)
        def playsong32():
            winsound.PlaySound('e.wav',winsound.SND_FILENAME)
        def playsong42():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        def playsong52():
            winsound.PlaySound('g.wav',winsound.SND_FILENAME)
        def playsong62():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        def playsong72():
            winsound.PlaySound('musical001.wav',winsound.SND_FILENAME)
        lbl12 = Label (root, text = "List of Playlist Three", height = 15, width = 3)
        btn02 = Button(frameleft, text="Song 1",height = 15, width = 3, command = playsong02)
        btn12 = Button(frameleft, text="Song 2", height = 15, width = 3, command = playsong12)
        btn22 = Button(frameleft, text="Song 3",height = 15, width = 3, command = playsong22)
        btn32 = Button(frameleft, text="Song 4",height = 15, width = 3, command = playsong32)
        btn42 = Button(frameright, text="Song 5",height = 15, width = 3, command = playsong42)
        btn52 = Button(frameright, text="Song 6", height = 15, width = 3, command = playsong52)
        btn62 = Button(frameright, text="Song 7", height = 15, width = 3, command = playsong62)
        btn72 = Button(frameright, text="Song 8",height = 15, width = 3, command = playsong72)

        lbl12.pack() 
        btn02.pack() 
        btn12.pack() 
        btn22.pack() 
        btn32.pack() 
        btn42.pack() 
        btn52.pack() 
        btn62.pack() 
        btn72.pack() 

    else:
        lbl007= Label(root,text="No Data Found")
        lbl007.pack()
  
btnsearch = Button (root, text = "Search Music", command= MusicCategories)
btnsearch.pack()


mainloop()

