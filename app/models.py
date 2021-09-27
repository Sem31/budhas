from django.db import models

# Create your models here.


class Gift(models.Model):
    giftTitle = models.CharField(max_length=255, blank=True, null=True)
    giftDetail =models.TextField()
    giftImage = models.ImageField(upload_to="uploads/")

class LandingPageDetails(models.Model):
    productHeading = models.CharField(max_length=255, blank=True, null=True)
    productDetail = models.TextField()
    productImage = models.ImageField(upload_to="uploads/")
    actuallPrice = models.IntegerField()
    percentage = models.IntegerField()
    offerTime = models.IntegerField()
    image_1 = models.ImageField(upload_to="uploads/")
    image_2 = models.ImageField(upload_to="uploads/")
    image_3 = models.ImageField(upload_to="uploads/")
    # Idol
    idolImage = models.ImageField(upload_to="uploads/")
    idolName =  models.CharField(max_length=255, blank=True, null=True)
    idolDetail = models.TextField()
    idolMaterial = models.CharField(max_length=255, blank=True, null=True)
    idolColor = models.CharField(max_length=255, blank=True, null=True)
    idolWeight = models.CharField(max_length=255, blank=True, null=True)
    idolSize = models.CharField(max_length=255, blank=True, null=True)
    idolInches = models.CharField(max_length=255, blank=True, null=True)
    # Gift
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    idolQuote = models.TextField()

    def __str__(self) -> str:
        return self.productHeading

class Comment(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(auto_now=True)