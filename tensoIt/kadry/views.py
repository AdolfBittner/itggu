from django.shortcuts import render, redirect
from .models import Kontakti,Otdel

def phonebook(request):

    Contacts = Kontakti.objects.exclude(Otdel = 35)
    Otdl = Otdel.objects.exclude(Otdel = 'УВОЛЕННЫЕ')
    return render(request, 'phonebook.html',{'Contacts':Contacts, 'Otdl':Otdl})

def phonereturn(request):
    return redirect('admin/kadry/kontakti')

def phonebookprint(request):
    pass
