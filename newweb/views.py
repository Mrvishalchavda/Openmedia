from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "./test1/authenticate/home.html")

def home(request):
    if request.method == "POST":
        if 'userlogin' in request.POST:
            print(request.POST)
            return HttpResponse("user login sucessfully")
        elif 'journalistlogin' in request.POST:
            return HttpResponse("journalist login sucessfully")
    return render(request,"home.html")


def login(request):
    return render(request,"login.html")
def register(request):
    print("ask for page")
    if request.method == 'POST':
        if 'userregister' in request.POST:
            # messages.success(request, 'user profile maked login now')
            return render(request,"register.html")
        elif 'journalistregister' in request.POST:
            # messages.success(request, ' journalist profile maked login now')
            return render(request,"register.html")
        # print("if working")
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # conpassword = request.POST.get("conpassword")
        # email = request.POST.get("email")
        # print(f"name={username} \n password={password} \n conpassword={conpassword}\nemail={email}")
        # user = User.objects.create_user(
        #     username = username,
        #     password = password,
        #     email = email
        #     )
        # user.save( )
        # print("data saved")
        # messages.success(request, 'profile maked login now')
        # return render(request, "login.html")
    else:
        return render(request, "register.html")