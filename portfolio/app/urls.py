from django.urls import path,include
from app import views
# from portfolio import views

urlpatterns = [
    path('',views.index,name='index'),
    path('portfolio-details',views.Portfoliodetails,name='portfolio-details'),
    path('inner-page',views.Innerpage,name='inner-page'),
]