from django.shortcuts import render, redirect
from .forms import Contact
from .models import Study, Work, Project, Article
from django.core.mail import EmailMessage
# Create your views here.

def home(request):
    studies = Study.objects.all().order_by('-end')
    jobs = Work.objects.all().order_by('end')
    projects = Project.objects.all()
    articulos = Article.objects.all().order_by('date')
    form = Contact()

    if request.method == 'POST':
        form_enviado = Contact(data = request.POST)
        if form_enviado.is_valid():
            name = request.POST.get('name', '')
            mail = request.POST.get('mail', '')
            subject = request.POST.get('subject', '')
            msj = request.POST.get('message', '')

            mail_envio = EmailMessage(
                    'Mensaje desde pagina personal',
                    """
                    Nombre: {}
                    <br>
                    Mail: {}
                    <br>
                    Subject: {}
                    <br>
                    Message: {}
                    """.format(name,mail, subject, msj),
                    'dblancbellido@gmail.com',
                    ['dblancbellido@gmail.com'],
                    reply_to=['dblancbellido@gmail.com'],
                )
            mail_envio.content_subtype = 'html'
            mail_envio.send()
            return redirect(request.META['HTTP_REFERER'])

    return render(
        request, 
        'core/index.html', 
        {
            'studies' : studies,
            'jobs' : jobs,
            'projects' : projects,
            'articulos' : articulos,
            'form' : form
        }
    )