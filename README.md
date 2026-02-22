# FastAPI Project

Cấu trúc cơ bản cho dự án FastAPI của bạn.

## Cấu trúc thư mục

```text
fast_api_base/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   │
│   ├── core/
│   │   ├── security.py
│   │   ├── exceptions.py
│   │   ├── middleware.py
│   │   └── base_crud.py        # Generic CRUD dùng chung
│   │
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── features/               # ← Đây là thay đổi chính
│   │   ├── auth/
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   ├── service.py
│   │   │   └── dependencies.py
│   │   │
│   │   ├── users/
│   │   │   ├── router.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── service.py
│   │   │
│   │   ├── venues/
│   │   │   ├── router.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   └── service.py
│   │   │
│   │   ├── bookings/
│   │   │   ├── router.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── crud.py
│   │   │   ├── service.py
│   │   │   └── tasks.py        # Celery tasks riêng cho booking
│   │   │
│   │   └── payments/
│   │       ├── router.py
│   │       ├── models.py
│   │       ├── schemas.py
│   │       ├── crud.py
│   │       ├── service.py
│   │       └── tasks.py
│   │
│   ├── workers/                # Celery workers
│   │   ├── celery_app.py
│   │   └── beat_schedule.py    # Cronjob: nhắc giờ, hủy booking...
│   │
│   └── utils/
│       ├── email.py
│       ├── sms.py
│       └── storage.py          # Upload ảnh sân
│
├── tests/
│   ├── conftest.py
│   └── features/               # Test mirror theo feature
│       ├── test_auth.py
│       ├── test_bookings.py
│       └── test_payments.py
│
├── alembic/
├── docker-compose.yml          # app + db + redis + celery
├── Dockerfile
└── .env
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




Bước tiếp theo bạn cần làm:
Cài đặt môi trường mới:

pip install -r requirements.txt

Khởi tạo Database: Đảm bảo DATABASE_URL trong .env sử dụng driver postgresql+asyncpg://. Khi bạn chạy uvicorn app.main:app --reload, hệ thống sẽ tự động tạo các bảng dựa trên models nếu bạn đang ở chế độ DEBUG=True.
Migrations: Nếu bạn muốn dùng Alembic chuyên nghiệp:

alembic revision --autogenerate -m "Initial sync"
alembic upgrade head


4. **Truy cập Documentation:**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
