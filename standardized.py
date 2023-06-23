import pandas as pd
import os
import random

# Đường dẫn thư mục chứa ảnh
folder_path = r'E:\Study\TTM\Save data'

# Tạo danh sách các đường dẫn tới ảnh và nhãn tương ứng
data = {
    'label': [],
    'data': [],
    'type': []
}


def savedata():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)  # Đường dẫn đầy đủ đến tệp

        # Kiểm tra xem tệp có phải là tệp văn bản hay không
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                rdata = file.readlines()
                # Tách chuỗi thành các phần tử riêng biệt, loại bỏ ký tự "\n" từ mỗi phần tử
                # data_row = [value.rstrip('\n') for value in rdata[0].strip().split()]
                # data_row = rdata[0].strip().split()[1:]
                label = rdata[0].strip().split()[0]
                data_row = rdata[0].strip().split()[1:]
                data['label'].append(label)
                data['data'].append(data_row)
                data['type'].append('')


    # Tỉ lệ phần trăm của tập huấn luyện (vd: 80%)
    train_percentage = 0.8

    # Số lượng mẫu trong tập huấn luyện
    num_train_samples = int(train_percentage * len(data['data']))

    # Chọn ngẫu nhiên các mẫu cho tập huấn luyện
    train_indices = random.sample(range(len(data['data'])), num_train_samples)

    # Gán giá trị "train" cho các mẫu trong tập huấn luyện
    for index in train_indices:
        data['type'][index] = 'train'

    # Gán giá trị "test" cho các mẫu không thuộc tập huấn luyện
    for index in range(len(data['data'])):
        if data['type'][index] == '':
            data['type'][index] = 'test'


    # Tạo DataFrame từ danh sách dữ liệu
    df = pd.DataFrame(data, columns=['label', 'data', 'type'])

    # Lưu DataFrame thành tệp tin CSV
    csv_file = r'E:\Study\TTM\Save data\data.csv'
    df.to_csv(csv_file, index=False)