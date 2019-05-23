FROM joyzoursky/python-chromedriver:3.6-xvfb
RUN mkdir /project/
WORKDIR /project
ADD ./project /project
RUN pip install -r requirements.txt
#docker build -t maxiplux/selenium-webdrive:3.6