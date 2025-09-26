ARG BASE=nvidia/cuda:12.8.1-base-ubuntu24.04
FROM ${BASE}

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends \
    gcc g++ make python3 python3-dev \
    espeak-ng libsndfile1-dev libc-dev && \
  rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.8.15 /uv /uvx /bin/
ENV UV_NO_CACHE=1 \
    UV_TORCH_BACKEND=auto

RUN uv venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Install dependencies first for better caching
COPY pyproject.toml /app
RUN uv pip install -r pyproject.toml --extra all

# Copy the rest of the application
COPY . /app

# Install the project
RUN uv pip install -e .

ENTRYPOINT ["tts"]
CMD ["--help"]
