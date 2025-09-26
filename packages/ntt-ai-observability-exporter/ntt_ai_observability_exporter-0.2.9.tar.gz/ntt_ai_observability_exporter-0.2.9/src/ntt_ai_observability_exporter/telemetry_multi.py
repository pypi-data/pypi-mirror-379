# Multi-Application Insights telemetry setup using OpenTelemetry and Azure Monitor exporters.
# Sends the same traces, logs, and metrics to multiple Application Insights resources.
#
# GenAI content recording (Azure AI Foundry):
# - By default, this enables content recording (prompts/responses) with mode="all"
# - It also enables Semantic Kernel OTEL diagnostics by default
# - You can turn either off via configure_multi_azure_monitor(...) flags
#
# Requirements (install what you use):
# - opentelemetry-sdk==1.36.0
# - opentelemetry-api==1.36.0
# - opentelemetry-instrumentation-requests
# - azure-monitor-opentelemetry-exporter>=1.0.0
# - azure-core
# - requests
# Optional for Azure AI Foundry GenAI spans with content:
# - azure-ai-inference (and/or azure-ai-agents)
# Optional if you use OpenAI python client instead of azure.ai.inference:
# - opentelemetry-instrumentation-openai

import logging
import os
import time
from typing import Dict, List, Optional

# Set up logger
logger = logging.getLogger("ntt_ai_observability")

from opentelemetry import trace, metrics
from opentelemetry.metrics import set_meter_provider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.metrics.view import View, DropAggregation
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import set_tracer_provider
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from .utilities import get_config, validate_telemetry_config
from azure.monitor.opentelemetry.exporter import (
    AzureMonitorTraceExporter,
    AzureMonitorMetricExporter,
    AzureMonitorLogExporter,
    ApplicationInsightsSampler,
)

_logger = logging.getLogger("multi_ai.telemetry")
if not _logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    _logger.addHandler(_handler)
_logger.setLevel(logging.INFO)


def enable_genai_content_recording(enabled: bool = True, mode: str = "all") -> None:
    """
    Enable Azure GenAI content recording. Must be called BEFORE importing azure.ai.* clients
    or Semantic Kernel to ensure the SDK reads these environment variables.

    Args:
        enabled: True to enable content recording
        mode: "all" to include prompts and responses; "sanitized" to redact sensitive content
              Any other value may be ignored by the SDK.
    """
    os.environ["AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED"] = "true" if enabled else "false"
    # Normalize mode to accepted values
    mode_normalized = (mode or "").strip().lower()
    if mode_normalized in ("all", "sanitized", "sanitize", "redacted", "redact"):
        # standardize to values commonly recognized: "all" or "sanitized"
        if mode_normalized in ("sanitize", "redacted", "redact"):
            mode_normalized = "sanitized"
    else:
        # fallback to sanitized if given invalid input (e.g., "true")
        mode_normalized = "sanitized"
    os.environ["AZURE_TRACING_GEN_AI_CONTENT_RECORDING_MODE"] = mode_normalized
    # Optional toggle some customers use; harmless to set
    os.environ.setdefault("ENABLE_AZURE_MONITOR_TRACING", "true")

    _logger.info("GenAI content recording enabled=%s mode=%s", enabled, mode_normalized)


def enable_semantic_kernel_otel(enabled: bool = True) -> None:
    """
    Enable/disable Semantic Kernel OTEL emission (prompts/steps).
    Call BEFORE importing semantic_kernel.
    """
    os.environ["SEMANTICKERNEL_EXPERIMENTAL_GENAI_ENABLE_OTEL_DIAGNOSTICS"] = "true" if enabled else "false"
    os.environ["SEMANTICKERNEL_EXPERIMENTAL_GENAI_ENABLE_OTEL_DIAGNOSTICS_SENSITIVE"] = "true" if enabled else "false"


def build_default_resource(
    service_name: str,
    service_instance_id: str,
    service_version: Optional[str] = None,
    extra_attributes: Optional[Dict[str, str]] = None,
) -> Resource:
    """
    Create an OpenTelemetry Resource with standardized service identification attributes.
    
    Resource represents the entity producing telemetry data (your application/service).
    These attributes appear in ALL telemetry (traces, logs, metrics) and help identify
    and organize data in Application Insights.
    
    OpenTelemetry Resource Attributes:
    - service.name: Logical name of the service (e.g., "customer-portal", "payment-api")
    - service.instance.id: Unique identifier for this instance (e.g., hostname, pod name)
    - service.version: Version of the service code (e.g., "1.2.3", git commit hash)
    
    In Application Insights, these appear as:
    - Cloud role name (service.name)
    - Cloud role instance (service.instance.id)
    - Custom dimensions for version and extra attributes
    
    Args:
        service_name: Logical name identifying your service across all instances
        service_instance_id: Unique ID for this specific running instance
        service_version: Optional version string for deployment tracking
        extra_attributes: Additional key-value pairs for custom classification
    
    Returns:
        Resource: OpenTelemetry Resource object with all specified attributes
    """
    # Core service identification attributes (required by OpenTelemetry spec)
    attrs: Dict[str, str] = {
        "service.name": service_name,        # Logical service identifier
        "service.instance.id": service_instance_id,  # Unique instance identifier
    }
    
    # Optional version information for deployment tracking
    if service_version:
        attrs["service.version"] = service_version
    
    # Custom attributes for additional service classification
    if extra_attributes:
        attrs.update(extra_attributes)
    
    # Resource.create(): Creates immutable Resource with semantic conventions
    # - Validates attribute names against OpenTelemetry standards
    # - Merges with auto-detected resource attributes (host, OS, etc.)
    # - Thread-safe and efficient for high-throughput applications
    return Resource.create(attrs)


