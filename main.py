from transformers import pipeline
from PIL import Image
import io

app = FastAPI(
    title="Vision Transformer API",
    description="API phân loại hình ảnh sử dụng mô hình ViT của Google"
)

# Khởi tạo pipeline phân loại hình ảnh
try:
    classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
except Exception as e:
    classifier = None
    print(f"Lỗi khi tải mô hình: {e}")

@app.get("/")
def read_root():
    return {
        "name": "Hệ thống Phân loại Hình ảnh API",
        "description": "API này nhận vào một tệp hình ảnh và trả về kết quả dự đoán (ví dụ: con mèo, ô tô,...) cùng với độ tin cậy."
    }

@app.get("/health")
def health_check():
    if classifier is None:
        raise HTTPException(status_code=503, detail="Mô hình chưa sẵn sàng hoạt động")
    return {"status": "Hoạt động bình thường"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Kiểm tra định dạng file
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Vui lòng tải lên một tệp hình ảnh hợp lệ (JPEG, PNG,...).")
    
    try:
        # Đọc dữ liệu byte từ file tải lên
        image_data = await file.read()
        
        # Chuyển đổi thành đối tượng hình ảnh PIL
        image = Image.open(io.BytesIO(image_data))
        
        # Gọi mô hình Hugging Face để suy luận
        result = classifier(image)
        return {"data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xử lý hình ảnh: {str(e)}")
