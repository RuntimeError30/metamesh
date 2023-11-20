"""
URL configuration for uiumetamesh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from metamesh import views
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.indexPage, name="login"),
    path("signup/", views.signupPage, name="signup"),
    path("post_signup/", views.post_sign, name="po_sign"),
    path("validate/", views.validate_user, name='validate'),
    path("dashboard/<str:user>", views.dashboard, name='dashb'),
    path("postit/<str:user>", views.postText, name='postit'),
    path("likeit/", views.likeit, name='likeit'),
    path('logout/<str:user>', views.logout, name="logout"),
    path('club/<str:user>', views.club, name="club"),
    path('addclub/<str:user>', views.createClub, name='addclub'),
    path('clubapprove/<str:user>/<str:club>', views.clubApprove, name='approval'),
    path('clubdash/<str:user>/<str:club>', views.clubDash, name='cdash'),
    path('posthandle/<str:user>/<str:club>', views.clubposthandling, name='phandle'),
    path('doapporve/<str:club>/<str:student>', views.doapprove, name='doapprove'),
    path('likeclubpost/', views.likeclubpost, name='likeclubpost'),
    path('refreeshchat/<str:user>', views.refreshchat, name='refchat'),
    path('eventadd/<str:user>/<str:club>', views.event, name='createevent'),
    path('comment/', views.comment, name='comment'),
    path('notice/<str:user>', views.notice, name='notice'),
    path('catss/<str:user>', views.categorize, name='categorize'),
    path('sendmsg/<str:user>', views.sendmsg, name='sendmsg'),
    path('getmsg/<str:user>', views.getmsg, name='getmsg'),
    path('commnt/<str:user>', views.comment, name='commentit'),
    path('getbig/<str:user>', views.getbig, name='getbig'),
    path('profile/<str:user>', views.profile, name='profile'),
    path('vdetails/<str:user>', views.viewDetails, name='vdetails'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
