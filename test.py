import tkinter as tk

root = tk.Tk()

# Create the first widget
label1 = tk.Label(root, text="Widget 1", bg="yellow")
label1.place(x=50, y=50)  # Use place to set the initial position

# Create the second widget
label2 = tk.Label(root, text="Widget 2", bg="green")
label2.pack(fill="both")  # Use pack to place it under the first widget

root.mainloop()
