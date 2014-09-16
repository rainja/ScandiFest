'''
Created on Sep 15, 2014

@author: Paul Reesman
'''

import Tkinter as tk
import ttk

def splash():
    root = tk.Tk()
    # show no frame
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
    # take a .jpg picture you like, add text with a program like PhotoFiltre
    # (free from http://www.photofiltre.com) and save as a .gif image file
    image_file = "Internetdownload.gif"
    #assert os.path.exists(image_file)
    # use Tkinter's PhotoImage for .gif files
    image = tk.PhotoImage(file=image_file)
    canvas = tk.Canvas(root, height=height*0.75, width=width*0.75, bg="black")
    canvas.create_image(width*0.75/2, height*0.75/2, image=image)
    canvas.pack()
    
    progress = ttk.Progressbar(root, orient="horizontal", length=width*0.3, mode="determinate")
    progress.pack(expand=True, side=tk.TOP)
    # show the splash screen for 5000 milliseconds then destroy
    progress.start(42)
    
    root.after(5000, root.destroy)
    
    root.mainloop()
splash()