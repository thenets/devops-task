FROM alpine:3.8

ENV USER=kratos
ENV USER_HOME=/home/${USER}
ENV APP_DIR=/app

RUN set -x \
    # Install OS dependencies
    && apk add py3-virtualenv python3-dev py3-psutil gcc build-base linux-headers \
    # Install tools
    && apk add htop nano curl wget bash git \
    # Add user
    && mkdir -p ${USER_HOME} \
    && adduser -D -u 1000 -s /bin/bash ${USER} \
    && chown -R 1000.1000 ${USER_HOME} \
    && echo 'export PS1="\e[1m\e[91mGodOfWar\e[39m:\e[96m\w\e[0m# "' > /root/.bashrc \
    && echo 'export PS1="\e[1m\e[32m\\u\e[39m@\e[34masgard\e[39m:\e[96m\w\e[0m$ "' > ${USER_HOME}/.bashrc \
    # Fix permissions
    && mkdir -p ${APP_DIR} \
    && chown 1000:1000 ${APP_DIR}

WORKDIR ${APP_DIR}

USER ${USER}

# Add project
COPY --chown=1000:1000 ./metrics ${APP_DIR}/metrics
COPY --chown=1000:1000 requirements.txt ${APP_DIR}/
COPY --chown=1000:1000 entrypoint.sh ${APP_DIR}/

RUN set -x \
    # Create virtualenv and install libs
    && virtualenv -p python3 venv \
    && . venv/bin/activate \
    && pip install -r requirements.txt \
    # Set permissions
    && chmod +x entrypoint.sh

EXPOSE 5000

CMD ["./entrypoint.sh"]