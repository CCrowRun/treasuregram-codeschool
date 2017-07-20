from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm

# Create your views here.
#Home page view - displays grid
def index(request):
	treasures = Treasure.objects.all()
	form = TreasureForm()
	return render(request, 'index.html', {'treasures': treasures, 'form': form})

#Detail triggered by selecting a treasure from Home
def detail(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request, 'detail.html', {'treasure': treasure})

#Form to add additional items to treasures
def post_treasure(request):
	form = TreasureForm(request.POST, request.FILES)
	if form.is_valid():
		form.save(commit = True)
	return HttpResponseRedirect('/')