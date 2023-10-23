# Use the official Prometheus image as a base
FROM prom/prometheus:v2.30.0

# Copy your local Prometheus configuration file into the image
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Expose the Prometheus web UI and API ports
EXPOSE 9090

# Start Prometheus with your custom configuration
CMD ["prometheus", "--config.file=/etc/prometheus/prometheus.yml"]
