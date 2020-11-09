import tkinter as tk
import matplotlib
from PIL import Image, ImageTk
from tkinter import messagebox
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style




#Applys a Dark theme colour to the graph
style.use("dark_background")

#Size of the figure
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


# Function that reads the line from the text file seperates it by using the comma and plots onto the graph
def animate(i):
    dataList = open("sampleData.txt","r").readlines()
    dataList = [x.strip() for x in dataList]
    xList = [x.split(',')[0] for x in dataList ]
    yList = [x.split(',')[1] for x in dataList ]
    a.clear()
    a.plot(xList, yList)


class GUI(tk.Tk):

#Initialises the frame
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(20, weight=10)
        container.grid_columnconfigure(20, weight=10)

        self.frames = {}
              
# Switches frames and shows the current frame in the GUI
        for Page in (PAGES):
            
            frame = Page(container, self)
    
            self.frames[Page] = frame
    
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PS)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#   Base code from Sentdex Tutorial
# Creates two buttons and a log in button which takes you to the homepage
class PS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        tk.Label(self, text = "Username").grid(row = 2)

        tk.Entry(self).grid(row = 2, column = 3) 
        
        tk.Label(self, text = "Password").grid(row = 3) 
        tk.Entry(self).grid(row = 3, column = 3) 
     
        tk.Checkbutton(self, text = "Keep Me Logged In").grid(columnspan = 2) 
                                                                                    
        btn= tk.Button(self,text="Log In",
                        command=lambda: controller.show_frame(SP), bg="red", fg="white")
        btn.grid()
        
        
 # Initial Homepage frame        
class SP(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home Page", font=("Calibri Bold", 12))
        label.pack()
# Button which links to input data and graph pages
        btn1 = tk.Button(self, text="Input Data",
                            command=lambda: controller.show_frame(P1), bg="red", fg="white")
        btn1.pack()
        
        btn2 = tk.Button(self, text="Graph",
                            command=lambda: controller.show_frame(P2), bg="red", fg="white")
        btn2.pack()
        
        load = Image.open("1.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=3, y=3)

#Frame for Input data Page
class P1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl = tk.Label(self, text="Input Data", font=("Calibri Bold", 12))
        lbl.pack()

# Writes to a file when data is inputted
        def write_File(text_File):
            file = open("sampleData.txt", "a")
            user_Input = text_File.get()
            file.write(user_Input + '\n')
            file.close()

# Reads and displays the co-ordinates in the text file 
        def display():
            file = open("sampleData.txt")
            data = file.read()
            file.close()
            lbl3 = tk.Label(self, text="Co-ordinate History", font=("Calibri bold", 8))
            lbl3.pack()
            lbll = tk.Label(self, text=data, font=("Calibri", 8))
            lbll.pack()
        
        
        the_input = tk.Entry(self)
        the_input.pack()
        
        lbl = tk.Label(self, text="Insert 2 or more (one at a time) Co-ordinates in format: 1,1 ", font=("Calibri", 8))
        lbl.pack()

# Sends the user input to the text file
        button1 = tk.Button(self, text = "Send Data", command = lambda: write_File(the_input), bg="red", fg="white")
        button1.pack()

# co ordinate display button     
        button2 = tk.Button(self, text = "Show Co-ordinates", command = lambda: display(), bg="red", fg="white")
        button2.pack()
        
# Clears the co-ordinates of the text file and resets graphs     
        def erase_File():
            res = messagebox.askquestion('WARNING','Are you Sure you want to reset graph?')
            if res == 'yes':
                file = open("sampleData.txt","r+")
                file.truncate(0)
                file.close()
                messagebox.showinfo('Alert', 'All Co-ordinates Have been erased') 
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
        
        button4 = tk.Button(self, text = "Reset Graph", command = lambda:[erase_File()], bg="red", fg="white")
        button4.pack()
       
        
        
        
        btn= tk.Button(self,text="Back to Homepage",
                        command=lambda: controller.show_frame(SP), bg="red", fg="white")
        btn.pack()
       

#Button which links back to the homepage
class P2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl = tk.Label(self, text="Graph", font=("Calibri Bold", 12))
        lbl.pack()
        btn= tk.Button(self,text="Back to Homepage",
                        command=lambda: controller.show_frame(SP), bg="red", fg="white")
        btn.pack()

# Clears the co-ordinates of the text file and resets graphs         
        def erase_File():
            res = messagebox.askquestion('WARNING','Are you Sure you want to reset graph?')
            if res == 'yes':
                file = open("sampleData.txt","r+")
                file.truncate(0)
                file.close()
                messagebox.showinfo('Alert', 'All Co-ordinates Have been erased') 
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
        
        button4 = tk.Button(self, text = "Reset Graph", command = lambda:[erase_File()])
        button4.pack()

        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#Page frame names which is used by the GUI class to switch from one page to another
PAGES = [PS, SP, P1 , P2]     

window = GUI()
window.title("GUI")
window.geometry("")
ani = animation.FuncAnimation(f, animate, interval=1000)
window.mainloop()

