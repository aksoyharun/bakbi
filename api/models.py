from django.db import models

# Create your models here.
class Trade(models.Model):
    ''' This model represents a operation type '''

    currency=models.CharField(max_length=250,blank=False,null=False)
    value=models.FloatField()
    cdate=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Para Tipleri"
        verbose_name='Para Tipi'
        ordering=['-cdate']
        
