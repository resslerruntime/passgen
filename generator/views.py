from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
def home(request):

    password_characters = string.ascii_letters + string.digits + string.punctuation

    length = 12
    password = ''.join(random.choice(password_characters))

    for x in range(length):
        password += random.choice(password_characters)

    return render(request,'generator/home.html', {'password':password})
