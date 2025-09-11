from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Resume
from django.contrib.auth.decorators import login_required
import os
import pdfkit
import platform
from django.conf import settings
from django.templatetags.static import static
from django.contrib.staticfiles import finders
import shutil

# Create your views here.
@login_required(login_url='login')
def form(request):
    if request.user.is_authenticated:
        try:
            resume = Resume.objects.get(user=request.user)
            context = {
                'resume': resume,
                'edit_mode': True,
                'first_name': resume.first_name,
                'last_name': resume.last_name,
                'email': resume.email,
                'phone': resume.phone,
                'summary': resume.summary,
                'skills': resume.skills,
                'softskills': resume.softskills,
                'language': resume.language,
                'education': resume.education,
                'address': resume.address,
                'start_year':resume.start_year,
                'end_year':resume.end_year,
                'cgpa':resume.cgpa,
                'company_one':resume.company_one,
                'company_two':resume.company_two,
                'role_one':resume.role_one,
                'role_two':resume.role_two,
                'job_one':resume.job_one,
                'job_two':resume.job_two
            }
        except Resume.DoesNotExist:
            context = {
                'resume': None,
                'edit_mode': False,
                'first_name': '',
                'last_name': '',
                'email': '',
                'phone': '',
                'summary': '',
                'skills': '',
                'softskills': '',
                'language': '',
                'experiences': '',
                'education': '',
                'address': '',
                'start_year':'',
                'end_year':'',
                'cgpa':'',
                'company_one':'',
                'company_two':'',
                'role_one':'',
                'role_two':'',
                'job_one':'',
                'job_two':'',

                
            }
    else:
        return redirect('login')  # Redirect to login if not logged in

    return render(request, 'form.html', context)

    
@login_required(login_url='login')
def form1(request):
    if request.user.is_authenticated:
        try:
            resume = Resume.objects.get(user=request.user)
            context = {
                'resume': resume,
                'edit_mode': True,
                'first_name': resume.first_name,
                'last_name': resume.last_name,
                'email': resume.email,
                'phone': resume.phone,
                'summary': resume.summary,
                'skills': resume.skills,
                'softskills': resume.softskills,
                'language': resume.language,
                'education': resume.education,
                'address': resume.address,
                'start_year':resume.start_year,
                'end_year':resume.end_year,
                'cgpa':resume.cgpa,
                'company_one':resume.company_one,
                'company_two':resume.company_two,
                'role_one':resume.role_one,
                'role_two':resume.role_two,
                'job_one':resume.job_one,
                'job_two':resume.job_two
            }
        except Resume.DoesNotExist:
            context = {
                'resume': None,
                'edit_mode': False,
                'first_name': '',
                'last_name': '',
                'email': '',
                'phone': '',
                'summary': '',
                'skills': '',
                'softskills': '',
                'language': '',
                'experiences': '',
                'education': '',
                'address': '',
                'start_year':'',
                'end_year':'',
                'cgpa':'',
                'company_one':'',
                'company_two':'',
                'role_one':'',
                'role_two':'',
                'job_one':'',
                'job_two':'',
            }
    else:
        return redirect('login')  # Redirect to login if not logged in

    return render(request, 'form1.html', context)

def home(request):
    user_resume = None
    if request.user.is_authenticated:
        try:
            user_resume = Resume.objects.get(user=request.user)
        except Resume.DoesNotExist:
            user_resume = None
    return render(request, 'home.html', {'resume_exists': user_resume})

def template(request):
    return render(request, 'template.html',)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')
    
    return render(request, 'signup.html')

