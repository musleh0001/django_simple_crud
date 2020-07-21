from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    description = models.TextField(verbose_name='Description', max_length=1000, blank=True)
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=8)
    created_at = models.DateTimeField(verbose_name='Created_at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated_at', auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk':self.pk})