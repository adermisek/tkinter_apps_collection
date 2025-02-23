import tkinter as tk


def izracunaj():
    iznos_cijene = float(entry_iznos.get())
    postotak_posk = float(entry_posto.get())
    rezultat.set(round(iznos_cijene*(1+postotak_posk/100),2)) 

    label_nakon_posk_iznos.config( fg="red", font=("Arial", 14,"bold"))


root = tk.Tk()
root.title("Poskupljenje")
rezultat = tk.DoubleVar()
frame = tk.Frame(root)
frame.grid(rows=3, columns=2)
label_iznos = tk.Label(frame,text='Iznos cijene')
label_iznos.grid(row=0, column=0)

entry_iznos = tk.Entry(frame)
entry_iznos.grid(row=0, column=1)

label_posto = tk.Label(frame,text='Postotak poskupljenja')
label_posto.grid(row=1, column=0)

entry_posto= tk.Entry(frame)
entry_posto.grid(row=1, column=1)

label_nakon_posk = tk.Label(frame,text='Cijena nakon poskupljenja')
label_nakon_posk.grid(row=2, column=0)

label_nakon_posk_iznos = tk.Label(frame,textvariable=rezultat)
label_nakon_posk_iznos.grid(row=2, column=1)

izr = tk.Button(frame, text="Izračunaj", command=izracunaj)
izr.grid(row=3, columnspan=2) 


root.mainloop()
