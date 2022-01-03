import datetime
from django.shortcuts import render


def home(request):
    date = datetime.datetime.now().date()
    name = 'Yan BEkker'
    _context = {'date': date, 'name':name}
    return render(request, 'home.html', _context)

def news(request):
    date = datetime.datetime.now().date()
    name = 'Yan Bekker'
    _context = {'date': date, 'name':name}
    return render(request, 'news.html', _context)
