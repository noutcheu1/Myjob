from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from .models import Travail, Choix

def index(request):
    lastest_Job_list = Travail.objects.order_by('-pub_date')[:10]
    context = {
        'lastest_job_list': lastest_Job_list,
    }
    return render(request, 'core/index.html', context)
def detail(request, job_id):
    try:
        job = Choix.objects.get(pk=job_id)
        context = {
                'job': job
        }
       # date = timezone.now()
    except Travail.DoesNotExist:
        raise Http404("job does not exist")
    return render(request, 'core/detail.html', context)