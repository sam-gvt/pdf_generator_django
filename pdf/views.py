from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
import pdfkit
from django.template import loader

def accept(request):

    if request.method == "POST":
        job_seek = request.POST.get("job_seek", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        location = request.POST.get("location", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")
        interests = request.POST.get("interests", "")
        

        profile = Profile(
            job_seek=job_seek,
            name=name, 
            email=email, 
            phone=phone,
            location=location,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills,
            interests=interests
        )
        profile.save()
        return redirect('/pdf')
    
    cv_id = request.GET.get('id')
    if cv_id:
        return redirect(f'/pdf/{cv_id}')


    list_cv = Profile.objects.all()

    return render(request, 'pdf/accept.html', {"list_cv":list_cv})


def cv(request, id):
    user_profile = Profile.objects.get(pk=id)
    html = loader.render_to_string('pdf/cv.html', {'user_profile':user_profile})
    output= pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response
    

