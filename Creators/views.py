from django.shortcuts import render,redirect
from .forms import Event_form,Question_form
from .models import Event
from User.models import New


# Create your views here.
def index(request):
    return render(request,'Creators/creators.html')
def Question(request,prod_id):
    request.session['p_id'] = prod_id
    Events=Event.objects.filter(pk=prod_id)
    print(Events)
    if request.method == 'POST':
        form = Question_form(request.POST, request.FILES)
        if form.is_valid():
            us = request.user.new.username
            New_user= New.objects.filter(username=us)
            for i in Events:
                Event_at=i
            p = form.save(commit=False)
            p.event_related=Event_at
            print('hello')
            p.save()
            print('hello')
            return redirect('Question',prod_id)
        else:
            print(form.errors)
            return render(request, 'Creators/questions.html', {'form': Question_form})
    else:
        form = Question_form()
    return render(request, 'Creators/questions.html',{'form': Question_form})
def createform(request):
    if request.method == 'POST':
        form = Event_form(request.POST, request.FILES)
        if form.is_valid():
            us = request.user.new.username
            New_user= New.objects.filter(username=us)
            for i in New_user:
                News=i
            p = form.save(commit=False)
            p.creator=News
            print(p.creator)
            print('hello')
            p.save()
            print('hello')
            k=p.pk
            print(k)
            return redirect('Question',k)
        else:
            print(form.errors)
            return render(request, 'Creators/Creator_form.html', {'form': Event_form})
    else:
        form = Event_form()
    return render(request, 'Creators/Creator_form.html',{'form': Event_form})


