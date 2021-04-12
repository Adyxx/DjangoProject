from django.db import models
from django.urls import reverse

def attachment_path(instance, filename):
    return "animal/" + str(instance.animal.id) + "/attachments/" + filename

def poster_path(instance, filename):
    return "animal/" + str(instance.id) + "/image/" + filename
class Type(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Animal type",
    help_text='Enter an animal type (e.g. mammal, bird)')

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    latinn = models.CharField(max_length=200, verbose_name="Latin name")
    typee = models.ManyToManyField(Type, verbose_name="Type", help_text='select an animal type') 
    info = models.TextField(blank=True, null=True, verbose_name="Info")
    image = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Image")

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return f"{self.name}, {self.latinn}"
    
    def get_absolute_url(self):
        return reverse('animal-detail', args=[str(self.id)])

class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

    TYPE_OF_ATTACHMENT = (
        ('audio','Audio'),
        ('image','Image'),
        ('text','Text'),
        ('video','Video'),
        ('other','Other'),
    )

    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True,
    default='image', help_text='Select attachment type', verbose_name="Attachment type")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-last_update", "type"]

    def __str__(self):
        return f"{self.title}, ({self.type})"
