from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406434172',
        'name': 'Muhammad Geriya Itsa',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