def resume(request):
    if request.method=="POST":
        resume, created = Resume.objects.get_or_create(user=request.user)
        resume.first_name=request.POST.get('first_name')
        resume.last_name=request.POST.get('last_name')
        resume.email=request.POST.get('email')
        resume.phone=request.POST.get('phone')
        resume.address=request.POST.get('address')
        resume.summary=request.POST.get('summary')
        resume.skills=request.POST.get('skills')
        resume.softskills=request.POST.get('softskills')
        resume.language=request.POST.get('language')
        resume.education=request.POST.get('education')
        resume.start_year=request.POST.get('start_year')
        resume.end_year=request.POST.get('end_year')
        resume.cgpa=request.POST.get('cgpa')
        resume.company_one=request.POST.get('company_one')
        resume.company_two=request.POST.get('company_two')
        resume.role_one=request.POST.get('role_one')
        resume.role_two=request.POST.get('role_two')
        resume.job_one=request.POST.get('job_one')
        resume.job_two=request.POST.get('job_two')
        resume.save()
        
        context={
            'first_name':resume.first_name,
            'last_name':resume.last_name,
            'email':resume.email,
            'phone':resume.phone,
            'address':resume.address,
            'summary':resume.summary,
            'skills':[skill.strip() for skill in (resume.skills or "").split(',')],
            'softskills':[softskill.strip() for softskill in (resume.softskills or "").split(',')],
            'language':[language.strip() for language in (resume.language or "").split(',')],
            'education':resume.education,
            'start_year':resume.start_year,
            'end_year':resume.end_year,
            'cgpa':resume.cgpa,
            'company_one':resume.company_one,
            'company_two':resume.company_two,
            'role_one':resume.role_one,
            'role_two':resume.role_two,
            'job_one':resume.job_one.split('.'),
            'job_two':resume.job_two.split('.'),
            
                             
        }
       
        request.session['resume_data'] = context
        
        return render(request,'resume.html',context)
    else:
         return render(request,'form.html')
    
def resume1(request):
    if request.method=="POST":
        resume, created = Resume.objects.get_or_create(user=request.user)
        resume.first_name=request.POST.get('first_name')
        resume.last_name=request.POST.get('last_name')
        resume.email=request.POST.get('email')
        resume.phone=request.POST.get('phone')
        resume.address=request.POST.get('address')
        resume.summary=request.POST.get('summary')
        resume.skills=request.POST.get('skills')
        resume.softskills=request.POST.get('softskills')
        resume.language=request.POST.get('language')
        resume.education=request.POST.get('education')
        resume.start_year=request.POST.get('start_year')
        resume.end_year=request.POST.get('end_year')
        resume.cgpa=request.POST.get('cgpa')
        resume.company_one=request.POST.get('company_one')
        resume.company_two=request.POST.get('company_two')
        resume.role_one=request.POST.get('role_one')
        resume.role_two=request.POST.get('role_two')
        resume.job_one=request.POST.get('job_one')
        resume.job_two=request.POST.get('job_two')
        resume.save()
            
        context={
            'first_name':resume.first_name,
            'last_name':resume.last_name,
            'email':resume.email,
            'phone':resume.phone,
            'address':resume.address,
            'summary':resume.summary,
            'skills':[skill.strip() for skill in (resume.skills or "").split(',')],
            'softskills':[softskill.strip() for softskill in (resume.softskills or "").split(',')],
            'language':[language.strip() for language in (resume.language or "").split(',')],
            'education':resume.education,
            'start_year':resume.start_year,
            'end_year':resume.end_year,
            'cgpa':resume.cgpa,
            'company_one':resume.company_one,
            'company_two':resume.company_two,
            'role_one':resume.role_one,
            'role_two':resume.role_two,
            'job_one':resume.job_one.split('.'),
            'job_two':resume.job_two.split('.'),
            
               
        }
       
        request.session['resume_data1'] = context
        return render(request,'resume1.html',context)
    else:
         return render(request,'form1.html')

@login_required(login_url='login')
def edit_resume(request, template_id):
    try:
        resume = Resume.objects.get(user=request.user)
    except Resume.DoesNotExist:
        return redirect('form')
    
    if request.method == 'POST':
        resume.first_name=request.POST.get('first_name')
        resume.last_name=request.POST.get('last_name')
        resume.email=request.POST.get('email')
        resume.phone=request.POST.get('phone')
        resume.address=request.POST.get('address')
        resume.summary=request.POST.get('summary')
        resume.skills=request.POST.get('skills')
        resume.summary=request.POST.get('summary')
        resume.education=request.POST.get('education')
        resume.start_year=request.POST.get('start_year')
        resume.end_year=request.POST.get('end_year')
        resume.cgpa=request.POST.get('cgpa')
        resume.company_one=request.POST.get('company_one')
        resume.company_two=request.POST.get('company_two')
        resume.role_one=request.POST.get('role_one')
        resume.role_two=request.POST.get('role_two')
        resume.job_one=request.POST.get('job_one')
        resume.job_two=request.POST.get('job_two')
        resume.save()

        messages.success(request, "Resume updated successfully.")
        return redirect('home')
    
    # render correct form
    if template_id == 1:
        return render(request, 'form.html', {'resume': resume})
    elif template_id == 2:
        return render(request, 'form1.html', {'resume': resume})
    else:
        return redirect('home')

