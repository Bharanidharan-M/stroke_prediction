from django.db import models

class React(models.Model):
    age = models.IntegerField()
    hypertension = models.IntegerField()
    heart_disease = models.IntegerField()
    ever_married = models.IntegerField()
    avg_glucose_level = models.IntegerField()
    bmi = models.IntegerField()
    
