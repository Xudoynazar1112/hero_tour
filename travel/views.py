from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookingForm
from .models import Travel


def main(request):
    travels = Travel.objects.all()
    context = {'travels': travels}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def destinations(request):
    travels = Travel.objects.all()
    context = {'travels': travels}
    return render(request, 'destinations.html', context)


def detail(request, id):
    travel = get_object_or_404(Travel, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = BookingForm()
        return render(request, 'detail.html', {'form': form, 'travel': travel})
