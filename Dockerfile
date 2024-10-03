FROM python

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5432

COPY . .

CMD ["pyhton", "app.py"]