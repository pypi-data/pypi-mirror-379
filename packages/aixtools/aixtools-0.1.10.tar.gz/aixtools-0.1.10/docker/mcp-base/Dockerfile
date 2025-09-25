FROM ubuntu:22.04

RUN apt-get -y update && \
    apt-get -y install ca-certificates curl gcc git libcap2-bin sudo
RUN mv /usr/bin/sudo /usr/sbin

# Add Zscaler CA certificate
COPY ./zscaler.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Install `uv` Python package manager
RUN bash -o pipefail -c "curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=/usr/local/bin sh"

# Add a user matching the sandbox user so that the files and folders created by the MCP server
# are writable by the user in the sandbox containers (UID=1000 must match!)
ENV USER=mcp_user
RUN useradd -m -s /bin/bash -u 1000 ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER} && chmod 0440 /etc/sudoers.d/${USER}
USER ${USER}

# Build argument: GITHUB_PAT (optional)
# If provided, this GitHub Personal Access Token will be used to authenticate git
# operations against github.com during the build. This is useful for accessing private repositories such as `aixtools`.
# If not set, git will use unauthenticated access (public repositories only).
ARG GITHUB_PAT
RUN if [ -n "$GITHUB_PAT" ]; then \
    git config --global url."https://x-access-token:${GITHUB_PAT}@github.com/".insteadOf "https://github.com/"; \
    fi

WORKDIR /app
RUN mkdir data
