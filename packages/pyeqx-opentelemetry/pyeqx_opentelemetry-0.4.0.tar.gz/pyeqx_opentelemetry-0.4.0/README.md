# esbm-dis-dfts-pyeqx-opentelemetry

This is part of pyeqx with opentelemetry packages. (package: `pyeqx-opentelemetry`)

## Pre-requisites

Python: `3.12`

Dependencies:

- opentelemetry-api
- opentelemetry-sdk
- opentelemetry-exporter-otlp
- opentelemetry-exporter-prometheus
- opentelemetry-instrumentation
- azure-monitor-opentelemetry-exporter

```bash
# setup virtual env
python3.12 -m venv .venv

# activate virtual env
source .venv/bin/activate

# install dependencies
pip install opentelemetry-api opentelemetry-distro opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-exporter-prometheus azure-monitor-opentelemetry-exporter==1.0.0b42

# or
pip install -e .[dev]

# execute opentelemetry bootstrap install (to auto-detect instrumentation and install)
opentelemetry-bootstrap -a install

# install dependencies (If you want to publish)
pip install twine
```

### Environement variables

Create `.env` file with content below

```bash
OTEL_TRACES_EXPORTER=otlp
OTEL_METRICS_EXPORTER=otlp
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

OTEL_PYTHON_LOG_CORRELATION=true
OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
```

## Tests

By default, just using `pytest` will run the test with coverage.

```bash
pytest
```

To execute unit test run this command at root of the project

```bash
python3 -m unittest discover test -p "**.py"

# or

pytest test/ --cov=src --cov-report=term-missing
```

To execute test with coverage

```bash
pytest test/ --cov=src
```

> [!NOTE] Additional commands for pytest
> to generate coverage report in another format, you can use this command `pytest --cov-report=xml:coverage/coverage.xml`
> to enable watch mode and rerun test when file changes, you can use this command `pytest --looponfail`
> to run and with stdout output, you can use this command `pytest -s`

## Build

```bash
python3 -m build
```

## Publish

To pypi

```bash
python3 -m twine upload --config-file .pypirc dist/*
```

## Remark
