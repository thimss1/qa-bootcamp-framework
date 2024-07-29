FROM python:3.11

# change timezone of the container to be PST
RUN ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
RUN echo "America/Los_Angeles" > /etc/timezone


RUN mkdir /automation
WORKDIR /automation

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt


COPY . /automation



WORKDIR ../automation/ssqatest

ENV HTTP_HOST=127.0.0.1

# set the entrypoint to run the application
# ENTRYPOINT ["pwd"]
ENTRYPOINT ["entrypoint.sh"]

#ENTRYPOINT ["python3", "-m", "pytest"]
# ENTRYPOINT ["python3", "-m", "pytest", "tests"]

# set the default arguments to run the application in development mode
# CMD ["--debug"]
# RUN python3 -m pytest
# RUN python3 -m pytest
# CMD ['python3','-m', 'pytest', './tests']