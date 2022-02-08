from django.shortcuts import render
from .models import Profile
import pdfkit #Helps in conerting html template to pdf file
from django.http import HttpResponse
from django.template import loader #Helps in conerting html template to pdf file
import io #Helps in conerting html template to pdf file

# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()
    return render(request, 'pdf/accept.html')

def resume (request, pk):
    '''The first two lines was just to show
    it in pdf format on the browser'''
    user_profile = Profile.objects.get(pk=pk)
    #return render(request, 'pdf/resume.html', {'user_profile':user_profile})

    template = loader.get_template('pdf/resume.html') # To get the template 
    html = template.render({'user_profile':user_profile}) # To render the template, we send it to the pdf library 
    options = {
        'page-size': 'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options) # converts the html string/template method to pdf document
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response

def list(request):
    profile = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profile':profile})