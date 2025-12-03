from django.shortcuts import render
from .forms import ContactForm

def portfolio(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get cleaned form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # For now, just print to console
            print("Message received:", name, email, message)

            return render(request, "index.html", {
                "form": ContactForm(),
                "success": True
            })

    return render(request, "index.html", {'form': form})