from django.urls import path
from .views import IssueCreateView, IssueDetailView, IssueListView, IssueDeleteView, IssueUpdateView

urlpatterns = [
    path('', IssueListView.as_view(), name='issues_list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issues_detail'),
    path('new/', IssueCreateView.as_view(), name='issues_new'),
    path('<int:pk>/edit/', IssueUpdateView.as_view() , name='issues_edit'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='issues_delete'),
]