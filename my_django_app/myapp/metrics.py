from prometheus_client import Counter, Gauge, generate_latest
from prometheus_client.exposition import MetricsHandler
from django.http import HttpResponse
import psutil

# Define custom Prometheus metrics
requests_total = Counter('requests_total', 'Total HTTP requests')
active_users = Gauge('active_users', 'Number of active users')
memory_usage = Gauge('memory_usage_bytes', 'Memory Usage (in bytes)')
cpu_usage = Gauge('cpu_usage_percent', 'CPU Usage (in percentage)')
network_usage = Gauge('network_usage_bytes', 'Network Usage (in bytes)')
disk_usage = Gauge('disk_usage_bytes', 'Disk Usage (in bytes)')

# Example view that increments the 'requests_total' metric and collects resource usage
def example_view(request):
    # Increment the 'requests_total' metric
    requests_total.inc()

    # Simulate the number of active users (replace with real logic)
    active_users.set(42)

    return HttpResponse('Hello, Prometheus!')

# Custom /metrics endpoint to expose metrics for Prometheus to scrape
def metrics_view(request):
    # Get resource usage metrics
    mem_info = psutil.virtual_memory()
    cpu_percent = psutil.cpu_percent(interval=None)
    net_io_counters = psutil.net_io_counters()
    disk_usage_info = psutil.disk_usage('/')

    # Set resource usage metrics
    memory_usage.set(mem_info.used)
    cpu_usage.set(cpu_percent)
    network_usage.set(net_io_counters.bytes_sent + net_io_counters.bytes_recv)
    disk_usage.set(disk_usage_info.used)

    response = HttpResponse(generate_latest(), content_type='text/plain; version=0.0.4')
    return response
