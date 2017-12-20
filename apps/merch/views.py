# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def index(request):
    request.session["init"] = True
    if "active_id" in request.session:
        return redirect("/main")
    
    return render(request, "merch/index.html")

def log_reg(request):
    return render(request, "merch/log_reg.html")
def logprocess(request):
    error = False
    incorrect_user = False
    if request.method == "POST":
        error = False
        incorrect_user = False
        email = request.POST["username"]
        alias = request.POST["username"]
        password = request.POST["password"]
        name = User.objects.filter(email=email)
        if len(email) < 0 or len(password) < 0:
            messages.add_message(request, messages.INFO, "Please Input All Fields")
            error = True
        all_user = User.objects.all()

        if len(all_user) < 1:
            messages.add_message(request, messages.INFO, "No users in database")
            error = True
        for user in all_user:
            if user.email != email or user.password != password:
                error = True
                incorrect_user = True
            elif user.email == email and user.password == password:
                error = False
                incorrect_user = False
                break
            if user.alias == alias or user.password != password:
                error = True
                incorrect_user = True
            elif user.alias == alias and user.password == password:
                error = False
                incorrect_user = False
                

        if incorrect_user == True:
            messages.add_message(request, messages.INFO, "Invalid Username/Password.")

        if error == True:
            return redirect("/log_reg")    

        
        request.session["context"] = {
            "name" : name[0].name,
            "email" : email,
            "password" : password
           
        }
        print "hey"
        active_user = User.objects.filter(email=email)
        request.session["active_id"] = active_user[0].id
        

    return redirect("/main")
def regprocess(request):
    error = False
    all_users = User.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        alias = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        error = False
        if len(email) < 0 or len(password) < 0 or len(name) < 0 or len(alias) < 0:
            messages.add_message(request, messages.INFO, "Please Input All Fields")
            error = True
        if len(password) < 8:
            messages.add_message(request, messages.INFO, "Passwords must be longer than 8 characters")
            error = True
        if password != confirm:
            messages.add_message(request, messages.INFO, "Passwords must match")
            error = True
        if not re.match(EMAIL_REGEX, email):
            messages.add_message(request, messages.INFO, "Email must be in proper format")
            error = True
        for user in all_users:
            if user.email == email:
                messages.add_message(request, messages.INFO, "User already exists with that email address.  Please select a new email and try again.")
                error = True
            if user.alias == alias:
                messages.add_message(request, messages.INFO, "User already exists with that alias.  Please select a new alias and try again.")
                error = True

        if error == True:
            print "There was an error numnuts"
            return redirect("/log_reg")

        request.session["context"] = {
            "name" : name,
            "alias" : alias,
            "email" : email,
            "password" : password,
            "confirm" : confirm
        }
        User.objects.create(name=name,alias=alias, email=email, password=password)
        active_user = User.objects.filter(email=email)
        request.session["active_id"] = active_user[0].id
        return redirect("/main")
    else:
        return redirect("/log_reg")

    return redirect("/main")

def main(request):
    active_id = request.session["active_id"]
    active_user = User.objects.get(id=active_id)
    videos = Video.objects.all()
    pics = Print.objects.all()
   
    context= {
        "videos" : videos,
        "pics" : pics
    }
    return render(request, "merch/main.html", context)

def logout(request):
    del request.session["active_id"]
    return redirect("/")

# Create your views here.
