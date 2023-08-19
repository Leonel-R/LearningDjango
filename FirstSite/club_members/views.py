from django.http import HttpResponse
from django.template import loader
from .models import Member 

def club_members(request):
	club_members = Member.objects.all()
	template = loader.get_template('all_members.html')	
	context = {
    'club_members': club_members,
  }
	return HttpResponse(template.render(context, request))

def details(request, id):
	club_member = Member.objects.get(id=id)
	template = loader.get_template('details.html')
	context = {
	'club_member': club_member,
	}
	return HttpResponse(template.render(context, request))
 
