FROM mcr.microsoft.com/devcontainers/base:bookworm

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y --no-install-recommends sudo curl wget ca-certificates ffmpeg \
    && apt clean \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

USER vscode

RUN <<EOT
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
    echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
EOT

RUN <<EOT
    curl -LsSf https://astral.sh/ruff/install.sh | sh
    echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
    echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
EOT

