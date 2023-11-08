import uuid
from django.db import models

class api(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    api_key=models.TextField(blank=False)
    No_use=models.CharField(max_length=100,default=0)
    created = models.DateTimeField(auto_now_add=True,editable=True)
    def __str__(self):
        return f"{self.No_use} | {self.created}"

class asked_Ai(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    api=models.ForeignKey(api,on_delete=models.SET_NULL,null=True)
    question=models.TextField(blank=True)
    answer=models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.api} | {self.created}"
