import tkinter as tk
from tkinter import *
from tkinter import filedialog
import torch
import torchvision
from PIL import ImageTk, Image
from torch import nn
from torchvision.transforms import transforms
from interface import makecenter

def run():
    root = Tk()
    root.title("Chẩn đoán bệnh viêm quanh cuống")
    root.resizable(height=False, width=False)
    root.minsize(height=340, width=400)

    frame = Frame(root)
    filename = None

    def selectpic():
        global filename  # Khai báo biến filename là biến toàn cục
        filename = filedialog.askopenfilename(initialdir="E:\Study\TTM\Viêm quanh cuống goc", title="Select Image",filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png")))
        img = Image.open(filename)
        img.thumbnail((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        lbl_show_pic.configure(image=img)
        lbl_show_pic.image = img

    def resnet():
        # Số lượng lớp trong bài toán phân loại
        num_classes = 2

        # Khởi tạo transform để chuẩn hóa ảnh và chuyển đổi thành tensor
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        # Xây dựng mô hình ResNet đã được huấn luyện trước
        model = torchvision.models.resnet34(pretrained=True)
        num_features = model.fc.in_features
        model.fc = nn.Linear(num_features, num_classes)

        # Chuẩn bị dữ liệu mới
        global filename  # Khai báo biến filename là biến toàn cục
        image = Image.open(filename)

        transformed_image = transform(image)
        transformed_image = transformed_image.unsqueeze(0)

        # Đưa dữ liệu mới qua mô hình để dự đoán
        model.eval()
        with torch.no_grad():
            outputs = model(transformed_image)

        # Lấy kết quả dự đoán
        _, predicted_labels = torch.max(outputs, 1)
        # return predicted_labels
        # In kết quả dự đoán
        if predicted_labels == 0:
            lbl_diagnose.configure(text='Không bị bệnh')
        elif predicted_labels == 1:
            lbl_diagnose.configure(text='Bị bệnh')

    lbl_show_pic = tk.Label(root)
    lbl_show_pic.place(x=20, y=20)
    lbl_show_pic.pack()

    lbl_diagnose = Label(root)
    lbl_diagnose.pack()

    btn_browse = Button(frame, font=('verdana', 16), text='Select Image', bg='grey', command=selectpic)
    btn_run = Button(frame, font=('verdana', 16), text='Run', bg='grey', command=resnet)

    btn_browse.pack(side=tk.LEFT)
    btn_run.pack(side=tk.LEFT, padx=15)

    frame.pack(side=BOTTOM, padx=5, pady=10)
    makecenter(root)
    root.mainloop()