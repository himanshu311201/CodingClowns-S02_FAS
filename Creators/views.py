from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from .models import Event
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required

# Create your views here.


# def togo(request):
#     return redirect('home', request.session.get('po'))

# def home(request):
#     return render(request, 'Creato.html')
@login_required
def home(request, *args, **kwargs):
    try:
        # print("kkk")
        print(request.GET.get('form'))
        # print(pk)
        # print(request['form'])
        # r1 = pk
        r1 = request.GET.get('form')
        request.session['po'] = r1
        name = SocialAccount.objects.get(
            user=request.user).extra_data['name']
        print(name)

        e = Event.objects.get(id=r1).csv_file
        # print(e)
        q = pd.read_csv(e)
        r = q["Full Name"].eq(name).any()
        print(r)
        # r = sessions['h']
        if not r:
            return redirect('login')
        else:
            return redirect('final', r1)
    except:
        return redirect('login')


# class home(LoginRequiredMixin, ListView):
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     print(self.kwargs['pk'])
#     #     return context
#     def __init__(self, **kwargs):
#         self.r = False

#     # def get_queryset(self, *args, **kwargs):
#     #     # try:
#     #     # print(self.request.user)
#     #     name = SocialAccount.objects.get(
#     #         user=self.request.user).extra_data['name']
#     #     print(name)
#     #     r1 = self.kwargs['pk']
#     #     e = Event.objects.get(id=r1).csv_file
#     #     # print(e)
#     #     q = pd.read_csv(e)
#     #     self.r = q["Full Name"].eq(name).any()

#         # self.request.session['h'] = r
#         # self.

#         # print(r)

#         # if not r:
#         #     return redirect('logout')
#         # print("Sorry")

#         # except:
#         #     self.r = False

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             name = SocialAccount.objects.get(
#                 user=self.request.user).extra_data['name']
#             print(name)
#             r1 = self.kwargs['pk']
#             e = Event.objects.get(id=r1).csv_file
#             # print(e)
#             q = pd.read_csv(e)
#             self.r = q["Full Name"].eq(name).any()
#             print(self.r)
#             # r = sessions['h']
#             if not self.r:
#                 return redirect('logout')
#             else:
#                 return redirect('final', r1)
#         except:
#             return redirect('logout')

#     # print(r)


def final(request, po):
    print(po)
    return render(request, 'Creators/creators.html')
