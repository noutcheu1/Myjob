from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from .models import Job, Choice

def index(request):
    lastest_Job_list = Job.objects.order_by('-pub_date')[:5]
    context = {
        'lastest_job_list': lastest_Job_list,
    }
    return render(request, 'polls/index.html', context)
# ...
def detail(request, job_id, date):
    try:
        job = Job.objects.get(pk=job_id)
        date = timezone.now()
    except Job.DoesNotExist:
        raise Http404("job does not exist")
    return render(request, 'polls/details.html', {'job': job})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)