def default_views() -> List[View]:
    """
    Create OpenTelemetry metric Views that control which metrics are collected and exported.
    
    Views are powerful filtering and aggregation rules that determine:
    1. Which metrics are collected vs. dropped (performance optimization)
    2. How metrics are aggregated (histogram buckets, etc.)
    3. Which dimensions/labels are preserved vs. dropped
    
    This configuration uses a "deny-by-default, allow-specific" strategy:
    - Drops ALL metrics by default (prevents metric explosion)
    - Selectively enables metrics from important namespaces
    - Optimizes for Azure Application Insights performance
    
    Strategy Benefits:
    - Prevents overwhelming Application Insights with irrelevant metrics
    - Reduces costs (fewer custom metrics ingested)
    - Improves query performance in Azure portal
    - Focuses on actionable telemetry data
    
    Returns:
        List[View]: Ordered list of metric filtering rules
    """
    return [
        # DENY-ALL rule: Drop everything by default
        # DropAggregation: Completely discards metric data (zero overhead)
        # instrument_name="*": Matches all metric instruments
        # This MUST be first rule to establish default deny behavior
        View(instrument_name="*", aggregation=DropAggregation()),
        
        # ALLOW rules: Selectively enable important metric namespaces
        # These rules override the deny-all rule for specific patterns
        
        # Semantic Kernel AI orchestration metrics
        # - Agent execution times, step counts, token usage
        # - LLM call latencies and success rates
        View(instrument_name="semantic_kernel*"),
        
        # Azure SDK and service metrics
        # - HTTP request durations, error rates
        # - Authentication success/failure rates
        # - Service-specific performance counters
        View(instrument_name="azure.*"),
        
        # HTTP client and server metrics
        # - Request/response times, status codes
        # - Connection pool statistics
        # - Network-level performance data
        View(instrument_name="http.*"),
        
        # AI/ML service metrics (OpenAI, Azure AI, etc.)
        # - Model inference times, token counts
        # - Content safety check results
        # - AI service availability metrics
        View(instrument_name="ai.*"),
        
        # Web framework metrics: Track incoming HTTP requests
        View(instrument_name="fastapi*"),     # FastAPI: request counts, response times
        View(instrument_name="flask*"),       # Flask: route metrics, template render times
        View(instrument_name="django*"),      # Django: view execution, middleware metrics
        View(instrument_name="asgi*"),        # ASGI servers: connection counts, throughput
        View(instrument_name="wsgi*"),        # WSGI servers: worker metrics, queue depths
    ]


