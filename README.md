# api-huggingface-fastapi
 Bài thực hành 1 - Web API với FastAPI và Hugging Face

## 1. Thông tin sinh viên
Họ và tên: Võ Nhật Minh  
Mã số sinh viên: 24120202  
Lớp: Tư duy tính toán - 24CTT3

## 2. Mô hình và liên kết Hugging Face
Tên mô hình: google/vit-base-patch16-224  
Liên kết:[https://huggingface.co/google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224)

## 3. Mô tả chức năng hệ thống
Hệ thống là một Web API được xây dựng bằng FastAPI nhằm khai thác mô hình Vision Transformer (ViT).  
Chức năng chính là nhận một tệp hình ảnh từ người dùng và thực hiện phân loại, trả về nhãn của sự vật trong ảnh cùng độ tin cậy tương ứng ở định dạng JSON.

## 4. Hướng dẫn cài đặt thư viện

```
Để cài đặt các thư viện cần thiết, chạy lệnh sau trong terminal:
```bash
pip install -r requirements.txt
```
## 5. Hướng dẫn chạy chương trình 
**Note**: Áp dụng trên hệ điều hành Windows, sử dụng PowerShell để chạy các lệnh.  
**Note**: còn Google Colab thì không cần cài đặt thư viện, chỉ cần chạy các cell code là được.

Mở 3 tab terminal, mỗi tab thực hiện một công việc khác nhau:  
Tab 1: Chạy server FastAPI cho main.py  
Tab 2: Dùng Pinggy để tạo đường dẫn public URL  
Tab 3: Chạy file test_api.py để triển khai API và gửi request  
Trước tiên tạo môi trường ảo cho cả 3 tab bằng lệnh:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate
```
-Khởi động server FastAPI trong main.py bằng lệnh:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

-Dùng pinggy để lấy đường dẫn public URL:
```bash
ssh -p 443 -R0:localhost:8000 qr@a.pinggy.io
```
Sau khi chạy pinggy nó sẽ trả về https://xxxx.a.free.pinggy.link
Dán đường link vào BASE_URL trong file test_api.py

-Chạy file api chính để triển khai API:
``` bash
python test_api.py
```
## 6. Hướng dẫn sử dụng API:
Ví dụ Request (Sử dụng Python requests):  
Trước tiên phải có BASE_URL là đường dẫn public URL từ pinggy tệp hình ảnh đã chèn vào thư mục
```bash
with open(image_filename, "rb") as image_file:
            # Cấu trúc dữ liệu gửi lên API
            files = {"file": (image_filename, image_file, "image/jpeg")}
            
            # Gửi request
            res = requests.post(f"{BASE_URL}/predict", files=files)
            
            print(f"Kết quả dự đoán cho {image_filename}:")
            print(res.json())
```
Ví dụ Response thực tế từ hệ thống:  
Của Image_1.jpg  
```bash
{
  "data": [
    {
      "label": "comic book",
      "score": 0.9917703866958618
    },
    {
      "label": "book jacket, dust cover, dust jacket, dust wrapper",
      "score": 0.004874749109148979
    }
  ]
}
```
**label**: Nhãn dự đoán của mô hình cho hình ảnh.  
**score**: Độ tin cậy của dự đoán, giá trị từ 0 đến 1, càng gần 1 thì mô hình càng chắc chắn về dự đoán đó.

## 7. Video demo
https://drive.google.com/file/d/1kdsIXWTbrNReBPmqIA2A1d4bkQdTX3RZ/view?usp=drive_link
