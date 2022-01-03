from django.shortcuts import render
from django.views.generic import View
# Create your views here

class Home(View):
    """
    Description: Model Description
    """
    
    template_name = "core/index.html"
    
    def get(self, request, *args, **kwargs):
    	
    	context = {}

    	return render(request, self.template_name, context=context)