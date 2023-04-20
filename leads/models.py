from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    inbox_token = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Lead(models.Model):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    date = models.DateTimeField
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name