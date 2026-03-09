FROM python:3.10-slim

WORKDIR /app
COPY pyproject.toml uv.lock .
RUN pip install uv
RUN uv sync --frozen
COPY . .

CMD ["uv", "run", "python", "-m", "main"]