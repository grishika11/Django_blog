from django.urls import path,include
from . import views
from core import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = 'core'

urlpatterns = [
              path('',views.IndexView.as_view(), name='index'),
              path('post/',views.PostView.as_view(), name='post'),
              path('add/',views.AddView.as_view(), name='add'),
              path('admin_login/',views.LoginView.as_view(template_name='admin_login.html'), name='admin_login'),
              path('<slug:slug>/',views.SingleView.as_view(), name ='single'),
              path('edit/<int:pk>',views.EditView.as_view(), name='edit'),
              path('delete/<int:pk>',views.Delete.as_view(), name='delete'),
              #path('logout',views.Logout, name='logout'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


