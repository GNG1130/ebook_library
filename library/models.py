from django.db import models
from PyPDF2 import PdfFileReader
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    pdf = models.FileField(upload_to='books/')

    def save(self, *args, **kwargs):
        if not self.cover:
            self.set_default_cover()
        super().save(*args, **kwargs)

    def set_default_cover(self):
        if default_storage.exists(self.pdf.name):
            with default_storage.open(self.pdf.name, 'rb') as f:
                reader = PdfFileReader(f)
                if reader.numPages > 0:
                    page = reader.getPage(0)
                    image = page.get_thumbnail()
                    if image:
                        img_io = BytesIO()
                        image.save(img_io, 'JPEG')
                        self.cover.save(self.pdf.name + '_cover.jpg', ContentFile(img_io.getvalue()), save=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
