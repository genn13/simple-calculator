import tkinter as tk

root = tk.Tk()
root.title("Cute Button Window")
root.geometry("360x220")
root.configure(bg="#d4ffda")

background_canvas = tk.Canvas(root, width=360, height=220, highlightthickness=0)
background_canvas.place(x=0, y=0, relwidth=1, relheight=1)
background_canvas.create_rectangle(0, 0, 360, 220, fill="#d4ffda", outline="")
background_canvas.create_oval(-120, -100, 220, 220, fill="#b8f7c1", outline="")
background_canvas.create_oval(140, 60, 480, 360, fill="#ccffdd", outline="")

label = tk.Label(root, text="", font=("Comic Sans MS", 18), bg="#d4ffda", fg="#d147a3")
label.pack(pady=30)


def on_click():
    label.config(text="I love Olesia", fg="#ff69b4")

button = tk.Button(
    root,
    text="Click me",
    command=on_click,
    font=("Comic Sans MS", 14, "bold"),
    bg="#ffb6c1",
    fg="#4b0082",
    activebackground="#ff99cc",
    activeforeground="#2f004f",
    relief=tk.RAISED,
    bd=4,
    padx=12,
    pady=8,
)
button.pack()

root.mainloop()
