from django.db import models


from users.models import User
from datetime import datetime, timezone

import pytz
ist = pytz.timezone('Asia/Kolkata')






class godown(models.Model):

    name = models.CharField(max_length=120, unique=False)
    
    
    def __str__(self):
        return self.name


class customer(models.Model):

    name = models.CharField(max_length=120, unique=False)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()
    
    
    def __str__(self):
        return self.name







class category(models.Model):

    name = models.CharField(max_length=120, unique=False)
    
    
    def __str__(self):
        return self.name

    
    def __str__(self):
        return self.name



class size(models.Model):
    
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=False)

    def __str__(self):
        return self.name

class thickness(models.Model):
    
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=False)

    def __str__(self):
        return self.name

class grade(models.Model):
    
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=False)

    def __str__(self):
        return self.name

class dealer(models.Model):

    name = models.CharField(max_length=120, unique=False)
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField()
    
    
    def __str__(self):
        return self.name





class product(models.Model):

    shelf = models.ForeignKey(godown, on_delete=models.CASCADE, null = True, blank = True)
    size = models.ForeignKey(size, on_delete=models.CASCADE, null = True, blank = True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null = True, blank = True)
    thickness = models.ForeignKey(thickness, on_delete=models.CASCADE, null = True, blank = True)
    grade = models.ForeignKey(grade, on_delete=models.CASCADE, null = True, blank = True)



class product_qr(models.Model):
    
    shelf = models.ForeignKey(godown, on_delete=models.CASCADE, null = True, blank = True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name = "project_material_re", null = True, blank = True)
    qr_code = models.ImageField(upload_to='static/qrcode/', height_field=None, width_field=None, max_length=None, null = True, blank = True)