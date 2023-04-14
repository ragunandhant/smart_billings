from django.urls import path
from . import views
app_name = 'transcation'


urlpatterns= [
    path('checkout',views.checkout,name = 'checkout'),
    path('view',views.mytranscation,name="mytranscation"),
    path('download_image',views.download_image,name = 'download_image'),
    path('billng',views.getqr,name='billing')
    
    ]