import json
import random

from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


class GenericClassBasedView(TemplateView):
    """Generic Class-Based View (gCBV)"""

    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        """Return the context."""
        context = super().get_context_data(**kwargs)
        context['title'] = "Welcome to the 'main.html' view (Generic Class-Based View)"
        return context


class ClassBasedView(View):
    """Class-Based View (CBV)"""

    def get(self, request, *args, **kwargs):
        template_name = kwargs['template']
        # This data dict will be added to the template context
        data = {}
        data['title'] = "Welcome to the '" + kwargs['template'] + "' view (Class-Based View)"
        return render(request, template_name, data)

    def post(self, request):
        # We don't handle POST requests
        pass


def function_based_view(request):
    """Function-Based View (FBV)"""

    if request.method == 'GET':
        template_name = 'main.html'
        # This data dict will be added to the template context
        data = {}
        data["title"] = "Welcome to the '" + template_name + "' view (Function-Based View)"
        return render(request, template_name, data)
    else:
        # We don't handle POST requests
        pass


def integrated_vue_view(request):
    names = ("bob", "dan", "jack", "lizzy", "susan")

    items = []
    for i in range(20):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20, 80),
            "url": "https://example.com",
        })

    context = {}
    context["items"] = items
    context["items_json"] = json.dumps(items)

    return render(request, 'integrated.html', context)
