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
          unzip \
          wget

RUN apt-get update && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb && \
    rm -f google-chrome-stable_current_amd64.deb

# refer https://googlechromelabs.github.io/chrome-for-testing/
# superset issue https://github.com/apache/superset/issues/25284
RUN export CHROMEDRIVER_VERSION=$(curl --silent https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE) && \
    wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/bin/ && \
    chmod 755 /usr/bin/chromedriver && \ 
    rm -f chromedriver-linux64.zip && \
    rm -f -r chromedriver-linux64

RUN pip install --no-cache gevent psycopg2 redis

USER superset