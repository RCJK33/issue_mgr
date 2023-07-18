from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Issue

from .models import Status
from accounts.models import Role
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IssueListView(ListView):
    model = Issue
    template_name = 'issues/list.html'
    context_object_name = 'issues'


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/detail.html'
    context_object_name = 'issue'


class IssueUpdateView(UpdateView):
    model = Issue
    template_name = 'issues/edit.html'
    fields = ['summary', 'description', 'status',
              'priority', 'assignee', 'reporter']
    success_url = reverse('issues_list')


class IssueCreateView(CreateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Issue
    template_name = 'issues/create.html'
    fields = ['summary', 'description', 'status',
              'priority', 'assignee', 'reporter']
    success_url = reverse('issues_list')

    def test_func(self):
        po = Role.objects.get(name='product owner')
        return self.request.user.role == po


class IssueDeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    model = Issue
    template_name = 'issues/delete.html'
    # success_url = reverse('issues_list')

    def test_func(self):
        po = Role.objects.get(name='product owner')
        done_status = Status.objects.get(name='done')
        issue = self.get_object()
        if issue.status == done_status and self.request.user.role == po:
            return True
        return False
