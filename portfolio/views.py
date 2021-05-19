from django.shortcuts import render
from .models import Project
from .models import Video

def home(request):
	projects=Project.objects.all()
	return render(request,'portfolio/home.html',{'projects':projects})
def index(request):
	videos=Video.objects.all()	
	return render(request, 'portfolio/home.html', {'videos':videos})
