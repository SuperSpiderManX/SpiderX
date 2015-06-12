from django.db import models

sex_choices = (
		('f','famale'),
		('m','male'),
)

class Employee(models.Model):
    name = models.CharField(max_length=20)
# Create your models here.
    def __unicode__(self):
        return self.name


class User(models.Model):
	name = models.CharField(max_length=20)
	#sex = models.CharField(max_length=1,choices=sex_choices)
	password = models.CharField(max_length=20)
# Create your models here.
	def __unicode__(self):
		return self.name

class Entry(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class Blog(models.Model):
	name = models.CharField(max_length=30)
	entry = models.ForeignKey(Entry)

	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=30)
	authors = models.ManyToManyField(Author)

	def __unicode__(self):
		return self.name