def _attach_logging_handlers(
    logger_provider: LoggerProvider,
    logger_names: Optional[List[str]] = None
) -> None:
    """
    Attach OpenTelemetry LoggingHandlers to Python loggers for comprehensive log capture.
    
    This function bridges Python's standard logging system with OpenTelemetry, ensuring that
    log records from libraries like Semantic Kernel, Azure SDKs, and application code are
    captured and sent to Application Insights.
    
    Architecture:
    - Creates LoggingHandler instances that convert Python LogRecord to OpenTelemetry LogRecord
    - Attaches handlers to both root logger (catches everything) and specific loggers
    - Uses propagate=False on specific loggers to prevent duplicate log records
    - No filtering is applied - all log levels are captured and exported
    
    Args:
        logger_provider: The OpenTelemetry LoggerProvider that will process log records
        logger_names: List of specific logger names to instrument (e.g., ["semantic_kernel", "azure"])
    
    Key Components:
    - LoggingHandler: OpenTelemetry class that converts Python logs to OTEL format
    - set_logger_provider: Makes the provider globally available to no-arg LoggingHandler()
    - Root logger strategy: Catches all logs that bubble up from child loggers
    - Specific logger strategy: Direct capture from important libraries
    """
    from opentelemetry._logs import set_logger_provider
    from opentelemetry.sdk._logs import LoggingHandler

    # set_logger_provider: Makes the LoggerProvider globally available
    # - Allows LoggingHandler() to work without explicit provider argument
    # - Required for the no-argument constructor LoggingHandler() to function
    # - Establishes the global logging pipeline for OpenTelemetry
    set_logger_provider(logger_provider)

    # Default target loggers (you can override via logger_names)
    targets = logger_names or [
        "semantic_kernel",      # Microsoft Semantic Kernel AI orchestration logs
        "azure",               # All Azure SDK logs (azure.core, azure.ai, etc.)
        "azure.core",          # Azure SDK core library (HTTP requests, auth, etc.)
        "azure.ai",            # Azure AI services (OpenAI, Cognitive Services, etc.)
        "azure.ai.projects",   # Azure AI Foundry project operations
    ]

    def _has_otel_handler(lg: logging.Logger) -> bool:
        """
        Check if a logger already has an OpenTelemetry LoggingHandler attached.
        Prevents duplicate handlers that would cause duplicate log records.
        """
        try:
            from opentelemetry.sdk._logs import LoggingHandler as RealLoggingHandler
            return any(isinstance(h, RealLoggingHandler) for h in lg.handlers)
        except ImportError:
            # Fallback: If we can't import LoggingHandler, check by class name
            return any(h.__class__.__name__ == 'LoggingHandler' for h in lg.handlers)

    # Strategy 1: Root logger with unfiltered handler
    # - Catches all log records that bubble up from child loggers
    # - Ensures no logs are missed due to logger hierarchy issues
    # - Acts as a safety net for any logs not caught by specific loggers
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    if not _has_otel_handler(root):
        # LoggingHandler(): No filtering - sends all log levels to OpenTelemetry
        # - Converts Python LogRecord to OpenTelemetry LogRecord format
        # - Preserves log level, message, timestamp, and exception information
        # - Adds trace context if current request/operation has active spans
        root.addHandler(LoggingHandler())  # unfiltered

    # Strategy 2: Specific logger handlers with propagation control
    # - Direct attachment to important library loggers
    # - Guarantees capture even if libraries set propagate=False later
    # - Prevents duplicate records by setting propagate=False after attachment
    for name in targets:
        lg = logging.getLogger(name)
        lg.setLevel(logging.INFO)
        if not _has_otel_handler(lg):
            # Each target logger gets its own LoggingHandler
            # - Ensures direct capture of logs from this specific logger
            # - Handles cases where library code might disable propagation
            lg.addHandler(LoggingHandler())  # unfiltered
        
        # propagate=False: Prevents logs from bubbling up to parent loggers
        # - Avoids duplicate log records (since we have both root and specific handlers)
        # - Each log record is captured exactly once
        # - Maintains clean separation between different logging sources
        lg.propagate = False  # prevent duplicate records (logger + root)

            
