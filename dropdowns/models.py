from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class District(models.Model):
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class City(models.Model):
	district = models.ForeignKey(District, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class AllData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return str(self.country)

    