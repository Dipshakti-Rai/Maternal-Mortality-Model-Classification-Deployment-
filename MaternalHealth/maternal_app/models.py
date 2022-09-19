from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class HealthPrediction(models.Model):
    patient_id = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    date_of_birth=models.DateField(auto_now=False)
    contact_num = models.IntegerField()
    age_group = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(11)])
    systolic_bp = models.PositiveIntegerField(default=False)
    diastolic_bp = models.PositiveIntegerField(default=False)
    blood_sugar = models.FloatField(default=False)
    body_temp = models.FloatField(default=False)
    heart_rate = models.PositiveIntegerField(default=False)

    class Meta:
        db_table = "MaternalHealth"

    def __str__(self):
        return self.patient_id

class PostNews(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField()
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "PostNews"
        ordering=('-create_at',)
    

    def __str__(self):
        return self.title
