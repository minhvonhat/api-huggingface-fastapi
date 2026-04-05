import requests
# Thay bằng các đường link lấy từ pinggy
BASE_URL = "http://127.0.0.1:8000"

print("--- 1. Kiểm tra giới thiệu API (GET /) ---")
try:
    res = requests.get(f"{BASE_URL}/")
    print(res.json())
except Exception as e:
    print("Lỗi kết nối:", e)

print("\n--- 2. Kiểm tra Health Check (GET /health) ---")
try:
    res = requests.get(f"{BASE_URL}/health")
    print(res.json())
except Exception as e:
    print("Lỗi kết nối:", e)

print("\n--- 3. Kiểm tra Suy luận (POST /predict) với ảnh từ máy ---")



image_list = ["Image_1.jpg", "Image_2.jpg"]
for image_filename in image_list:
    print(f"\n>> Đang xử lý file: {image_filename}")
    try:
      
        with open(image_filename, "rb") as image_file:
            # Cấu trúc dữ liệu gửi lên API
            files = {"file": (image_filename, image_file, "image/jpeg")}
            
            # Gửi request
            res = requests.post(f"{BASE_URL}/predict", files=files)
            
            print(f"Kết quả dự đoán cho {image_filename}:")
            print(res.json())

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{image_filename}'. Bạn hãy kiểm tra lại tên file hoặc chắc chắn đã upload lên Colab chưa nhé.")
    except Exception as e:
        print("Lỗi:", e)
