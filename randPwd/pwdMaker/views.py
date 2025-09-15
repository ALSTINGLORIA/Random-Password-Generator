from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request, 'pwdMaker/home.html')

def submit(request):
    size = int(request.POST.get('length'))
    letter = request.POST.get('include_letters')
    digit = request.POST.get('include_digits')
    special = request.POST.get('include_special_chars')
    option = []
    if letter == 'on':
        option.append(1)
    if digit == 'on':
        option.append(2)
    if special == 'on':
        option.append(3)

    password = ""

    for x in range(size):
        choice = random.choice(option)
        if choice == 1:
            if random.randint(0,1) == 0:
                password += chr(random.randint(65, 90))  
            else:
                password += chr(random.randint(97, 122))
        elif choice == 2:
            password += chr(random.randint(48, 57))
        elif choice == 3:
            password += chr(random.randint(33, 47))
    
    return render(request,'pwdMaker/submit.html', {'password':password})
