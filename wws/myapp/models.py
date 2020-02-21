from django.db import models

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.search) #this returns the name of search instead of something like object

    class Meta:
        verbose_name_plural = 'Searches' #this is the name of your field in admin page
