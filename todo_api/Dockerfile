FROM python:3.8-alpine
COPY . /todo_api
WORKDIR /todo_api
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
