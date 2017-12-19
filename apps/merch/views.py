# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    request.session["init"] = True
    if "user_id" in request.session:
        return redirect("/main")
    
    return render(request, "merch/index.html")

def login(request):
    return render(request, "merch/log_reg.html")
def logprocess(request):
    return redirect("/main")


def register(request):
    return render(request, "merch/log_reg.html")
def regprocess(request):
    return redirect("/main")

def main(request):
    return render(request, "merch/main.html")

def logout(request):
    return redirect("/")

# Create your views here.
