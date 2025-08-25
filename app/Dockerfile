FROM python:3.10-slim

#determinde the folder in the container to operate the app
WORKDIR /app
COPY requirements.txt .

# تثبيت الباكجات المطلوبة
RUN pip install --upgrade pip
RUN pip install  -r requirements.txt

# then copy the rest of the app
COPY . .
# فتح البورت 8000
EXPOSE 5000

# أمر التشغيل
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
