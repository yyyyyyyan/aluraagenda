from django.http import HttpResponse
from .models import Contatos

def index(request):
	html = "<html><body><h1>Lista de Contatos</h1>"
	contatos = Contatos.objects.all()
	for contato in contatos:
		html += "{} - {}<br>".format(contato.nome, contato.telefone)
	html += "</body></html>"
	return HttpResponse(html)

def get_contato_by_id(request, contato_id):
	html = "<html><body>"
	
	try:
		contato = Contatos.objects.get(id=contato_id)
	except:
		html += "<h1>Contato não encontrado :(</h1>"
	else:
		html += "{} - {}".format(contato.nome, contato.telefone)
	finally:
		html += "</body></html>"

	return HttpResponse(html)