from django.shortcuts import render, redirect 
from django.http import JsonResponse 
from django.contrib.auth import authenticate,login as lg,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
import random 

def signup(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1!=p2:
            return redirect('signup')
        user = User.objects.create_user(u,e,p1)
        user.save()
        return redirect('home')
    return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(username=username,password=pass1)
        if user is not None:
            lg(request,user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')
def logout(request):
    return redirect('login')

def home(request): 
	context = {'categories': Category.objects.all()} 
	if request.GET.get('category'): 
		return redirect(f"/quiz/?category={request.GET.get('category')}") 
	return render(request, 'home.html', context) 
def quiz(request): 
	context = {'category': request.GET.get('category')} 
	return render(request, 'quiz.html', context) 
def get_quiz(request): 
	try: 
		question_objs = Question.objects.all() 
		if request.GET.get('category'): 
			question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category')) 
		question_objs = list(question_objs) 
		random.shuffle(question_objs) 
		data = [] 
		for question_obj in question_objs: 
			data.append({ 
				"uid": question_obj.uid, 
				"category": question_obj.category.category_name, 
				"question": question_obj.question, 
				"marks": question_obj.marks, 
				"answer": question_obj.get_answers(), 
			}) 
		payload = {'status': True, 'data': data} 
		return JsonResponse(payload) 
	
	except Exception as e:	 print(e) 
	return HttpResponse("Something went wrong") 
