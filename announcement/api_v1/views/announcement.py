from django.shortcuts import render


def home_page_generate(request, *args, **kwargs):
    return render(request, 'announcement/home_page.html')