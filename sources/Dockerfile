# Gunakan Python sebagai base image
FROM python:3.9

# Set direktori kerja di dalam container
WORKDIR /sources

# Salin file ke dalam container
COPY . .

# Instal dependensi
RUN pip install -r requirements.txt

# Ekspos port Flask
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]

