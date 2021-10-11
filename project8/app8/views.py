from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    print(dir(request.session))
    request.session.set_test_cookie()
    return HttpResponse('<h1>Heellooo</h1>')


def delete_coki(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse('<h1>Cokkei worked</h1>')
    return HttpResponse('<h1>Not worked</h1>')


def count_view(request):
    print("++++++++++===COKEIIEE +++++++++")
    print(request.COOKIES)
    print("+++++++++++++++++++")
    if 'count' in request.COOKIES:
        newcount = int(request.COOKIES['count']) + 1
    else:
        newcount = 1
    response = render(request, 'count.html', {'counter': newcount})
    response.set_cookie('count', newcount)
    return response


def page_count_view(request):
    count = request.session.get('count', 0)
    newcount = count+1
    request.session['count'] = newcount
    request.session.get('countqw', 0)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request, 'pagecount.html', {'count': newcount})
