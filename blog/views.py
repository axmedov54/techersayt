from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import login,logout,authenticate
from .models import *
# ,redirect




def OquvchiPage(request):
    return render(request, 'o`quvchilar.html')


def HomePage(request):
    return render(request, 'base.html')



def RasmPage(request):
    return render(request, 'rasm.html')

def uyPage(request):
    
    return render(request, 'uyishlari.html')

def TestPage(request):
    return render(request, 'testlar.html')


#
# def contactPage(request):
#     contact=Contact()
#     if request.method == 'POST':
#        contact.username=request.POST.get('name')
#        contact.email=request.POST.get('email')
#        contact.message=request.POST.get('message')
#        contact.save()
#        print('Contact Saqlandi')
#        return render (request,'contact.html')




def Matem(request):
    Posts = Matematika.objects.all()
    return render(request,'vazifa.html',{'post':Posts})

def OnaltliPage(request):
    Onatili = Onnatili.objects.all()
    return render(request, 'onatili.html',{'onatili':Onatili})



# def SignupPage(request):

#     if request.method == 'POST':
#       username = request.POST.get('YourName')
#       useremail = request.POST.get('YourEmail')
#       password = request.POST.get('Password')
#       password2 = request.POST.get('Password2')
#       if password==password2:
#           password= request.POST.get('Password')
#           user=User.objects.create_user(username=username,email=useremail,password=password)
#           login(request, user)
#           return redirect('home')     
#     return render (request,'singnup.html')

# def loginPage(request):
#     if request.method =='POST':
#         username = request.POST.get('YourName')
#         password = request.POST.get('Passwordl')
#         user= authenticate(request,username=username,password=password)
        
#         if user is not None:
#             login(request,user)
#         return redirect('home')

#     return render(request,'login.html')


# def LogoutUser(request):
#     logout(request)
#     return redirect('home')

