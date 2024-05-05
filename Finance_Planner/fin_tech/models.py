from django.db import models

class PersonalDetails(models.Model):
  name = models.CharField(db_column='Name', max_length=255)
  birthyear = models.CharField(db_column='BirthYear', max_length=255)
  age = models.CharField(db_column='Age', max_length=255)
  gender = models.CharField(db_column='Gender', max_length=255)
  profession = models.CharField(db_column='Profession', max_length=255)
  
  def __str__(self):
        return self.name
  
