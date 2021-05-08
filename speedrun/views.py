from django.http import HttpResponse
from django.shortcuts import render
from .models import Run


def index(request):
    top_runs_list = Run.objects.order_by('time')[:]
    top_runs_list.reverse()

    context = {
        'top_runs_list': top_runs_list,
    }

    return render(request, 'home.html', context)
