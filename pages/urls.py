from django.urls import path
from .views import HomePageView, AboutPageView, ContactCreateView, OurServicesView, FaqView, ImprintView,\
                    DataProtectionView, BecomeMentorView, MentorsView, MentorDetailView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactCreateView.as_view(), name='contact'),
    path('faq', FaqView.as_view(), name='faq'),
    path('imprint', ImprintView.as_view(), name='imprint'),
    path('data-protection', DataProtectionView.as_view(), name='data-protection'),
    path('our-services', OurServicesView.as_view(), name='our-services'),
    path('become-mentor', BecomeMentorView.as_view(), name='become-mentor'),
    path('mentors', MentorsView.as_view(), name='mentors'),
    path('mentor-detail', MentorDetailView.as_view(), name='mentor-detail'),

]