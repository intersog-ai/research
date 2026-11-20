# Agent lab container: agents get a shell here, never on the host.
FROM node:22-bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip python3-venv curl sqlite3 ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && python3 -m pip install --break-system-packages pytest \
 && npm install -g @anthropic-ai/claude-code
WORKDIR /lab
COPY . /lab
ENV LAB_IN_CONTAINER=1
CMD ["bash"]
