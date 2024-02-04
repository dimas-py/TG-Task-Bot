FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .


RUN echo "#!/bin/bash" >> start.sh
RUN echo "python bot.py &" >> start.sh
RUN echo "python app.py" >> start.sh
RUN chmod +x start.sh


CMD ["bash", "/app/start.sh"]