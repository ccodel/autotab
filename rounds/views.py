from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView

from .models import *
from .forms import *

class RoundsView(TemplateView):
    model = Pairing
    context_object_name = 'pairing'
    template_name = 'rounds/rounds.html'

    def get(self, request):
        if request.user.is_staff:
            pairing_list = Pairing.objects.all()
            self.form = PairingForm()
            return render(request, self.template_name,
                {'form': self.form, 'pairing_list': pairing_list})
        else:
            messages.add_message(request, messages.WARNING,
                'You must be logged in to create a new team.')
            return HttpResponseRedirect(reverse('home'))

    def post(self, request):
        # Create a new instance of the pairing form
        print(request.POST)
        self.form = PairingForm(request.POST)
        if self.form.is_valid():
            p = self.form.save()
            messages.add_message(request, messages.SUCCESS,
                'Pairing for ' + p.pros_str() + ' and ' + p.def_str() + ' created.')
            self.form = PairingForm()

        pairing_list = Pairing.objects.all()
        return render(request, self.template_name,
            {'form': self.form, 'pairing_list': pairing_list})

class PairingDetailView(DetailView):
    model = Pairing
    context_object_name = 'pairing'
    template_name = 'rounds/pairing_detail.html'

    def get(self, request, pk):
        if request.user.is_staff:
            self.pairing = Pairing.objects.get(pk=pk)
            self.ballot_form = BallotForm()
            self.ranking_form = RankingsForm(initial={'pairing': self.pairing.id})
            return render(request, self.template_name,
                {'ballot_form': self.ballot_form,
                  'ranking_form': self.ranking_form,
                  'pairing': self.pairing,
                  'ranking_list': self.pairing.rankings})
        else:
            messages.add_message(request, messages.WARNING,
                'You must be logged in to create a new team.')
            return HttpResponseRedirect(reverse('home'))

    def post(self, request, pk):
        print(request.POST)
        self.pairing = Pairing.objects.get(pk=pk)
        if 'ballot1_score' in request.POST:
            self.ballot_form = BallotForm(request.POST)
            if self.ballot_form.is_valid():
                self.pairing.ballot1_score = request.POST.get('ballot1_score')
                self.pairing.ballot1_initials = request.POST.get('ballot1_initails')
                self.pairing.ballot2_score = request.POST.get('ballot2_score')
                self.pairing.ballot2_initials = request.POST.get('ballot2_initials')

                self.pairing.save()

                messages.add_message(request, messages.SUCCESS,
                    'Scores saved successfully.')
        elif 'ranks' in request.POST:
            print(request.POST)
            self.ranking_form = RankingsForm(request.POST)
            if self.ranking_form.is_valid():
                self.ranking_form.save()
        
        self.ranking_form = RankingsForm(initial={'pairing': self.pairing})
        self.ballot_form = BallotForm()

        return render(request, self.template_name,
                {'ballot_form': BallotForm(),
                  'ranking_form': self.ranking_form,
                  'pairing': self.pairing,
                  'ranking_list': self.pairing.rankings})

