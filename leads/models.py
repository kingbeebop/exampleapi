from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    inbox_token = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Lead(models.Model):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    from_first = models.CharField(max_length=200)
    from_last = models.CharField(max_length=200)
    from_message = models.CharField(max_length=1000)
    from_email = models.CharField(max_length=200)
    from_phone = models.CharField(max_length=20)
    referring_url = models.CharField(max_length=200)
    from_source = models.CharField(max_length=200)
    date = models.DateTimeField
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.from_first
    
    #def processed(self):
    #   self.processed = True