FROM python:3

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /star_char

EXPOSE 8080

CMD   ["python","app.py"]





