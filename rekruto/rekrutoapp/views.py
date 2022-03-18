from django.shortcuts import render

# Create your views here.
def hi(request):
    name = request.GET.get('name', 'Rekruto')
    message = request.GET.get('message', 'Давай дружить')
    print('\nTest function\n')
    print('Request:')
    print(request)
    print('Name:')
    print(name)
    print('Message:')
    print(message)
    return render(request, 'rekrutoapp/index.html', {'name': name, 'message': message})
