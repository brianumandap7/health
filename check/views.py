from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Gender, Profile, Classification

# Create your views here.
def check(request):
	query = {
		'gender': Gender.objects.all(),
		'class': Classification.objects.all(),
		'curr': User.objects.filter(username = request.user),
	}

	if request.method == "POST" and 'sbtn' in request.POST:
		db = Profile()
		db.full_name = request.POST.get('fname')
		db.gender_id = request.POST.get('gender')
		db.email = request.POST.get('email')
		db.classification_id = request.POST.get('classi')
		db.identification_number = request.POST.get('in')
		db.save()

		return HttpResponseRedirect('/submitted/')

	return render(request, 'check/check.html', query)

def submitted(request):
	query = {

	}
	return render(request, 'check/submitted.html', query)


