from django.db import models


class Staff(models.Model):
   
    brend = models.CharField(blank=True, max_length=128)
    model = models.CharField(blank=True, max_length=256)
    year_of_pruduction = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=10,null=True)
    count = models.IntegerField(default=10)
    id = models.AutoField(primary_key=True)
    


    def __str__(self):
      
        return f"'id': {self.id}, 'name': '{self.brend}', "
