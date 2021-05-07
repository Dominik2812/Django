
from django.db import models
from django.urls import reverse

# Create your models here.
class Bubble(models.Model):
    topic=models.CharField(max_length=200)
    bubbs = models.ManyToManyField('self', blank=True,related_name='bubbles',db_column='relatedBubbles',symmetrical=False)
    motherBubble = models.ForeignKey('self', null=True, blank=True,related_name='subBubbles',db_column='motherBubble', on_delete=models.CASCADE)
    # events=models.ManyToManyField(Event, null=True, blank=True,related_name='relatedEvents',db_column='relatedEvents',symmetrical=False)


    def __str__(self):
        return self.topic #+ ' ' + '- id = ' +  str( self.pk ) 

    # Das passiert wenn eine Bubble erzeugt wird
    def get_absolute_url(self):
        return reverse("D3App:BubblesList")#D3App:,kwargs={'pk':self.pk}

    class Meta():
        verbose_name='Bubbles'
