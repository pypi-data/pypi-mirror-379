"""
Logging via Logfire with OpenTelemetry support.

Auto-instrumentation is applied for Pydantic AI and Redis, and `prima.logger.logfire`
is available for use like `prima.logger.logfire.instrument_fastapi(app)` in app.py.
"""

import os
from urllib.parse import urlparse, urlunparse

import httpx
import logfire

from tracapp.settings import PrimaSettings


_prima_settings = PrimaSettings()

# because I keep forgetting where the OpenTelemetry alternative backend logfire documentation is:
# https://logfire.pydantic.dev/docs/how-to-guides/alternative-backends/

# It appears that PrimaSettings.otel_exporter_otlp_endpoint is not getting populated in
# os.environ thus not triggering logfire to send to that endpoint. There is an explicit
# export shown in
# https://github.com/pydantic/logfire/blob/main/docs/how-to-guides/otel-collector/otel-collector-overview.md#back-up-data-in-aws-s3
# so we'll do that before calling logfire.configure()


def _configure_otel_if_reachable(endpoint: str | None) -> tuple[logfire.LevelName, str]:
    """Check if OTLP endpoint is reachable, and if so, configure it in os.environ for logfire."""
    if not endpoint:
        return "debug", "No OTLP endpoint configured, skipping OTLP trace export"

    parsed = urlparse(endpoint)
    parsed = parsed._replace(netloc=f"{parsed.hostname}:13133")
    health = urlunparse(parsed)  # pyright: ignore[reportReturnType] stdlib is so poorly typed

    try:
        response = httpx.get(health, timeout=2.0)
        response.raise_for_status()
    except Exception:
        return "error", f"Failed to reach OTLP endpoint {health}, not exporting OTLP traces"

    # if we got here, the health check passed, so set the env var for logfire
    os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = endpoint
    return "debug", f"OTLP endpoint {health} is reachable, exporting OTLP traces"


otlp_level, otlp_msg = _configure_otel_if_reachable(_prima_settings.otel_exporter_otlp_endpoint)

log = logfire.configure(
    send_to_logfire="if-token-present",
    token=_prima_settings.logfire_token,
    service_name=_prima_settings.prima_package_name,
    distributed_tracing=True,
)
logfire.instrument_pydantic_ai()
logfire.instrument_celery()
logfire.instrument_httpx(capture_all=True)

log.log(otlp_level, otlp_msg)
