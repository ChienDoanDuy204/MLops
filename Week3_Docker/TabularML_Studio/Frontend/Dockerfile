# Tạo môi trường base
FROM python:3.11.4-slim 
# Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# Sao chép file requirements.txt vào thư mục làm việc
COPY requirements.txt /app/requirements.txt
# Cài đặt các thư viện cần thiết từ requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# Sao chép toàn bộ thư mục hiện tại vào thư mục làm việc bên trong container
COPY . /app
# Mở cổng 3000 để ứng dụng có thể truy cập từ bên ngoài container
EXPOSE 3000
# Chạy ứng dụng khi container được khởi động
CMD ["streamlit", "run", "App.py","--server.address=0.0.0.0","--server.port=3000"]
