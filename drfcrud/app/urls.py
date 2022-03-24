from django.urls import path
from app import views

urlpatterns = [
      path('',views.ApiOverview),
      path('create/',views.add_data),
      path('viewall/',views.view_info),
      path('update/<int:pk>/',views.update_items),
      path('item/<int:pk>/delete/',views.delete_data),


]