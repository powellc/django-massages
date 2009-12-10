from django.shortcuts import get_list_or_404, render_to_response, get_object_or_404
from django.template import RequestContext
from massages.models import Massage, RateList

def index(request):
	massages=Massage.objects.filter(active=True)
	ratelist=RateList.objects.get(active=True)
	return render_to_response('massages/index.html', locals(), 
						context_instance=RequestContext(request))

def massage_detail(request, slug):
	massage=get_object_or_404(Massage, slug=slug)
	return render_to_response('massages/massage_detail.html', locals(), 
						context_instance=RequestContext(request))
	