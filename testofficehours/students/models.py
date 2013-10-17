from django.db import models

class Student(models.Model):
	
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=150)

	def __unicode__(self):  # Python 3: def __str__(self):
		outputString = "Name: " + str(self.name) + " Description: " + str(self.description)
		return outputString

	def delete_myself(self):
		self.delete()

	def helped_by_staff(self):
		self.delete()

	def helped_by_peer(self, peername):
		self.delete()