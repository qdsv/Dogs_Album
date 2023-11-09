import tkinter

pnum = 0
def photograph():
    global pnum
    canvas.delete("PH")
    canvas.create_image(400,400, image=photo[pnum], tag="PH")
    pnum += 1
    if pnum>= len(photo):
        pnum = 0
    root.after(3000, photograph) #after -> ms단위 = 1000==1초

root = tkinter.Tk()
root.title("디지털 액자")
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

photo=[
tkinter.PhotoImage(file="dog01.png"),
tkinter.PhotoImage(file="dog02.png"),
tkinter.PhotoImage(file="dog03.png"),
tkinter.PhotoImage(file="dog04.png")
]

photograph()
root.mainloop()