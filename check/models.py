from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class Classification(models.Model):        
    classification = models.CharField(max_length=255, blank=True, null = True)
    def __str__(self):
    	return str(self.classification)

class Gender(models.Model):        
    gender = models.CharField(max_length=255, blank=True, null = True)
    def __str__(self):
    	return str(self.gender)

class Profile(models.Model):        
    # required to associate Author model with User model (Important)
    full_name = models.CharField(max_length=255, blank=True, null = True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank = True)
    email = models.CharField(max_length=255, blank=True, null = True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True, blank = True)
    identification_number = models.CharField(max_length=255, blank=True, null = True)
    date_accomplished = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    qr_code = models.ImageField(upload_to = 'uploads/', blank = True, null = True)

    def __str__(self):
    	return str(self.full_name) + "  " +str(self.date_accomplished)

    def save(self, *args, **kwargs):
    	qrcode_img = qrcode.make("Full_name: "+self.full_name)
    	canvas = Image.new('RGB', (300, 300), 'white')
    	draw = ImageDraw.Draw(canvas)
    	canvas.paste(qrcode_img)
    	fname = f'qr_code-{self.full_name}.png'
    	buffer = BytesIO()
    	canvas.save(buffer,'PNG')
    	self.qr_code.save(fname, File(buffer), save = False)
    	canvas.close()
    	super().save(*args, **kwargs)
