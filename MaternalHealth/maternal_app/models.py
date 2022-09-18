from django.db import models

# Create your models here.

class HealthPrediction(models.Model):
    patient_id = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    date_of_birth=models.DateField(auto_now=False)
    contact_num = models.IntegerField()
    age_group = models.IntegerField()
    systolic_bp = models.IntegerField()
    diastolic_bp = models.IntegerField()
    blood_sugar = models.IntegerField()
    body_temp = models.IntegerField()
    heart_rate = models.IntegerField(default=False)

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
