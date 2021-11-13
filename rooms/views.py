from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView

from .models import Room
from .forms import RoomForm

class RoomListView(ListView):
    model = Room
    context_object_name = 'room_list'
    template_name = 'rooms/room_list.html'

    def get(self, request):
        if request.user.is_staff:
            room_list = Room.objects.all()
            self.form = RoomForm()
            return render(request, self.template_name, 
                {'form' : self.form, 'room_list': room_list})
        else:
            messages.add_message(request, messages.WARNING,
                'You must be logged in to create a new room.')
            return HttpResponseRedirect(reverse('home'))


    def post(self, request):
        # Create new instance of form
        self.form = RoomForm(request.POST)
        if self.form.is_valid():
            # Save model to database
            new_room = self.form.save()

            # Add success message
            messages.add_message(request, messages.SUCCESS, 
              'Room ' + str(new_room) + ' created.')

            self.form = RoomForm()
            room_list = Room.objects.all()

            return render(request, self.template_name, 
                {'form': self.form, 'room_list': room_list})

        room_list = Room.objects.all()
        return render(request, 'rooms/room_creation.html', 
            {'form': self.form, 'room_list': room_list})
