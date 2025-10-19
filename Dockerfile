# Build Stage Stage 1

FROM python:3.12.12-slim AS builder

WORKDIR /app

# Install build dependencies 

RUN apt-get update && apt-get install -y build-essential libpq-dev

# Copy requirements 

COPY app/requirements.txt .

RUN pip install --prefix=/install -r requirements.txt


# Stage 2 : Final

FROM python:3.12.12-slim

WORKDIR /app

# copy only installed packages form builder 

COPY --from=builder /install /usr/local

#Cpy app code

COPY app/ .

EXPOSE 5000

CMD ["python" , "app.py"]

