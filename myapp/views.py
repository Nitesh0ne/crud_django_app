from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForms
from .forms import ImageFrom
from .models import ImageModel
# Create your views here.

def home(request, id=None):
    if id:
        student_update =get_object_or_404(Student, id=id)
        form = StudentForms(request.POST or None, instance=student_update)
    else:
        form = StudentForms(request.POST or None)


  
    # form = StudentForms()

    if request.method == "POST" :
        if 'delete' in request.POST:
            student_to_delete = get_object_or_404(Student,id=request.POST['delete'])
            student_to_delete.delete()
            return redirect('home')
        
        form = form
        if form.is_valid():
            form.save()
            return redirect('home')

    students = Student.objects.all()



    
    context = {
        'students' : students,
        'form':form
    }

    return render(request, "home.html", context=context)



def upload_image(request):
    if request.method == "POST":
        form = ImageFrom(request.POST, request.Files)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageFrom()
    images = ImageModel.objects.all()
    context = {
        'form' : form,
        'images': images,
    }
    return render(request,'upload.html', context=context)    





