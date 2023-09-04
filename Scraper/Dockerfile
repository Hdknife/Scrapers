FROM ubuntu


RUN apt-get update && \
    apt-get install -y python3 python3-pip
    
RUN pip3 install requests
RUN pip3 install beautifulsoup4




WORKDIR /app

COPY . .


CMD ["python3", "main.py"]
