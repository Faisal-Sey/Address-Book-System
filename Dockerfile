FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /address_book_main/address_book_main/
COPY requirements.txt /address_book_main/address_book_main/
RUN pip install -r requirements.txt
COPY . /address_book_main/