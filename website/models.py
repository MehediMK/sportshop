from django.db import models


class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default='Sports Shop')
    site_logo = models.ImageField(upload_to='site/')
    offer_message = models.CharField(max_length=300,  default='Welcome to SportsHub!', null=True, blank=True)
    contact_email = models.EmailField(default='contact@sportsshop.com')
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Site Configuration"


class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=50)
    subject = models.EmailField(max_length=50, blank=False)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"
