from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime
from datetime import datetime
from random import randint
# Create your views here.
  # the index function is called when root is visited
def index(request):
	# request.session.flush()
	if "gold" not in request.session:
		request.session["gold"] = 0
	if "activity" not in request.session:
		request.session["activity"] = []

	context = {
	'gold': request.session["gold"],
	# "place": request.session["place"]
	}
	print request.session["gold"], "0"
	return render(request,'ninjaGold_app/index.html', context)


def process(request):
	print request.session["gold"], "1"
	new_activity = {}
	if request.POST['place'] == "farm":
		new_activity['gold'] = randint(10,20)
		request.session["gold"]+=new_activity['gold']
		new_activity["place"]=request.POST["place"]
	if request.POST['place'] == "cave":
		new_activity['gold'] =randint(5,10)
		request.session["gold"]+=new_activity['gold']
		new_activity["place"]=request.POST["place"]
	if request.POST['place'] == "house":
		new_activity['gold']=randint(2,5)
		request.session["gold"]+=new_activity['gold']
		new_activity["place"]=request.POST["place"]
	if request.POST['place'] == "casino":
		new_activity['gold'] =randint(-50,50)
		request.session["gold"]+=new_activity['gold']
		new_activity["place"]=request.POST["place"]

	new_activity['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")

	temp_list = request.session['activity']
	temp_list.append(new_activity)
	request.session['activity'] = temp_list
	print request.session["gold"], "2"

	return redirect('/')

def clear(request):
    request.session["gold"] = 0
    for key in request.session.keys():
        del request.session[key]
    return redirect('')