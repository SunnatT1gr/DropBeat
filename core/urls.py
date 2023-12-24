from django.urls import path
from .views import homeview, ContactView, TrainingsView, ShowsView, ShortcodesView, ClassesView

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('contact/', ContactView.as_view(), name="contact_page"),
    path('training/', TrainingsView.as_view(), name="trainings_page"),
    path('classes/', ClassesView.as_view(), name="classes_page"),
    path('shortcodes/', ShortcodesView.as_view(), name="shortcodes_page"),
    path('shows/', ShowsView.as_view(), name="shows_page")
]