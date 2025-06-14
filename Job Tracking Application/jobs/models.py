from django.db import models

class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title