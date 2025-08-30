from django.urls import path
from . import views

urlpatterns = [
    path('draft', views.index, name='index'),
    path("fetch_drafts", views.fetch_draft_tickets, name="fetch_drafts"),
    path('jira_ticket', views.jira_issue_creation, name='jira_ticket_creation'),
    path('twilio_test', views.twilio_test, name='twilio_test'),    
]