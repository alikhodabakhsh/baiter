import uuid
from django.db import models
from accounts.models import User
from django.utils import timezone
from datetime import date
from django.db.models.signals import pre_save, post_save


class CurrencyQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()


class CurrencyManager(models.Manager):
    def get_queryset(self):
        return CurrencyQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Category(models.Model):
    TRAN_STATUS = (
        ('B','Buy'),
        ('S','Sell'),
    )
    status = models.CharField(max_length=1,
                                choices = TRAN_STATUS,
                                default= 'B',
                                help_text='buy or sell')
    
    class Meta:
        ordering = ('status',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('service:product_list_by_category', args=[self.status])


class CurrencyAd(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(blank=True, unique=True)
    username = models.ForeignKey(User, on_delete=models.PROTECT, related_name='currencyads')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='currencyads')
    max_amount = models.IntegerField()
    min_amount = models.IntegerField()
    name_currency = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    publish_date = models.DateField(default=timezone.now)
    date = models.DateField(default=date.today)
    timestamp = models.DateTimeField(auto_now_add=True)


    objects = CurrencyManager()


    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.slug

    def __unicode__(self):
        return self.slug

    @property
    def name(self):
        return self.name_currency



def CurrencyAd_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_name_currency_generator(instance)

pre_save.connect(CurrencyAd_pre_save_receiver, sender=CurrencyAd) 

