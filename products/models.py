from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    pub_date =models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=1)
    #if user is deleted then delete product he entered
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)

    #name of title in adming panel
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:160]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
