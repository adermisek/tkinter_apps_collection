from tkinter import Tk, Canvas, Radiobutton, IntVar

# Funkcija za crtanje kruga
def draw_circle(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='blue', outline='black')

# Funkcija za crtanje pravokutnika
def draw_rectangle(event):
    x, y = event.x, event.y
    canvas.create_rectangle(x - 30, y - 20, x + 30, y + 20, fill='green', outline='black')

# Funkcija koja poziva odgovarajuću funkciju za crtanje ovisno o odabranom obliku
def on_click(event):
    if shape_var.get() == 1:  # Ako je odabran krug
        draw_circle(event)
    elif shape_var.get() == 2:  # Ako je odabran pravokutnik
        draw_rectangle(event)

# Kreiranje glavnog prozora
root = Tk()
root.title("Crtanje oblika")

# Varijabla koja pohranjuje odabrani oblik
shape_var = IntVar()
shape_var.set(1)  # Zadano je odabrano "Krug"

# Kreiranje radio dugmadi za odabir oblika
radio_circle = Radiobutton(root, text="Krug", variable=shape_var, value=1)
radio_circle.pack()
radio_rectangle = Radiobutton(root, text="Pravokutnik", variable=shape_var, value=2)
radio_rectangle.pack()

# Kreiranje platna za crtanje
canvas = Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Povezivanje lijevog klika miša sa funkcijom on_click
canvas.bind("<Button-1>", on_click)

# Pokretanje glavne petlje aplikacije
root.mainloop()
