from django.shortcuts import render,redirect
from .models import AllData,Country,State,District,City

def home(request):
	countries = Country.objects.all()
	return render(request,'dropdowns/home.html',{'countries':countries})

def load_states(request):
    countryId = request.GET.get('country')
    states = State.objects.filter(country_id=countryId).order_by('name')
    return render(request, 'dropdowns/states.html', {'states': states})

def load_districts(request):
   stateId = request.GET.get('state')
   districts = District.objects.filter(state_id=stateId).order_by('name')
   return render(request, 'dropdowns/districts.html', {'districts': districts})

def load_cities(request):
   districtID = request.GET.get('city')
   cities = City.objects.filter(district_id=districtID).order_by('name')
   return render(request, 'dropdowns/cities.html', {'cities': cities})

def save_data(request):
	alldata = AllData()
	alldata.country_id = int(request.POST['countries'])
	alldata.state_id = int(request.POST['state'])
	alldata.district_id = int(request.POST['district'])
	alldata.city_id = int(request.POST['city'])
	alldata.save()
	return redirect('data')

def data(request):
	data = AllData.objects.order_by('-id')[:8]
	return render(request,'dropdowns/data.html',{'datas':data})

