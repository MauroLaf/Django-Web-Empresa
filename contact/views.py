from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm #instanciamos
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) #si viene por POST el form lo completamos con los datos que vino por POST
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
            "La Caffettiera: Nuevo mensaje de contacto",
            f"De {name} <{email}>\n\nEscribió:\n\n{content}",
            "no-contestar@ginbox.mailtrap.io",       # Emial non reply
            ["maurojoaquinlafuente@gmail.com"],
            reply_to=[email]           # El email del usuario para responderle
)
            try:
                 # Todo ha ido bien, redireccionamos a Ok
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a Fail
                return redirect(reverse('contact')+"?fail")
            
    return render(request, "contact/contact.html",{'form':contact_form}) #una vez instanciado enviamos al template en un dict context llamando a la clave form:y le pasamos contact_form