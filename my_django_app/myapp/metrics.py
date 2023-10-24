from prometheus_client import Counter, Gauge, generate_latest
from prometheus_client.exposition import MetricsHandler
from django.http import HttpResponse

# Define custom Prometheus metrics
requests_total = Counter('myapp_requests_total', 'Total HTTP requests')
active_users = Gauge('myapp_active_users', 'Number of active users')

# Example view that increments the 'requests_total' metric
def example_view(request):
    # Increment the 'requests_total' metric
    requests_total.inc()

    # Simulate the number of acjtive users (replace with real logic)
    active_users.set(42)

    return HttpResponse('Hello, Prometheus!')

# Custom /metrics endpoint to expose metrics for Prometheus to scrape
def metrics_view(request):
    response = HttpResponse(generate_latest(), content_type='text/plain; version=0.0.4')
    return response
