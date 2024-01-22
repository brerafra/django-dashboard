from django.db import models

#Users in access-control system enviroment
class UserC(models.Model):
    uid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.uid}, {self.name}'
    
#Device in access-control system enviroment
class Device(models.Model):
    name = models.CharField(max_length=250, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.active}, {self.name}'
    

#Events in access-control system enviroment
class Event(models.Model):
    type = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(UserC, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.type}, {self.user}'
