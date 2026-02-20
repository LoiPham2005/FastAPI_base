# FastAPI Project

Cấu trúc cơ bản cho dự án FastAPI của bạn.

## Cấu trúc thư mục

```text
fast_api/
├── app/
│   ├── main.py          # Điểm khởi đầu của ứng dụng
│   ├── api/             # Các API routes
│   │   └── router.py
│   ├── core/            # Cấu hình hệ thống (Settings, security, etc)
│   │   └── config.py
│   ├── models/          # Database models (SQLAlchemy, Tortoise, etc)
│   ├── schemas/         # Pydantic models (Data validation)
│   └── crud/            # Create, Read, Update, Delete logic (Tùy chọn)
├── .env                 # Biến môi trường
├── .gitignore
├── requirements.txt
└── README.md
```

## Cách chạy dự án

1. **Tạo môi trường ảo (Virtual Env):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Cài đặt thư viện:**
   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   pip install pydantic-settings
   ```

3. **Chạy ứng dụng:**
   ```bash
   uvicorn app.main:app --reload
   ```

   **Chạy ứng dụng bằng Docker:**
  ```bash
  docker-compose up --build
  ```

4. **Truy cập Documentation:**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
