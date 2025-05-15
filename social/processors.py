from .models import Link 

def context_dict(request):
    context_dict = {}
    links = Link.objects.all()
    for link in links:
        context_dict[link.key] = link.url
    return context_dict