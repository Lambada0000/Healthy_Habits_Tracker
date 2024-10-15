FROM python:3.12-slim

WORKDIR /app

# Копируем только файл с зависимостями
COPY requirements.txt .

# Устанавливаем pip и зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash"]