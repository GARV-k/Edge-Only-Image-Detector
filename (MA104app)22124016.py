from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import shutil

pic_1 = None

def pic_select():
    global pan1, pan2, location_of_pic
    global pic_1
    location_of_pic = filedialog.askopenfilename()

    if len(location_of_pic) > 0:
        pic = cv2.imread(location_of_pic)
        grayscale = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        edge_only_pic = cv2.Canny(grayscale, 50, 100)
        # above code reads the pic, converts to grayscale then to edge only pic

         
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        # OpenCV has BGR order; however, PIL has RGB order hence swapping

        pic = Image.fromarray(pic)
        edge_only_pic = Image.fromarray(edge_only_pic)
        pic_1 =edge_only_pic
        #converting pic using PIL
        pic = ImageTk.PhotoImage(pic)
        edge_only_pic = ImageTk.PhotoImage(edge_only_pic)
        # pic_1 = edge_only_pic

        if pan1 is None or pan2 is None:
            # first panel is to store the real pic while second is to store edge only pic
            pan1 = Label(image=pic)
            pan1.image = pic
            pan1.pack(side="left", padx=10, pady=10)

            pan2 = Label(image=edge_only_pic)
            pan2.image = edge_only_pic
            pan2.pack(side="left", padx=10, pady=10)

        else:
            # update the panels
            pan1.configure(image=pic)
            pan2.configure(image=edge_only_pic)
            pan1.image = pic
            pan2.image = edge_only_pic

def copy_image():

    # pic_1.save("lo.jpg")
    save_window()
    # # create a copy of the image and save it to a new file
    # save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    # if len(save_path) > 0:
    #     shutil.copy(location_of_pic, save_path)
    #     print("Image has been saved successfully.")

name_entry =None
prompt_menu2 =None
screen = None

def save_window():
    global screen
    global clicked2
    global prompt_menu2
    options = [".jpg" , ".png" , ".jpeg"]
    global name_entry
    screen = Tk()
    screen.geometry('300x130')
    label1 = Label(screen,text="Please enter file name and select the extension below:")
    label1.place(x=0,y=0)
    name_entry = Entry(screen,width=20)
    # name_entry.insert(0,"name with extension")
    name_entry.place(x=90,y=20)

    prompt_menu2 = OptionMenu(screen,clicked2,*options)
    prompt_menu2.config(width=5,fg="black")
    prompt_menu2.place(x=110 ,y=45)
    
    button_1 = Button(screen ,text="save" ,command=save)
    button_1.place(x=132,y=85)

def save():
    global name_entry
    name = name_entry.get()
    ext = clicked2.get()
    pic_1.save(f"{name}{ext}")
    screen.destroy()

rt = Tk()
rt.title("Image Edge Detector")
rt.geometry("600x400")
style = ttk.Style()
if "clam" in style.theme_names():
    style.theme_use("clam")

pan1 = None
pan2 = None
location_of_pic = ""

button_frame = Frame(rt)
button_frame.pack(side="bottom", pady=10)

select_button = Button(button_frame, text="Select an image", command=pic_select)
select_button.pack(side="left", padx=10)

clicked2 = StringVar()
clicked2.set("Currency")
copy_button2 = Button(button_frame, text="Download Edge-Only Image", state=DISABLED, command=copy_image)
copy_button2.pack(side="left", padx=10)

def enable_download_buttons():
    copy_button2.config(state=NORMAL)

rt.after(100, enable_download_buttons)

rt.mainloop()



