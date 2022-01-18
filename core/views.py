from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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
def nbre_place(request, travail_id):
    travail = get_object_or_404(Travail, pk=travail_id)
    try:
        selected_choice = travail.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choix.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, '/detail.html', {
            'travail': travail,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.nbre_place += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('core:results', args=(travail.id,)))
def results(request, travail_id):
    question = get_object_or_404(Travail, pk=travail_id)
    return render(request, 'core/results.html', {'question': question})

