from django.urls import path
from .views import (HomePageView, AboutPageView, AppointmentListView,
                    AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView,
                    AppointmentDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', AppointmentListView.as_view(), name='blog'),
    path('blog/<int:pk>', AppointmentDetailView.as_view(), name='blog_detail'),
    path('blog/create', AppointmentCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', AppointmentUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', AppointmentDeleteView.as_view(), name='blog_delete'),
]