def _install_instrumentations() -> None:
    """
    Automatically detect and instrument all available libraries for comprehensive telemetry.
    
    This function implements an "auto-discovery" pattern that:
    1. Checks sys.modules to see what libraries are already imported
    2. Attempts to install instrumentation only for detected libraries
    3. Handles missing instrumentation packages gracefully
    4. Provides clear logging for troubleshooting
    
    Instrumentation Categories:
    
    🌐 HTTP & Network:
    - requests: HTTP client calls (used by Azure SDKs)
    - azure-core: Azure SDK tracing integration
    
    🗄️ Database & Storage:
    - PostgreSQL (psycopg2): Database queries, connection pooling
    - SQL Server (pyodbc): T-SQL execution, stored procedures
    - MySQL (pymysql): Query performance, transaction tracing
    - SQLite (sqlite3): File-based database operations
    - Redis: Cache operations, pub/sub messaging
    - MongoDB (pymongo): Document operations, aggregations
    - SQLAlchemy: ORM queries, relationship loading
    
    🌍 Web Frameworks (Incoming HTTP):
    - FastAPI: Route handling, middleware execution
    - Flask: Request processing, template rendering
    - Django: View execution, middleware chain
    - ASGI: Async server request/response cycles
    - WSGI: Traditional server request handling
    
    🤖 AI & ML Services:
    - azure.ai.inference: Azure AI Foundry model calls with content
    - azure.ai.agents: AI agent orchestration and workflows
    - OpenAI: Direct OpenAI API calls (alternative to Azure AI)
    
    Instrumentation Strategy:
    - Automatic Detection: Uses sys.modules to avoid instrumenting unused libraries
    - Graceful Degradation: Missing instrumentation packages don't break the app
    - No-Op Safety: Checks is_instrumented_by_opentelemetry to avoid double-instrumentation
    - Consistent Logging: DEBUG for expected issues, WARNING for real problems
    
    This function is called automatically by configure_telemetry_azure_monitor().
    """
    import sys
    
    # ===== AZURE SDK CORE INTEGRATION =====
    # Enable OpenTelemetry spans for all Azure SDK HTTP calls
    # This is foundational - enables tracing for Azure AI, Storage, KeyVault, etc.
    try:
        from azure.core.settings import settings
        from azure.core.tracing.ext.opentelemetry_span import OpenTelemetrySpan

        # settings.tracing_implementation: Global Azure SDK tracing backend
        # - Replaces Azure SDK's default no-op tracing with OpenTelemetry
        # - Enables automatic span creation for all Azure service calls
        # - Adds HTTP headers for distributed tracing across service boundaries
        settings.tracing_implementation = OpenTelemetrySpan
        _logger.info("Enabled azure-core OpenTelemetry tracing")
    except Exception as ex:
        _logger.warning("azure-core tracing not enabled: %s", ex)

    # ===== HTTP CLIENT INSTRUMENTATION =====
    # Instrument HTTP libraries commonly used by applications and Azure SDKs
    try:
        from opentelemetry.instrumentation.requests import RequestsInstrumentor

        # RequestsInstrumentor: Automatic HTTP client tracing
        # - Creates spans for all requests.get/post/etc calls
        # - Captures HTTP method, URL, status codes, timing
        # - Propagates trace context to downstream services
        RequestsInstrumentor().instrument()
        _logger.info("Instrumented requests")
    except Exception as ex:
        _logger.warning("requests instrumentation failed: %s", ex)

    # ===== DATABASE INSTRUMENTATION =====
    # Comprehensive database telemetry for all major database systems
    # Pattern: Check sys.modules → Import instrumentor → Check not already instrumented → Instrument
    
    # PostgreSQL Database (psycopg2 driver)
    # Traces: SELECT, INSERT, UPDATE, DELETE queries with execution times
    # Metrics: Connection pool usage, query latency distributions  
    # Context: Automatic trace correlation between HTTP requests and DB queries
    if 'psycopg2' in sys.modules:
        try:
            from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
            # is_instrumented_by_opentelemetry: Prevents double-instrumentation
            # - Multiple calls to instrument() could create duplicate spans
            # - Safety check ensures clean instrumentation lifecycle
            if not Psycopg2Instrumentor().is_instrumented_by_opentelemetry:
                Psycopg2Instrumentor().instrument()
                _logger.info("✓ Instrumented psycopg2 - PostgreSQL database calls will be traced")
        except ImportError:
            # ImportError: Expected when opentelemetry-instrumentation-psycopg2 not installed
            # This is normal - not all applications use every database type
            _logger.debug("psycopg2 instrumentation not available. Install: pip install opentelemetry-instrumentation-psycopg2")
        except Exception as ex:
            # Other exceptions: Real problems that need attention (config errors, etc.)
            _logger.warning("psycopg2 instrumentation failed: %s", ex)
    
    # SQL Server Database (pyodbc driver) 
    # Traces: T-SQL queries, stored procedures, bulk operations
    # Spans include: SQL text (sanitized), parameters, row counts
    if 'pyodbc' in sys.modules:
        try:
            from opentelemetry.instrumentation.pyodbc import PyODBCInstrumentor
            if not PyODBCInstrumentor().is_instrumented_by_opentelemetry:
                PyODBCInstrumentor().instrument()
                _logger.info("✓ Instrumented pyodbc - SQL Server database calls will be traced")
        except ImportError:
            _logger.debug("pyodbc instrumentation not available. Install: pip install opentelemetry-instrumentation-pyodbc")
        except Exception as ex:
            _logger.warning("pyodbc instrumentation failed: %s", ex)
            
    # MySQL (pymysql, MySQLdb)
    if 'pymysql' in sys.modules:
        try:
            from opentelemetry.instrumentation.pymysql import PyMySQLInstrumentor
            if not PyMySQLInstrumentor().is_instrumented_by_opentelemetry:
                PyMySQLInstrumentor().instrument()
                _logger.info("✓ Instrumented pymysql - MySQL database calls will be traced")
        except ImportError:
            _logger.debug("pymysql instrumentation not available. Install: pip install opentelemetry-instrumentation-pymysql")
        except Exception as ex:
            _logger.warning("pymysql instrumentation failed: %s", ex)
            
    # SQLite (sqlite3 - built-in)
    if 'sqlite3' in sys.modules:
        try:
            from opentelemetry.instrumentation.sqlite3 import SQLite3Instrumentor
            if not SQLite3Instrumentor().is_instrumented_by_opentelemetry:
                SQLite3Instrumentor().instrument()
                _logger.info("✓ Instrumented sqlite3 - SQLite database calls will be traced")
        except ImportError:
            _logger.debug("sqlite3 instrumentation not available. Install: pip install opentelemetry-instrumentation-sqlite3")
        except Exception as ex:
            _logger.warning("sqlite3 instrumentation failed: %s", ex)
            
    # SQLAlchemy (ORM)
    if 'sqlalchemy' in sys.modules:
        try:
            from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
            if not SQLAlchemyInstrumentor().is_instrumented_by_opentelemetry:
                SQLAlchemyInstrumentor().instrument()
                _logger.info("✓ Instrumented SQLAlchemy - ORM database calls will be traced")
        except ImportError:
            _logger.debug("sqlalchemy instrumentation not available. Install: pip install opentelemetry-instrumentation-sqlalchemy")
        except Exception as ex:
            _logger.warning("sqlalchemy instrumentation failed: %s", ex)
            
    # Redis
    if 'redis' in sys.modules:
        try:
            from opentelemetry.instrumentation.redis import RedisInstrumentor
            if not RedisInstrumentor().is_instrumented_by_opentelemetry:
                RedisInstrumentor().instrument()
                _logger.info("✓ Instrumented redis - Redis cache calls will be traced")
        except ImportError:
            _logger.debug("redis instrumentation not available. Install: pip install opentelemetry-instrumentation-redis")
        except Exception as ex:
            _logger.warning("redis instrumentation failed: %s", ex)
            
    # MongoDB (pymongo)
    if 'pymongo' in sys.modules:
        try:
            from opentelemetry.instrumentation.pymongo import PymongoInstrumentor
            if not PymongoInstrumentor().is_instrumented_by_opentelemetry:
                PymongoInstrumentor().instrument()
                _logger.info("✓ Instrumented pymongo - MongoDB database calls will be traced")
        except ImportError:
            _logger.debug("pymongo instrumentation not available. Install: pip install opentelemetry-instrumentation-pymongo")
        except Exception as ex:
            _logger.warning("pymongo instrumentation failed: %s", ex)

    # Web Framework instrumentation - instrument incoming HTTP requests
    # FastAPI instrumentation
    if 'fastapi' in sys.modules:
        try:
            from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
            if not FastAPIInstrumentor().is_instrumented_by_opentelemetry:
                FastAPIInstrumentor().instrument()
                _logger.info("✓ Instrumented FastAPI - incoming HTTP requests will be traced")
        except ImportError:
            _logger.debug("FastAPI instrumentation not available. Install: pip install opentelemetry-instrumentation-fastapi")
        except Exception as ex:
            _logger.warning("FastAPI instrumentation failed: %s", ex)
    
    # Flask instrumentation
    if 'flask' in sys.modules:
        try:
            from opentelemetry.instrumentation.flask import FlaskInstrumentor
            if not FlaskInstrumentor().is_instrumented_by_opentelemetry:
                FlaskInstrumentor().instrument()
                _logger.info("✓ Instrumented Flask - incoming HTTP requests will be traced")
        except ImportError:
            _logger.debug("Flask instrumentation not available. Install: pip install opentelemetry-instrumentation-flask")
        except Exception as ex:
            _logger.warning("Flask instrumentation failed: %s", ex)
    
    # Django instrumentation
    if 'django' in sys.modules:
        try:
            from opentelemetry.instrumentation.django import DjangoInstrumentor
            if not DjangoInstrumentor().is_instrumented_by_opentelemetry:
                DjangoInstrumentor().instrument()
                _logger.info("✓ Instrumented Django - incoming HTTP requests will be traced")
        except ImportError:
            _logger.debug("Django instrumentation not available. Install: pip install opentelemetry-instrumentation-django")
        except Exception as ex:
            _logger.warning("Django instrumentation failed: %s", ex)
    
    # ASGI instrumentation (for modern async frameworks)
    if any(framework in sys.modules for framework in ['starlette', 'uvicorn', 'hypercorn']):
        try:
            from opentelemetry.instrumentation.asgi import ASGIInstrumentor
            if not ASGIInstrumentor().is_instrumented_by_opentelemetry:
                ASGIInstrumentor().instrument()
                _logger.info("✓ Instrumented ASGI - async web server requests will be traced")
        except ImportError:
            _logger.debug("ASGI instrumentation not available. Install: pip install opentelemetry-instrumentation-asgi")
        except Exception as ex:
            _logger.warning("ASGI instrumentation failed: %s", ex)
    
    # WSGI instrumentation (for traditional frameworks)
    if any(framework in sys.modules for framework in ['werkzeug', 'gunicorn']):
        try:
            from opentelemetry.instrumentation.wsgi import WSGIInstrumentor
            if not WSGIInstrumentor().is_instrumented_by_opentelemetry:
                WSGIInstrumentor().instrument()
                _logger.info("✓ Instrumented WSGI - web server requests will be traced")
        except ImportError:
            _logger.debug("WSGI instrumentation not available. Install: pip install opentelemetry-instrumentation-wsgi")
        except Exception as ex:
            _logger.warning("WSGI instrumentation failed: %s", ex)

    # Individual instrumentations for all libraries
    _logger.info("Instrumenting all available libraries individually")
    
    # Azure AI Foundry: instrument azure.ai.inference for GenAI spans with content
    if 'azure.ai.inference' in sys.modules:
        try:
            from azure.ai.inference.tracing import AIInferenceInstrumentor  # type: ignore
            AIInferenceInstrumentor().instrument()
            _logger.info("✓ Instrumented azure.ai.inference")
        except ImportError:
            _logger.debug("azure.ai.inference instrumentation not available. Install: pip install azure-ai-inference[tracing]")
        except Exception as ex:
            _logger.warning("azure.ai.inference instrumentation failed: %s", ex)

    # Azure AI Agents (optional) - only if already imported
    if 'azure.ai.agents' in sys.modules:
        try:
            from azure.ai.agents.telemetry import AIAgentsInstrumentor  # type: ignore
            AIAgentsInstrumentor().instrument()
            _logger.info("✓ Instrumented azure.ai.agents")
        except ImportError:
            _logger.debug("azure.ai.agents instrumentation not available. Install: pip install azure-ai-agents[telemetry]")
        except Exception as ex:
            _logger.warning("azure.ai.agents instrumentation failed: %s", ex)

    # OpenAI instrumentation - automatically instrument if OpenAI is imported
    if 'openai' in sys.modules:
        try:
            from opentelemetry.instrumentation.openai import OpenAIInstrumentor  # type: ignore
            if not OpenAIInstrumentor().is_instrumented_by_opentelemetry:
                OpenAIInstrumentor().instrument()
                _logger.info("✓ Instrumented OpenAI python client")
        except ImportError:
            _logger.debug("OpenAI instrumentation not available")
        except Exception as ex:
            _logger.warning("OpenAI instrumentation failed: %s", ex)
            
    # Note: LangchainInstrumentor removed - Azure AI Foundry provides built-in telemetry
    # through AzureAIChatCompletionsModel and AzureAIInferenceTracer
    _logger.debug("Using Azure AI Foundry built-in telemetry instead of LangchainInstrumentor")
            


