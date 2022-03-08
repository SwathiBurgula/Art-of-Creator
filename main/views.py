from django.http import HttpRequest
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="templates/register.html", context={"register_form":form})


def create(request):
    form  = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    context = {'form':form}
    return render(request,'templates/create.html',context)