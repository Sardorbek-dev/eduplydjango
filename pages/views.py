from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactCreateView(TemplateView):
    template_name = 'contact.html'

class OurServicesView(TemplateView):
    template_name = 'our-services.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class ImprintView(TemplateView):
    template_name = 'imprint.html'

class DataProtectionView(TemplateView):
    template_name = 'data-protection.html'

class BecomeMentorView(TemplateView):
    template_name = 'become-mentor.html'

class MentorsView(TemplateView):
    template_name = 'mentors.html'

class MentorDetailView(TemplateView):
    template_name = 'mentor-detail.html'

class EventsView(TemplateView):
    template_name = 'events.html'

class EventDetailView(TemplateView):
    template_name = 'event-detail.html'


class PageNotFoundView(TemplateView):
    template_name = 'page-not-found.html'

