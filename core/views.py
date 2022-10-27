from django.shortcuts import render
from .models import Study, Work

# Create your views here.

def home(request):
    studies = Study.objects.all().order_by('-end')
    jobs = Work.objects.all().order_by('end')
    return render(
        request, 
        'core/index.html', 
        {
            'studies' : studies,
            'jobs' : jobs
        }
    )