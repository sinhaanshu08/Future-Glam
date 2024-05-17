from django.urls import path
from.import views

urlpatterns = [
    path('chathome',views.Chathome,name='chathome')
]