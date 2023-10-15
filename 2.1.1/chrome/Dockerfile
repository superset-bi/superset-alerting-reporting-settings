FROM apache/superset:2.1.1

USER root

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
          libnss3 \
          libdbus-glib-1-2 \
          libgtk-3-0 \
          libx11-xcb1 \
          libasound2 \
          libxtst6 \
          wget

RUN apt-get update && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb && \
    rm -f google-chrome-stable_current_amd64.deb

RUN wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin && \
    chmod 755 /usr/bin/chromedriver && \
    rm -f chromedriver_linux64.zip

RUN pip install --no-cache gevent psycopg2 redis

USER superset