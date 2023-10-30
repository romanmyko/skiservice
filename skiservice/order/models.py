from django.db import models, DataError

from authentication.models import CustomUser
from equipment.models import Staff


class Order(models.Model):
   
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(default=None, null=True, blank=True)
    plated_end_at = models.DateTimeField(default=None)



    def __str__(self):
        return self.user
      
   