from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
	return render(request, 'index.html')


def service(request):
	return render(request, 'service.html')


def servicesignup(request):
	return render(request, 'servicesignup.html')

def usersignup(request):
	return render(request, 'usersignup.html')



def signupstore(request):
	email=request.POST['email']
	pwd=request.POST['pwd']
	name=request.POST['name']
	phone=request.POST['phone']
	
		
	
	d1=user.objects.filter(email__exact=email).count()
	if  d1>0:
		return render(request, 'usersignup.html',{'msg':"Email Already Registered"})
	else:
		d=user(name=name,email=email,pwd=pwd,phone=phone)
		d.save()
		d=userloc(lat='0.0',lon='0.0', email=email)
		d.save()
		return render(request, 'usersignup.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'usersignup.html',{'msg':"Register Success, You can Login.."})



def addpoi(request):
	if request.method=='POST':
		service=request.POST["bsnm"]
		phno=request.POST['phno']
		
		
		nf=request.POST['nf']
		nn=request.POST['nn']
		cf=request.POST['cf']
		cn=request.POST['cn']
		
		
		email=request.POST['email']
		adrs=request.POST['adrs']
		city=request.POST['city']
		password=request.POST['password']
		latitude=request.POST['latitude']
		longitude=request.POST['longitude']

		d=services(name=service,phno=phno,email=email,adrs=adrs,\
		normal_charge=nn, fast_charge=nf, fast_cost=cf, normal_cost=cn,password=password, latitude=latitude,longitude=longitude, city=city)
		d.save()

		return render(request, 'servicesignup.html',{'msg':"EV station added Successfully"})


	else:
		return render(request, 'servicesignup.html')


def servicelogin(request):
	if request.method=='POST':
		uid=request.POST['email']
		pwd=request.POST['pwd']
		d=services.objects.filter(email__exact=uid).filter(password__exact=pwd).count()
		
		if d>0:
			d=services.objects.filter(email__exact=uid)
			request.session['semail']=uid
			
			request.session['sname']=d[0].name
			return render(request, 's_home.html',{'data': d[0]})

		else:
			return render(request, 'service.html',{'msg':"Login Fail"})

	else:
		return render(request, 'service.html')


def userlogin(request):
	if request.method=='POST':
		uid=request.POST['email']
		pwd=request.POST['pwd']
		d=user.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=user.objects.filter(email__exact=uid)
			request.session['uemail']=uid
			
			request.session['uname']=d[0].name
			return render(request, 'u_home.html',{'data': d[0]})

		else:
			return render(request, 'index.html',{'msg':"Login Fail"})

	else:
		return render(request, 'index.html')

def shome(request):
	if "semail" in request.session:
		uid=request.session["semail"]
		d=services.objects.filter(email__exact=uid)
		return render(request, 's_home.html',{'data': d[0]})

	else:
		return render(request, 'service.html')

def viewev(request):
	if "semail" in request.session:
		uid=request.session["semail"]
		d=services.objects.filter(email__exact=uid)
		return render(request, 'viewev.html',{'data': d})

	else:
		return render(request, 'service.html')

def editdata(request):
	if "semail" in request.session:
		uid=request.session["semail"]
		d=services.objects.filter(email__exact=uid)
		return render(request, 'editdata.html',{'data': d})

	else:
		return render(request, 'service.html')

def slogout(request):
	try:
		del request.session['semail']
	except:
		pass
	return render(request, 'service.html')



def uhome(request):
	if "uemail" in request.session:
		uid=request.session["uemail"]
		d=user.objects.filter(email__exact=uid)
		return render(request, 'u_home.html',{'data': d[0]})

	else:
		return render(request, 'index.html')

def ulogout(request):
	try:
		del request.session['uemail']
	except:
		pass
	return render(request, 'index.html')



def updatedata(request):
	if request.method=='POST':
		phno=request.POST['ph']
		uid=request.session["semail"]
		
		
		
		fast_charge=request.POST['fast_charge']
		fast_cost=request.POST['fast_cost']
		normal_charge=request.POST['normal_charge']
		normal_cost=request.POST['normal_cost']
		
		d=services.objects.filter(email=uid).update(phno=phno,normal_charge=normal_charge, fast_charge=fast_charge, fast_cost=fast_cost, normal_cost=normal_cost)


		d=services.objects.filter(email__exact=uid)
		return render(request, 'viewev.html',{'data': d, 'msg':'Data updated !!'})
		
	else:
		return render(request, 'editdata.html')



def viewprofile(request):
    if "uemail" in request.session:
        uid = request.session["uemail"]
        d = user.objects.filter(email=uid)
        d2 = userloc.objects.filter(email=uid)
        return render(request, 'viewprofile.html', {'data': d,'data2': d2,})

    else:
        stz = True
        return render(request, 'index.html', {'msg': "Your session is expired !! ", 'stz': stz})







def locationset(request):
	if request.method=='POST':
		email=request.session['uemail']
		lat=request.POST['latitude']
		lon=request.POST['longitude']
		try:
			instance = userloc.objects.filter(email=email).update(lat=lat, lon=lon)
			
		except:
			pass

		return render(request, 'u_home.html',{'msg':"Your Locaion data updated.. "})

	else:
		return render(request,'current_location.html')



from .haversine_dist import distance
def getdata(request):
	if request.method=='POST':
		cdist=request.POST['dist']
		
		d=services.objects.all()
		t=temp.objects.all().delete()

		uid=request.session['uemail']
		t=userloc.objects.get(email=uid)
		uloc=[t.lat, t.lon]


		for d1 in d:
			dist=distance(uloc, [d1.latitude,d1.longitude])
			d=temp(name=d1.name,phno=d1.phno,email=d1.email,adrs=d1.adrs,normal_charge=d1.normal_charge, fast_charge=d1.fast_charge, fast_cost=d1.fast_cost, normal_cost=d1.normal_cost,latitude=d1.latitude,longitude=d1.longitude, city=d1.city, dist=dist)
			d.save()
		

		d=temp.objects.filter(dist__lte=cdist)
		return render(request, 'viewdata.html',{'data': d, })
		
	else:
		d=services.objects.all()
		t=temp.objects.all().delete()
		uid=request.session['uemail']
		t=userloc.objects.get(email=uid)
		uloc=[t.lat, t.lon]

		for d1 in d:
			dist=distance(uloc, [d1.latitude,d1.longitude])
			d=temp(name=d1.name,phno=d1.phno,email=d1.email,adrs=d1.adrs,normal_charge=d1.normal_charge, fast_charge=d1.fast_charge, fast_cost=d1.fast_cost, normal_cost=d1.normal_cost,latitude=d1.latitude,longitude=d1.longitude, city=d1.city, dist=round(dist, 2))
			d.save()
		

		d=temp.objects.filter(dist__lte=50)
		return render(request, 'viewdata.html',{'data': d})



def viewloc2(request):
	if "uemail" in request.session:
	
		lat=request.GET['lat']
		lon=request.GET['lon']


		return render(request, 'view_loc.html',{'lat':lat,'lon':lon})

	else:
		return render(request,'user.html')


def search(request):
	if request.method=='POST':
		city=request.POST['city']
		
		
		d=services.objects.filter(city__icontains=city)
		return render(request, 'searchdata.html',{'data': d, })
		
	else:
		return render(request, 'search.html',)
