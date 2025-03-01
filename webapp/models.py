from django.db import models

class services(models.Model):
    name=models.CharField(max_length=100);
    email=models.CharField(max_length=100);
    phno=models.CharField(max_length=100);
    fast_charge=models.IntegerField();
    normal_charge=models.IntegerField();
    fast_cost=models.IntegerField();
    normal_cost=models.IntegerField();
    adrs=models.CharField(max_length=200);
    city=models.CharField(max_length=100);
    latitude=models.CharField(max_length=100);
    longitude=models.CharField(max_length=100);
    password=models.CharField(max_length=100);


class user(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	phone=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);


class userloc(models.Model):
	email=models.CharField(max_length=100);
	lat=models.CharField(max_length=100);
	lon=models.CharField(max_length=100);
	

class temp(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	phno=models.CharField(max_length=100);
	fast_charge=models.IntegerField();
	normal_charge=models.IntegerField();
	fast_cost=models.IntegerField();
	normal_cost=models.IntegerField();
	adrs=models.CharField(max_length=200);
	city=models.CharField(max_length=100);
	latitude=models.CharField(max_length=100);
	longitude=models.CharField(max_length=100);
	dist=models.FloatField();

