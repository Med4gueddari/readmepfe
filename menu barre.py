import tkinter as tk

def on_button_click():
    print("Button clicked")

# Create the main window
window = tk.Tk()

# Calculate the center coordinates of the window
window_width = 500
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window size and position it in the center
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame to hold the menu
menu_frame = tk.Frame(window)
menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create buttons in the menu frame
button1 = tk.Button(menu_frame, text="Button 1", command=on_button_click)
button1.pack()

button2 = tk.Button(menu_frame, text="Button 2", command=on_button_click)
button2.pack()

button3 = tk.Button(menu_frame, text="Button 3", command=on_button_click)
button3.pack()

# Start the main loop
window.mainloop()
