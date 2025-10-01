from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import myadmin
from faculty.models import faculty
# Create your views here.
# Main pages
def myadmin_home(request):
     admin_id = request.session.get("admin_id")
     if not admin_id:
        return redirect("myadmin_index")

     current_admin = myadmin.objects.get(myadmin_id=admin_id)
     return render(request, "myadmin/home.html", {"admin": current_admin})




def myadmin_index(request):
    if request.method == "POST":
        login_type = request.POST.get("login_type")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if login_type == "myadmin":
            user = myadmin.objects.filter(username=username, password=password).first()
            if user:
                request.session["admin_id"] = user.myadmin_id   # use your custom PK
                request.session["admin_username"] = user.username
                return redirect("myadmin_home")
    # admin dashboard
            else:
                messages.error(request, "Invalid admin credentials")

        elif login_type == "faculty":
            user = faculty.objects.filter(username=username, password=password).first()
            if user:
                request.session["faculty_id"] = user.id
                request.session["role"] = "faculty"
                return redirect("faculty_home")  # faculty dashboard
            else:
                messages.error(request, "Invalid faculty credentials")

    return render(request, "myadmin/index.html")  # your login template

def myadmin_register(request):
    return render(request, "myadmin/register.html")

def myadmin_prediction(request):
    return render(request, "myadmin/prediction.html")

def myadmin_faculty(request):
    return render(request, "myadmin/faculty.html")

def myadmin_data(request):
    return render(request, "myadmin/data.html")


# Branch pages
def myadmin_branch_aiml(request):
    return render(request, "myadmin/branch/aiml.html")

def myadmin_branch_com(request):
    return render(request, "myadmin/branch/com.html")

def myadmin_branch_it(request):
    return render(request, "myadmin/branch/it.html")

def myadmin_branch_mech(request):
    return render(request, "myadmin/branch/mech.html")

def myadmin_branch_civil(request):
    return render(request, "myadmin/branch/civil.html")

def myadmin_branch_auto(request):
    return render(request, "myadmin/branch/auto.html")
