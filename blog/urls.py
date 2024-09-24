from django.urls import path 
from .views import *
#,PostDatail,SignupPage,LogoutUser,loginPage,contactPage
urlpatterns=[
    path('',HomePage,name='home'),
    # path('rasm/',RasmPage,name='rasm'),
    path('onatili/',OnatiliPage,name='onatili'),
    path('uy/',uyPage,name='uyish'),
    path('royhat/',OquvchiPage,name="royhat"),
    path('test/',TestPage,name='test'),
    path('matem/',Matem,name='matem')

]

