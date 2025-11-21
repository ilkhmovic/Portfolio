from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    
class Portfel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

class AboutMe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to='aboutme/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Mening Haqimda"
        verbose_name_plural = "Mening Haqimdagilar"


class Skill(models.Model):
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ko\'nikma"
        verbose_name_plural = "Ko\'nikmalar"

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"

class ContactMessage(models.Model):
    # Foydalanuvchi ma'lumotlari (forma orqali to'ldiriladi)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Sizning doimiy ma'lumotlaringiz (admin panelda to'ldiriladi)
    author_email = models.EmailField(blank=True, null=True)
    author_phone = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        verbose_name = "Kontakt Xabar"
        verbose_name_plural = "Kontakt Xabarlar"

class SocialMedia(models.Model):
    url = models.URLField()
    icon_class = models.CharField(max_length=200)

    def __str__(self):
        return self.url



