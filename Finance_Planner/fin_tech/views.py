from django.shortcuts import render, HttpResponse
from .models import PersonalDetails
from django.db.models import Q

def members(request):
    print(request.method)
    if request.method == 'POST':
        Name = request.POST['name']
        BirthYear = request.POST['birthYear']
        Age = request.POST['currentAge']
        Gender = request.POST['gender']
        Profession = request.POST['profession']
        print(Name,BirthYear,Age,Gender,Profession)
        new_emp = PersonalDetails(name=Name, birthyear=BirthYear, age=Age, gender=Gender, profession=Profession)
        new_emp.save()
        return HttpResponse("Form Submited Successfully")
    elif request.method == 'GET':
        return render(request,'sample.html')
    
def show_details(request):
    data = PersonalDetails.objects.all()
    context = {
        'data': data
    }
    print(context)
    return render(request, 'show_details.html', context)
 
        