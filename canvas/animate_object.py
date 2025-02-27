import tkinter as tk

root=tk.Tk()

WIDTH = 500
HEIGHT = 500

canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()

x1 = WIDTH / 2
y1 = HEIGHT / 2
  
image = canvas.create_rectangle(x1-30-30, y1-30-30, x1+30-30, y1 +30-30, fill="blue")
image2 = canvas.create_rectangle(x1+30-30, y1+30-30, x1 + 90-30, y1 + 90-30, fill="green")
image3 = canvas.create_rectangle(x1-30-30, y1+30-30, x1 + 30-30, y1 + 90-30, fill="yellow")
image4 = canvas.create_rectangle(x1+30-30, x1-30-30, x1+90-30, x1+30-30, fill="red")

def redraw():
   canvas.after(50,redraw)
   canvas.move(image2,5,5)
   canvas.move(image,-5,-5)
   canvas.move(image4,5,-5)
   canvas.move(image3,-5,5)

   if(canvas.coords(image2)[0]==500):
       root.destroy()
       
redraw()
root.mainloop()
