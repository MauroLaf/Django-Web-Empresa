from .models import Link 

def context_dict_link(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context