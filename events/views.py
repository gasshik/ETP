from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import EventForm
from .models import Event


def event_list(request):
    now = timezone.now().date()

    ongoing_events = Event.objects.filter(start_date__lte=now, end_date__gte=now)

    upcoming_events = Event.objects.filter(start_date__lte=now).order_by("start_date")

    return render(
        request,
        "events/events_list.html",
        {"ongoing_events": ongoing_events, "upcoming_events": upcoming_events},
    )

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    
    return render(request, 'events/event_form.html', {'form': form})
