from django.shortcuts import render
from .models import  Info_Model, Exp_Model ,Portfolio_Model
# Create your views here.
def home(request):
    exp = Exp_Model.objects.all()
    work = Portfolio_Model.objects.all()
    cv_info = Info_Model.objects.all()
   
    context={
    'cv_info':cv_info,
    'exp':exp ,
    'work':work,
    
    }

    return render(request , 'portfolio/home.html',context)