def configure_telemetry_azure_monitor(
    connection_strings: List[str],
    customer_name: Optional[str] = None,
    agent_name: Optional[str] = None,
    views: Optional[List[View]] = None,
    enable_live_metrics: bool = True,
    logger_names: Optional[List[str]] = None,
    disable_offline_storage: bool = False,
    metric_export_interval_millis: int = 15000,
    # New flags to avoid explicit helper calls:
    enable_genai_content: bool = True,
    genai_content_mode: str = "all",
    enable_semantic_kernel_diagnostics: bool = True
) -> None:
    """
    Configure OpenTelemetry providers with Azure Monitor exporters for multiple
    Application Insights connection strings.

    - All telemetry (traces, logs, metrics) will be sent to ALL destinations.
    - Must be called once at process start, BEFORE importing/initializing libraries that emit telemetry.

    Args:
        connection_strings: List of Application Insights connection strings.
        resource: OpenTelemetry Resource for service attributes.
        views: Metric Views to filter/aggregate metrics.
        enable_live_metrics: Enable Live Metrics (QuickPulse) for metrics exporter.
        logger_names: Extra logger names to attach OTEL LoggingHandler (e.g. ["semantic_kernel", "azure"]).
        disable_offline_storage: Disable local disk retry storage for exporters.
        metric_export_interval_millis: Export interval for metrics.
        enable_genai_content: If True (default), set AZURE_TRACING_GEN_AI_* env to capture prompts/responses.
        genai_content_mode: "all" (default) or "sanitized".
        enable_semantic_kernel_diagnostics: If True (default), enable SK OTEL diagnostics env.
    """
    if not connection_strings or not any(cs for cs in connection_strings):
        raise ValueError("At least one valid connection string is required")

    # Set env-based features FIRST (so subsequent imports/instrumentations see them)
    if enable_genai_content:
        enable_genai_content_recording(True, genai_content_mode)
    else:
        # Explicitly disable
        enable_genai_content_recording(False, "sanitized")
    if enable_semantic_kernel_diagnostics:
        enable_semantic_kernel_otel(True)
    else:
        enable_semantic_kernel_otel(False)

    config = get_config()   
    # Get from config if not provided
    customer = customer_name or config["customer_name"]
    agent = agent_name or config["agent_name"]
    
    # Validate customer and agent names - we don't validate connection strings here
    # since we have multiple connection strings
    if not customer:
        error_msg = "Customer name is required for service identification"
        logger.error(f"Configuration error: {error_msg}")
        raise ValueError(error_msg)
        
    if not agent:
        error_msg = "Agent name is required for instance identification"
        logger.error(f"Configuration error: {error_msg}")
        raise ValueError(error_msg)
    
    # Validate the format of customer and agent names
    from .utilities import validate_name_format
    validate_name_format(customer, agent)
    
    resource = build_default_resource(customer,agent)
    if views is None:
        views = default_views()
    if logger_names is None:
        logger_names = ["semantic_kernel",
        "azure",
        "azure.core",
        "azure.ai",
        "azure.ai.projects"]

    common_exporter_kwargs = {
        "disable_offline_storage": disable_offline_storage,
    }

    # ---- Tracing Configuration ----
    # TracerProvider: The main factory for creating Tracer instances
    # - Manages the lifecycle of spans and traces
    # - Coordinates sampling decisions and resource attribution
    # - Handles span processors that export trace data
    tracer_provider = TracerProvider(
        # ApplicationInsightsSampler: Azure-specific sampling strategy
        # - sampling_ratio=1.0 means 100% of traces are sampled (no filtering)
        # - Helps reduce data volume in high-traffic scenarios
        # - Integrates with Application Insights adaptive sampling
        sampler=ApplicationInsightsSampler(sampling_ratio=1.0),
        # Resource: Metadata about the service generating telemetry
        # - Contains service.name, service.instance.id, and other attributes
        # - Appears in all traces/spans from this provider
        resource=resource,
    )
    configured_traces = 0
    for conn_str in connection_strings:
        if not conn_str:
            continue
        # AzureMonitorTraceExporter: Sends trace data to Azure Application Insights
        # - Converts OpenTelemetry spans to Application Insights telemetry format
        # - Handles authentication, retry logic, and offline storage
        # - Each connection string creates a separate exporter instance
        trace_exporter = AzureMonitorTraceExporter(connection_string=conn_str, **common_exporter_kwargs)
        
        # BatchSpanProcessor: Buffers spans before export for efficiency
        # - Collects spans in batches rather than sending individually
        # - Reduces network overhead and improves performance
        # - Automatically handles timeouts and batch size limits
        tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))
        configured_traces += 1
    
    # set_tracer_provider: Sets the global tracer provider for the application
    # - Makes this provider available to trace.get_tracer() calls
    # - All instrumentation libraries will use this provider
    # - Must be called before any tracing instrumentation occurs
    set_tracer_provider(tracer_provider)
    _logger.info("Tracing configured with %d exporters", configured_traces)

    # ---- Logging Configuration ----
    # LoggerProvider: Central factory for creating Logger instances
    # - Manages log record processors that handle log export
    # - Coordinates resource attribution for all log records
    # - Integrates with Python's standard logging module via LoggingHandler
    logger_provider = LoggerProvider(resource=resource)
    configured_logs = 0
    for conn_str in connection_strings:
        if not conn_str:
            continue
        # AzureMonitorLogExporter: Sends log records to Azure Application Insights
        # - Converts OpenTelemetry LogRecord to Application Insights trace/exception format
        # - Handles authentication, connection management, and retry logic
        # - Supports offline storage when connectivity is unavailable
        log_exporter = AzureMonitorLogExporter(connection_string=conn_str, **common_exporter_kwargs)
        
        # BatchLogRecordProcessor: Buffers log records before export
        # - Groups log records into batches for efficient network transmission
        # - Reduces API calls and improves overall logging performance
        # - Automatically handles flush timeouts and memory management
        logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))
        configured_logs += 1
    
    # _attach_logging_handlers: Configures Python loggers to send records to OpenTelemetry
    # - Creates LoggingHandler instances that bridge Python logging to OpenTelemetry
    # - Ensures logs from Azure SDKs, Semantic Kernel, etc. are captured
    # - Handles both root logger and specific named loggers to avoid duplicates
    _attach_logging_handlers(logger_provider, logger_names)
     
    _logger.info("Logging configured with %d exporters", configured_logs)

    # ---- Metrics Configuration ----
    # Metrics in OpenTelemetry provide quantitative measurements over time
    # Examples: request counts, response times, error rates, custom business metrics
    readers = []
    configured_metrics = 0
    for conn_str in connection_strings:
        if not conn_str:
            continue
        # AzureMonitorMetricExporter: Sends metrics to Azure Application Insights
        # - Converts OpenTelemetry metrics to Application Insights customMetrics format
        # - enable_live_metrics: Enables real-time metrics dashboard in Azure portal
        # - Handles aggregation, batching, and efficient transmission to Azure
        metric_exporter = AzureMonitorMetricExporter(
            connection_string=conn_str,
            # Live Metrics (QuickPulse): Real-time monitoring in Azure portal
            # - Shows live request rates, failure rates, CPU/memory usage
            # - Enables interactive debugging and performance monitoring
            enable_live_metrics=enable_live_metrics,
            **common_exporter_kwargs,
        )
        
        # PeriodicExportingMetricReader: Exports metrics at regular intervals
        # - export_interval_millis: How often to send metrics (15 seconds default)
        # - Collects metrics from instruments and sends them via exporter
        # - Handles temporal aggregation (sum, count, histogram, etc.)
        readers.append(PeriodicExportingMetricReader(metric_exporter, export_interval_millis=metric_export_interval_millis))
        configured_metrics += 1

    # MeterProvider: Factory for creating Meter instances
    # - metric_readers: List of readers that export metrics to different destinations
    # - resource: Service metadata attached to all metrics
    # - views: Filter and transformation rules for metrics
    #   * Controls which metrics are collected vs. dropped
    #   * Defines aggregation strategies (histogram buckets, etc.)
    #   * Enables/disables specific metric instruments
    meter_provider = MeterProvider(metric_readers=readers, resource=resource, views=views)
    
    # set_meter_provider: Sets the global meter provider for the application
    # - Makes this provider available to metrics.get_meter() calls
    # - All instrumentation libraries will use this provider for metrics
    # - Must be called before any metrics instrumentation occurs
    set_meter_provider(meter_provider)
    _logger.info(
        "Metrics configured with %d exporters (live_metrics=%s, interval=%dms)",
        configured_metrics,
        enable_live_metrics,
        metric_export_interval_millis,
    )
   
    _install_instrumentations()

    _logger.info(
        "Azure Monitor multi-destination telemetry configured for %d connection strings "
        "(genai_content=%s, genai_mode=%s, sk_otel=%s)",
        len(connection_strings),
        enable_genai_content,
        genai_content_mode,
        enable_semantic_kernel_diagnostics,
    )

