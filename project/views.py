from django.http import HttpResponse
from django.shortcuts import render
from teachers.models import Teacher,TimeTable
from django.views.generic import TemplateView

def homepage(request):
    teachers = Teacher.objects.all().order_by('id')
    return render(request,'homepage.html', {'teachers':teachers})

def timetable_is(request, id):
    #return HttpResponse(id)
    teacher = Teacher.objects.get(id=id)
    timetable = TimeTable.objects.filter(Teacher_id=id)
    # print(timetable)
    # for e in timetable:
    #     print(e.Lecture)
    return render(request,'timetable.html',{'teacher':teacher,'timetable':timetable})

def after_attendance(request):
    teachers = Teacher.objects.all().order_by('id')
    timetable = TimeTable.objects.all().order_by('id')
    return render(request,'after_attendance.html',{'teachers':teachers, 'timetable':timetable})
