from django.shortcuts import render


rooms = [
    { 'id':1, 'name': 'lets learn django'},
    { 'id':2, 'name': 'from scratch'},
    { 'id':3, 'name': 'by looking at youtube'},
]

def home(request):
    return render(request,'home.html', {'rooms': rooms})

def room(request, val):
    room = None
    for i in rooms:
        if i['id'] == val:
            room = i
        context={'room':room}
    return render(request,'room.html', context)
