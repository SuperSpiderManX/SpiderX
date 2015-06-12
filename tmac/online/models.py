from django.db import models

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	role = models.IntegerField()

	def __unicode__(self):
		return self.username

class Group(models.Model):
	groupname = models.CharField(max_length=50)
	user = models.ManyToManyField(User)

	def __unicode__(self):
		return self.groupname

class Machine(models.Model):
	name = models.CharField(max_length=50)
	ip = models.CharField(max_length=50)
	port = models.IntegerField()
	loginuser = models.CharField(max_length=50)
	loginpassword = models.CharField(max_length=50)
	group = models.ManyToManyField(Group)

	def __unicode__(self):
		return self.name
