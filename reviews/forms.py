from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(min_length=5, label="username", error_messages={
        'required': 'Please enter your username',
        'min_length': 'The minimum length of usernames are 5',
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)



