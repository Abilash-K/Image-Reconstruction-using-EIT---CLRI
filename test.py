import tkinter as tk
import numpy as np

#
# # Create the main window and canvas
# root = tk.Tk()
# canvas = tk.Canvas(root, width=400, height=400)
# canvas.pack()
#
# Define the oval parameters
circle_X = 210
cirxle_Y= 148
radius = 120

x0, y0, x1, y1 = circle_X-radius,cirxle_Y-radius,circle_X+radius,cirxle_Y+radius
#
# # Create the oval shape
# oval = canvas.create_oval(x0, y0, x1, y1, fill="purple")
#
# # Divide the oval into sections
# coords = []
# num_sections = 8
# for i in range(num_sections):
#     theta = 2 * i * 3.14159 / num_sections
#     x = (x0 + x1) / 2 + (x1 - x0) / 2 * np.cos(theta)
#     y = (y0 + y1) / 2 + (y1 - y0) / 2 * np.sin(theta)
#     x0_, y0_ = (x0 + x1) / 2, (y0 + y1) / 2
#     a = canvas.create_line(x, y, x0_, y0_, fill='black', width=2)
#     b= canvas.coords(a)
#     coords.extend([b])
#
# print(coords)
# root.mainloop()




def electrode_val():
    global electrode
    electrode = 8


def creating_electrodes():
    # Divide the oval into sections
    x0, y0, x1, y1 = circle_X - radius, cirxle_Y - radius, circle_X + radius, cirxle_Y + radius
    coords = []
    num_sections = 8
    for i in range(electrode):
        theta = 2 * i * 3.14159 / electrode
        x = (x0 + x1) / 2 + (x1 - x0) / 2 * np.cos(theta)
        y = (y0 + y1) / 2 + (y1 - y0) / 2 * np.sin(theta)
        x0_, y0_ = (x0 + x1) / 2, (y0 + y1) / 2
        # a = canvas.create_line(x, y, x0_, y0_, fill='black', width=2)
        # b = canvas.coords(a)
        # coords.extend([b])
        print(x,y,x0_,y0_)


electrode_val()
creating_electrodes()