def download_pdf(request):
    resume, created = Resume.objects.get_or_create(user=request.user)
    context = {
        'first_name':resume.first_name,
            'last_name':resume.last_name,
            'email':resume.email,
            'phone':resume.phone,
            'address':resume.address,
            'summary':resume.summary,
            'skills':[skill.strip() for skill in (resume.skills or "").split(',')],
            'softskills':[softskill.strip() for softskill in (resume.softskills or "").split(',')],
            'language':[language.strip() for language in (resume.language or "").split(',')],
            'education':resume.education,
            'start_year':resume.start_year,
            'end_year':resume.end_year,
            'cgpa':resume.cgpa,
            'company_one':resume.company_one,
            'company_two':resume.company_two,
            'role_one':resume.role_one,
            'role_two':resume.role_two,
            'job_one':resume.job_one.split('.'),
            'job_two':resume.job_two.split('.'),
            'for_pdf': True 
    }

    html = render_to_string("resume.html", context)
   
    path_wkhtmltopdf = shutil.which("wkhtmltopdf")
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    
    css_path = os.path.join(settings.BASE_DIR, "static" "css", "resume.css")

    pdf = pdfkit.from_string(
        html,
        False,
        configuration=config,
        css=[css_path],
        options={
            "enable-local-file-access": None,
            "print-media-type": None,
            "page-size": "A4",
            "page-width": "210mm",      
            "page-height": "297mm",   
            "margin-top": "0mm",
            "margin-right": "0mm",
            "margin-bottom": "0mm",
            "margin-left": "0mm",
            "zoom": "0.8",   
            "disable-smart-shrinking": None,
            "no-stop-slow-scripts": "",
            "viewport-size": "1280x1024",
        },
        
    )    
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="resume.pdf"'
    return response
    

def download_pdf1(request):
    resume, created = Resume.objects.get_or_create(user=request.user)
    context = {
        'first_name': resume.first_name,
        'last_name': resume.last_name,
        'email': resume.email,
        'phone': resume.phone,
        'address': resume.address,
        'summary': resume.summary,
        'skills': [skill.strip() for skill in (resume.skills or "").split(',')],
        'softskills': [softskill.strip() for softskill in (resume.softskills or "").split(',')],
        'language': [language.strip() for language in (resume.language or "").split(',')],
        'education': resume.education,
        'start_year': resume.start_year,
        'end_year': resume.end_year,
        'cgpa': resume.cgpa,
        'company_one': resume.company_one,
        'company_two': resume.company_two,
        'role_one': resume.role_one,
        'role_two': resume.role_two,
        'job_one': resume.job_one.split('.'),
        'job_two': resume.job_two.split('.'),
        'for_pdf': True
    }

    html = render_to_string("resume1.html", context)
    if platform.system() == "Windows":
        wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    else:
        wkhtmltopdf_path = "/usr/bin/wkhtmltopdf"
        config = pdfkit.configuration(wkhtmltopdf,wkhtmltopdf_path)

    css_path = finders.find('css/resume1.css')
    print("CSS exists?", os.path.exists(css_path)) 

    pdf = pdfkit.from_string(
    html,
    False,
    configuration=config,
    css=[css_path],
    options={
            "enable-local-file-access": None,
            "print-media-type": None,
            "page-size": "A4",
            "page-width": "210mm",    
            "page-height": "297mm",       
            "margin-top": "5mm",        
            "margin-right": "5mm",
            "margin-bottom": "5mm",
            "margin-left": "5mm",
            "encoding": "UTF-8",
            "zoom": "0.8",
            "disable-smart-shrinking": None,
            "no-stop-slow-scripts": "",
            "viewport-size": "1280x1024",

        }
)

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="resume1.pdf"'
    return response
