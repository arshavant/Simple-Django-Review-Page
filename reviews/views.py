from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
from .models import Review

# Create your views here.


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_data = Review(
                username=form.cleaned_data['username'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
            review_data.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        'form': form
    })


def thank_you(request):
    return render(request, 'reviews/thank-you.html')
