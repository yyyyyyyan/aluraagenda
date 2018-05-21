from django.http import HttpResponse
from .models import Contatos

def index(request):
	html = "<html><body>"
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
		html += "Contato não encontrado :("
	else:
		html += "{} - {}<br>".format(contato.nome, contato.telefone)
	finally:
		html += "</body></html>"

	return HttpResponse(html)