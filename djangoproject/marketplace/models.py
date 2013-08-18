from django.conf import settings
from django.db import models
from django.db.models import Q

class DealManager(models.Manager):
    
    def search(self, query=''):
        return self.filter(Q(title__icontains=query) | Q(description__icontains=query))

class Deal(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    price = models.DecimalField('Price', max_digits=20, decimal_places=2)
    title = models.CharField('Title', max_length=40)
    description = models.CharField('Description', max_length=100, blank=True, null=True, default='')
    is_available = models.BooleanField('Available', default=True)
    is_sold = models.BooleanField('Sold', default=False)
    image = models.ImageField(upload_to='deal_images')
    is_open = models.BooleanField('Open', default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = DealManager()
    
    def __unicode__(self):
        return self.title
        
class Offer(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    deal_offered_to = models.ForeignKey(Deal, related_name='deal_offered_to')
    deal_owned = models.ForeignKey(Deal, blank=True, null=True, related_name='deal_owned')
    amount = models.DecimalField('Price', max_digits=20, decimal_places=2, blank=True, null=True)
    description = models.CharField('Description', max_length=100, blank=True, null=True, default='')
    is_accepted = models.BooleanField('Accepted', default=False)
    is_rejected = models.BooleanField('Rejected', default=False)
    is_cancelled = models.BooleanField('Cancelled', default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.description
        
    def accept_offer(self):
        self.is_accepted = True
        self.deal_offered_to.is_sold = True
        self.deal_offered_to.is_available = False
        self.__class__.objects.filter(deal_offered_to=self.deal_offered_to).update(is_accepted=False)
