from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Apps(models.Model):
    c_choices=(('UPI','upi'),('CRYPTO','crypto'),('STOCK&MUTUALFUND','stock&mutualfund'),('OTHERS','others'),('RUMMY&FANTACY','rummy&fantacy'))
    no=models.IntegerField()
    appname=models.CharField(max_length=128)
    logo=models.FileField(null=True,blank=True,upload_to="images/")
    slug=models.SlugField(max_length=128,unique_for_date='publish')
    category=models.CharField(max_length=17,choices=(c_choices),default='others')
    home_description=models.TextField()
    detail_description=models.TextField()
    steps=models.TextField()
    andriod_link=models.CharField(max_length=10000)
    andriod_rate=models.FloatField()
    total_andownloads=models.IntegerField()
    total_iosdownloads=models.IntegerField()
    ios_link=models.CharField(max_length=10000,null=True,blank=True)
    ios_rate=models.FloatField(null=True,blank=True)
    publish=models.DateTimeField(timezone.now)

    class Meta:
        ordering=['-no']

    def __str__(self):
        return self.appname  

    def get_absolute_url(self):
        return reverse('app_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])      


