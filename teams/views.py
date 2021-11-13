from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView

from .models import Team
from .forms import TeamForm

class TeamListView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'teams/team_list.html'

    def get(self, request):
        if request.user.is_staff:
            team_list = Team.objects.all()
            self.form = TeamForm()
            return render(request, self.template_name, 
                {'form': self.form, 'team_list': team_list})
        else:
            messages.add_message(request, messages.WARNING,
                'You must be logged in to create a new team.')
            return HttpResponseRedirect(reverse('home'))

    def post(self, request):
        # Create new instance of form
        self.form = TeamForm(request.POST)
        if self.form.is_valid():
            # Save model to database
            new_team = self.form.save()

            # Add success message
            messages.add_message(request, messages.SUCCESS,
                'Team ' + str(new_team) + ' created.')
            self.form = TeamForm()

        team_list = Team.objects.all()
        return render(request, self.template_name, 
            {'form': self.form, 'team_list': team_list})

class TeamDetailView(DetailView):
    model = Team
    context_object_name = 'team'
    template_name = 'teams/team_detail.html'
