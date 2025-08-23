# IB Gateway + IBC Dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y openjdk-17-jre wget curl xvfb && \
    useradd -ms /bin/bash ibkr

WORKDIR /opt/ibkr

# Download IB Gateway and IBC
RUN wget https://download2.interactivebrokers.com/ibg/IBGateway-latest-linux-x64.sh -O ibgateway.sh && \
    chmod +x ibgateway.sh && \
    wget https://github.com/IbcAlpha/IBC/releases/download/v3.13.0/IBC.zip -O IBC.zip && \
    unzip IBC.zip -d IBC && \
    rm IBC.zip

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER ibkr

ENTRYPOINT ["/entrypoint.sh"]
