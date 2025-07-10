from tkinter import *

window = Tk()
window.geometry("800x192")
window.title("new window")
window.configure(bg="black")
frame1 = Frame(window,width=100, height=100, cursor= "dot" )
frame2 = Frame(window,width=100, height=100, cursor= "dot" )
button1 = Button(frame1,text="Buttten",bg="gray",fg="white")
button2 = Button(frame2,text="Buttten",bg="gray",fg="white")


frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
mainloop()