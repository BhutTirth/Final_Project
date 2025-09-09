from django.shortcuts import render

# Create your views here.
# Main pages
def admin_home(request):
    return render(request, "admin/home.html")

def admin_index(request):
    return render(request, "admin/index.html")

def admin_prediction(request):
    return render(request, "admin/prediction.html")

def admin_faculty(request):
    return render(request, "admin/faculty.html")

def admin_data(request):
    return render(request, "admin/data.html")


# Branch pages
def admin_branch_aiml(request):
    return render(request, "admin/branch/aiml.html")

def admin_branch_com(request):
    return render(request, "admin/branch/com.html")

def admin_branch_it(request):
    return render(request, "admin/branch/it.html")

def admin_branch_mech(request):
    return render(request, "admin/branch/mech.html")

def admin_branch_civil(request):
    return render(request, "admin/branch/civil.html")

def admin_branch_auto(request):
    return render(request, "admin/branch/auto.html")
