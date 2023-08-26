import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
import tkinter.messagebox
import pikepdf
from tkinter import PhotoImage, filedialog

# def choosefile():
#     pdf =  filedialog.askopenfilename(initialdir="/", title="Select A PDF", filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))

def protect():
    pdf_location = location.get()
    pdf_password = password.get()
    pdf_name = new_pdf_name.get()+".pdf"

    old_pdf = pikepdf.Pdf.open(pdf_location)

    no_extr = pikepdf.Permissions(extract=False)
    try:
        old_pdf.save(pdf_name, encryption= pikepdf.Encryption(user=pdf_password, owner="USER", allow=no_extr))
        #status.set('PDF Protected')
        tkinter.messagebox.showinfo("PDF Protector",  "PDF Protected and saved in the root folder")
    except:
        #status.set('Failed to protect')
        tkinter.messagebox.showinfo("PDF Protector",  "PDF Protection Failed")

window = ttk.Window(themename='darkly')

window.title("Protect PDF   ||   MAF")
window.geometry('650x300')
window.iconbitmap("icon.ico")

input_frame0 = ttk.Frame(master=window)
input_frame1 = ttk.Frame(master=window)
input_frame2 = ttk.Frame(master=window)
input_frame3 = ttk.Frame(master=window)
input_frame4 = ttk.Frame(master=window)
input_frame_space = ttk.Frame(master=window)

location = tk.StringVar()
location_label = ttk.Label(master= input_frame0,  text = "PDF LOCATION            :  ", font= "Poppins 12 bold")
#location_label = ttk.Label(master= input_frame,  text = "PDF", font= "Poppins 12 bold")

new_pdf_name = tk.StringVar()
new_pdf_name_label = ttk.Label(master= input_frame1,  text = "NEW PDF NAME          :  ", font= "Poppins 12 bold")


password = tk.StringVar()
password_label = ttk.Label(master= input_frame2, text = " SET PASSWORD         :  ", font= "Poppins 12 bold")


entry =  ttk.Entry(master=input_frame0, textvariable= location)
entry1 = ttk.Entry(master=input_frame1, textvariable= new_pdf_name)
entry2 = ttk.Entry(master=input_frame2, textvariable= password)
button = ttk.Button(master=input_frame3, text = "Protect", command= protect)

status = tk.StringVar()
status_label = ttk.Label(master= input_frame2, text = "PDF Protected", font= "Poppins 5", textvariable=status)

input_frame_space.pack(pady= 10)

location_label.pack(side= "left")
#entry_button_choose.pack(pady=10)
entry.pack(side = 'left', padx= 5)
input_frame0.pack(pady=10)

new_pdf_name_label.pack(side= "left")
entry1.pack(side = 'left', padx= 5)
input_frame1.pack(pady= 10)

password_label.pack(side= "left")
entry2.pack(side = 'left', padx= 5)
input_frame2.pack(pady= 10)

button.pack()
input_frame3.pack(pady= 10)

status_label.pack(pady=5)



window.mainloop()