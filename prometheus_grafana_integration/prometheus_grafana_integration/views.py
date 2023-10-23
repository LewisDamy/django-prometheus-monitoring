from django.shortcuts import render
from prometheus_client import Summary

# Create a Summary metric
render_time = Summary('template_render_time', 'Time taken to render a template')

@render_time.time()
def my_view(request):
    # Your view logic here

    # Creating a context dictionary to pass data to the template
    context = {
        'variable1': 'This is some data',
        'variable2': 42,
        'list_data': [1, 2, 3, 4, 5],
    }

    # Pass the context to the template when rendering
    return render(request, 'my_template.html', context)
