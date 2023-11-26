from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserBalance
from django.utils import timezone

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = UserBalance.objects.filter(username=username).first()
        if user:
            if user.expiry_date and user.expiry_date < timezone.now():
                messages.error(request, 'Account has expired. Please contact admin.')
            else:
                return redirect('balance:show_balance', username=username)
        else:
            messages.error(request, 'User does not exist. Contact admin.')
    return render(request, 'balance/home.html')

def show_balance(request, username):
    user = UserBalance.objects.get(username=username)
    return render(request, 'balance/show_balance.html', {'user': user})
def external_page(request):
    # Replace 'https://www.example.com' with the actual external link you want to display
    external_url = 'https://kdc2.000webhostapp.com/index.php'
    return render(request, 'balance/external_page.html', {'external_url': external_url})