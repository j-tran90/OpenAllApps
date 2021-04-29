import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('setting.txt'):
    with open('setting.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#f functions
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title = "Select Fille", filetypes = (("executeables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "#1f1f1f", fg = "white")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height = 300, width = 700, bg = "#1f1f1f")

canvas.pack()



# embedded frame style
frame = tk.Frame(root, bg = "#1f1f1f")
frame.place(relwidth = 0.8, relheight = 0.5, relx = 0.1, rely = 0.1)

# select what files to launch
openFile = tk.Button(root, text="Select Applications", padx = 10, pady = 5, fg ="black", bg = "orange", command = addApp) 

openFile.pack()

# launch all selected apps
runApps = tk.Button(root, text = "Launch Applications", padx = 10, pady = 5, fg = "black", bg = "orange", command = runApps)

runApps.pack()

for app in apps:
    label = tk.Label(frame, text = app, bg = "#1f1f1f", fg = "white")
    label.pack()

root.mainloop()



# save slected files
with open('setting.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

        