from django.http import HttpResponse

def test_view(request):
    print("test view ", request.user)
    return HttpResponse("test success")