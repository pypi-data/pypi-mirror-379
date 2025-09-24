"""Application logic for rendering HTML templates and handling HTTP requests.

View objects encapsulate logic for interpreting request data, interacting with
models or services, and generating the appropriate HTTP response(s). Views
serve as the controller layer in Django's MVC-inspired architecture, bridging
URLs to business logic.
"""

from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, viewsets

from .models import *
from .permissions import *
from .serializers import *

__all__ = [
    'AuditLogViewSet',
    'RequestLogViewSet',
    'TaskResultViewSet',
]


@extend_schema_view(
    list=extend_schema(
        summary="List all audit logs",
        description=(
            "Retrieve all application audit logs. "
            "These log entries track changes to database records and are used for compliance and security auditing."
        ),
        tags=["Logging"],
    ),
    retrieve=extend_schema(
        summary="Retrieve an audit log record",
        description=(
            "Retrieve an audit log by ID. "
            "These log entries track changes to database records and are used for compliance and security auditing."
        ),
        tags=["Logging"],
    )
)
class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for fetching audit logs."""

    permission_classes = [permissions.IsAuthenticated, IsAdminRead]
    search_fields = ['resource', 'action', 'user_username']
    serializer_class = AuditLogSerializer
    queryset = AuditLog.objects.select_related('actor', 'content_type')


@extend_schema_view(
    list=extend_schema(
        summary="List all HTTP request logs",
        description=(
            "Retrieve a list of HTTP request logs. "
            "These logs track incoming API requests and their resulting HTTP responses."
        ),
        tags=["Logging"],
    ),
    retrieve=extend_schema(
        summary="Retrieve an HTTP request log record",
        description=(
            "Retrieve a single HTTP request log by ID. "
            "These logs track incoming API requests and their resulting HTTP responses."
        ),
        tags=["Logging"],
    )
)
class RequestLogViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for fetching HTTP request logs."""

    permission_classes = [permissions.IsAuthenticated, IsAdminRead]
    search_fields = ['endpoint', 'method', 'response_code', 'body_request', 'body_response', 'remote_address']
    serializer_class = RequestLogSerializer
    queryset = RequestLog.objects.select_related('user')


@extend_schema_view(
    list=extend_schema(
        summary="List all background task results",
        description=(
            "Retrieve a list of background task results. "
            "These logs are collected from the Celery backend to track background task outcomes and failures."
        ),
        tags=["Logging"],
    ),
    retrieve=extend_schema(
        summary="Retrieve a background task result",
        description=(
            "Retrieve a single background task result by ID. "
            "These logs are collected from the Celery backend to track background task outcomes and failures."
        ),
        tags=["Logging"],
    )
)
class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for fetching background task results."""

    permission_classes = [permissions.IsAuthenticated, IsAdminRead]
    search_fields = ['periodic_task_name', 'task_name', 'status', 'worker', 'result', 'traceback']
    serializer_class = TaskResultSerializer
    queryset = TaskResult.objects.all()
