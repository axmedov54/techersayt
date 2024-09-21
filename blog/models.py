from django.db import models
from django.utils import timezone




# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     slug= models.SlugField(max_length=200,unique=True)
    
    
#     def __str__(self) -> str:
#         return self.name
    
# class Publishmeneger(models.Manager):
#     def get_queryset(self) -> models.QuerySet:
#         return super(Publishmeneger,self).get_queryset().filter(status='published')
    
    
class Matematika(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )
    title = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="photos", null=True, blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()  # defoult manager
    # published = Publishmeneger() # published manajer yangiliklarni qayataradi

    class Meta:
        ordering = ('-publish',)


class Onnatili(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )
    title = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="photos", null=True, blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()  # defoult manager
    # published = Publishmeneger() # published manajer yangiliklarni qayataradi

    class Meta:
        ordering = ('-publish',)        


# class CommentPost(models.Model):
#     author = models.ForeignKey(to=User,on_delete=models.CASCADE)
#     post= models.ForeignKey(to=Post,on_delete=models.CASCADE)
#     comment=models.TextField()
#     crated= models.DateField(auto_now_add=True)
    
    
    
#     def __str__(self) -> str:
#         return f'{self.author} -> {self.crated}'
    
    
class Contact(models.Model):
    username = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    message = models.TextField()
    
    
    def __str__(self) -> str:
        return  self.username    