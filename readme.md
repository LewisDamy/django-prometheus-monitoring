# Django Application Monitoring with Prometheus and Grafana

This example demonstrates how to set up monitoring for a Django application using Prometheus and Grafana. You can use this as a template for implementing monitoring in your own Django projects.

## Setup

1. **Django Application**:
   - Ensure your Django application is ready for monitoring.
   - Install the necessary Python packages:
     ```
     pip install prometheus-client django-prometheus
     ```
   - Configure your Django application as mentioned in the previous instructions.

2. **Prometheus**:
   - Create a `prometheus.yml` configuration file to specify scrape targets and other settings. Make sure it's correctly formatted.
   - Build the Prometheus Docker image:
     ```
     docker build -t my-prometheus ./prometheus
     ```
   - Start the Prometheus container:
     ```
     docker run -d -p 9090:9090 --name my-prometheus my-prometheus
     ```

3. **Grafana**:
   - Create dashboard and data source configurations (e.g., `my-dashboard.json` and `my-datasource.yml`) in the `grafana/` directory.
   - Build the Grafana Docker image:
     ```
     docker build -t my-grafana ./grafana
     ```
   - Start the Grafana container:
     ```
     docker run -d -p 3000:3000 --name my-grafana my-grafana
     ```

4. **Docker Compose**:
    - Execute all three containers using the `docker-compose.yml`.
    - Start the server:
    ```
    docker-compose build
    ```
    - Run the applications:
    ```
    docker-compose up
    ```
    - Stopping the applications:
    ```
    docker-compose down
    ```
5. **Access Metrics**:
   - Access the Django application at `http://localhost:8080/example` or to see the data being send to prometheus at `http://localhost:8080/metrics`.
   - Access the Prometheus metrics at `http://localhost:9090/metrics`.
   - Access Grafana at `http://localhost:3000` and configure it to use Prometheus as the data source. Import the dashboard using the `my-dashboard.json` file.

## Running
   - Here is a sample of them running:
    - Grafana `http:locahost:3000/dashboards/prometheus-2-0-stats`
    ![Grafana Graphics](https://github.com/LewisDamy/django-prometheus-monitoring/blob/main/assets/Grafana%20App%20Running.png)
    - Django `http:localhost:8080/example`
    ![Django App Example](https://github.com/LewisDamy/django-prometheus-monitoring/blob/main/assets/Django%20App%20Running%20-%20Example.png)
    - Django `http:localhost:8080/metrics`
    ![Django App Metrics](https://github.com/LewisDamy/django-prometheus-monitoring/blob/main/assets/Django%20App%20Running%20-%20Metrics.png)
    - Prometheus `http:localhost:9090/metrics`
    ![Prometheus App Metrics](https://github.com/LewisDamy/django-prometheus-monitoring/blob/main/assets/Prometheus%20App%20Running.png)

## Troubleshooting

- If you encounter any issues, refer to the troubleshooting steps in the provided documentation.
- Check the container logs for Prometheus and Grafana using `docker logs my-prometheus` and `docker logs my-grafana`, respectively.

This example provides a basic setup for monitoring a Django application. Customize the configurations and dashboard as needed for your specific use case.

Feel free to expand on this README with additional project-specific instructions or details.
