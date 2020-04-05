from django.shortcuts import render
from .models import Teacher

# Create your views here.
def teacher_tt(request):
    teachers = Teacher.objects.all().order_by('id')
    return render(request,'teachers/teacher_tt.html', {'teachers':teachers})
