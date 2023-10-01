# import tkinter as tk

# # Create the Tkinter window
# window = tk.Tk()
# window.title("Gradient Background Example")

# # Set the window size
# window.geometry("500x500")

# # Create a canvas widget
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# # Create a gradient background
# canvas.create_rectangle(0, 0, 500, 500, fill="red", outline="")
# canvas.create_rectangle(0, 0, 500, 250, fill="blue", outline="")

# # Run the Tkinter event loop
# window.mainloop()
# from PIL import Image

# img = Image.new('RGBA', (900, 900))

# for i in range(900):
#     for j in range(900):
#         red = int(i / 4)
#         blue = 0
#         green = int(j / 4)
#         img.putpixel((i, j), (red, blue, green))

# img.show()
# img.save("background_image.png")
# from tkinter import *

# root = Tk()
# root.title('Magasin Carrefour')
# root.geometry("800x500")

# bg =PhotoImage(file="carrefour.png")
# my_label= Label(root,image=bg)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)

# my_canvas=Canvas(root, width=800, height=500)
# my_canvas.pack(fill='both', expand=True)
# my_canvas.create_image(0,0, Image=bg, anchro='nw')
# root.mainloop()

from PIL import Image, ImageTk
from tkinter import Tk, BOTH, Canvas 
from tkinter.ttk import Frame, Label, Style

root = Tk()
root.title('Screen')

w = Canvas(root, width=800 , height=480)
w.pack()

back_ground = ImageTk.PhotoImage(Image.open("background_image.png"))
back_ground_label = Label(image=back_ground, borderwidth=0)
back_ground_label.place(x=0,y=0)
back_ground_label = Label(image=back_ground, borderwidth=0)
back_ground_label.place(x=0,y=0)
back_ground_label = Label(image=back_ground, borderwidth=0)
back_ground_label.place(x=0,y=0)
w.create_rectangle(0, 400, 800, 480,outline="#000", fill="#000")
w.pack()

root.mainloop()