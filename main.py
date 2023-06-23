import tkinter as tk
from tkinter import filedialog
from tkinter import *
from interface import makecenter
from standardized import savedata
from runimage import run

root = Tk()
root.title("Chẩn đoán bệnh viêm quanh cuống")
root.resizable(height=True,width=True)
root.minsize(height=200,width=250)

frame = Frame(root)


# Chọn thư mục chứa dữ liệu và hiển thị đường dẫn
def directory():
    folder_path = filedialog.askdirectory(initialdir='E:\Study\TTM\Data')
    lbl_show_path.insert(0, folder_path)


lbl_path = tk.Label(frame, text='Data path:', font=('verdana',16))
lbl_show_path = tk.Entry(frame, font=('verdana',16), width=25)
btn_browse = Button(frame, font=('verdana',16), text='Select Folder', bg='grey', command=directory)
btn_save = Button(frame, font=('verdana',16), text='Save to csv', bg='grey',command = savedata)
btn_run = Button(frame, font=('verdana',16), text='Run on image', bg='grey',command = run)
lbl_blank = tk.Label(frame, height=3)

lbl_path.grid(row=0,column=0)
lbl_show_path.grid(row=0,column=1)
lbl_blank.grid(row=1,column=1)
btn_browse.grid(row=2,column=0)
btn_save.grid(row=2,column=1)
btn_run.grid(row=2, column=2)

frame.pack(side=TOP ,padx=5,pady=10)
makecenter(root)
root.mainloop()