def get_azure_ai_tracer(
    enable_content_recording: bool = True,
    instrument_inference: bool = True
):
    """
    Create an Azure AI Inference Tracer that integrates with the global telemetry configuration.
    
    The Azure AI Inference Tracer is a specialized component that:
    1. Captures Azure AI model calls (GPT, embedding, etc.) with rich context
    2. Records prompts and responses based on content recording settings
    3. Integrates seamlessly with LangChain and Azure AI Foundry workflows
    4. Inherits connection strings from global telemetry setup (no duplication)
    
    Architecture Integration:
    - Uses connection_string=None to inherit from global configure_telemetry_azure_monitor()
    - Leverages existing TracerProvider, LoggerProvider, and MeterProvider
    - Maintains trace correlation across HTTP → AI model → database calls
    - Respects global content recording settings and compliance requirements
    
    Content Recording Features:
    - Prompt/Response Capture: Full conversation history with timestamps
    - Token Usage Tracking: Input/output token counts for cost optimization  
    - Model Metadata: Model version, temperature, max tokens, etc.
    - Error Context: Detailed failure information for troubleshooting
    
    LangChain Integration:
    - Works as a LangChain callback for automatic integration
    - Captures agent reasoning steps and tool usage
    - Tracks multi-turn conversations and memory operations
    - Provides span hierarchy: Agent → Tool → Model Call
    
    Args:
        enable_content_recording: Whether to capture AI prompts and responses
                                 (subject to global AZURE_TRACING_GEN_AI_CONTENT_RECORDING_* settings)
        instrument_inference: Whether to instrument the Azure AI inference client directly
                             (complements but doesn't duplicate OpenTelemetry auto-instrumentation)
    
    Returns:
        AzureAIInferenceTracer: Configured tracer instance ready for LangChain integration
        
    Raises:
        RuntimeError: If global telemetry not configured (must call configure_telemetry_azure_monitor first)
        ImportError: If langchain-azure-ai package not installed
        
    Example:
        # Step 1: Configure global telemetry
        configure_telemetry_azure_monitor(connection_strings=["InstrumentationKey=..."])
        
        # Step 2: Get tracer (inherits global config)
        tracer = get_azure_ai_tracer()
        
        # Step 3: Use with LangChain
        llm = AzureChatOpenAI(callbacks=[tracer])
        response = llm.invoke("What is the weather?")
    """
    try:
        # Import Azure LangChain integration package
        # This provides the AzureAIInferenceTracer class for LangChain callbacks
        from langchain_azure_ai.callbacks.tracers import AzureAIInferenceTracer
        
        # ===== GLOBAL TELEMETRY VALIDATION =====
        # Verify that configure_telemetry_azure_monitor() has been called
        # The tracer requires an active TracerProvider to function properly
        from opentelemetry import trace
        current_provider = trace.get_tracer_provider()
        
        # NoOpTracerProvider: Default provider when OpenTelemetry not configured
        # - Created automatically if no explicit provider is set
        # - Discards all telemetry data (no-op operations)
        # - Indicates configure_telemetry_azure_monitor() hasn't been called
        if current_provider.__class__.__name__ == "NoOpTracerProvider":
            raise RuntimeError(
                "Global telemetry not configured. The AzureAIInferenceTracer requires "
                "OpenTelemetry to be set up first. Call configure_telemetry_azure_monitor() "
                "before calling get_azure_ai_tracer()."
            )
        
        # ===== TRACER CREATION =====
        # Create tracer that inherits global configuration
        tracer = AzureAIInferenceTracer(
            # connection_string=None: Critical configuration choice
            # - Inherits connection strings from global TracerProvider
            # - Avoids duplicating connection string configuration
            # - Ensures consistency with other telemetry destinations
            # - Leverages existing authentication and retry settings
            connection_string=None,  # Inherit from global configuration
            
            # Content recording: Captures prompts/responses if enabled globally
            # - Respects AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED env var
            # - Subject to compliance and privacy requirements
            # - Can be overridden per tracer instance if needed
            enable_content_recording=enable_content_recording,
            
            # Inference instrumentation: Auto-instrument Azure AI client
            # - Complements OpenTelemetry auto-instrumentation
            # - Adds LangChain-specific context and metadata
            # - Enables deeper integration with agent workflows
            instrument_inference=instrument_inference,
        )
        
        _logger.info("✓ Created Azure AI tracer using global telemetry configuration")
        return tracer
        
    except ImportError:
        # ImportError: langchain-azure-ai package not installed
        # This is expected if users don't need LangChain integration
        _logger.error(
            "Azure LangChain tracer not available. Install with: "
            "pip install langchain-azure-ai"
        )
        raise
    except RuntimeError:
        # RuntimeError: Configuration problems (re-raise with original message)
        # These are user errors that need to be surfaced clearly
        raise
    except Exception as ex:
        # Other exceptions: Unexpected errors during tracer creation
        # Could indicate version incompatibilities or configuration issues
        _logger.error("Failed to create Azure AI tracer: %s", ex)
        raise

