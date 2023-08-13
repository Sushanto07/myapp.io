from django.shortcuts import render
from django.http import HttpResponse
import os

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Saving to a text file with the username as the filename
        file_path = f'media/user_data/{username}.txt'
        with open(file_path, 'w') as file:
            file.write(f'Username: {username}\nPassword: {password}')

        return HttpResponse('Login data saved successfully!')

    return render(request, 'login.html')
