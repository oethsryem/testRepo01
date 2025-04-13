FROM python:3.12
WORKDIR /usr/local/app/testrepo01

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY main.py ./main.py
COPY send_mail.py ./send_mail.py
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
CMD ["flask", "--app", "main.py" "run"]