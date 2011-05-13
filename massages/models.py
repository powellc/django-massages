from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from massages.managers import ActiveManager

class Massage(models.Model):
    '''
    This model stores massage information.
    '''
    title = models.CharField(_("title"), max_length = 255)
    slug = models.SlugField()
    lead = models.CharField(_('lead'), max_length=255)
    description = models.TextField(_("description"))
    photo = models.FileField(_('photo'), upload_to="massages/")
    creator = models.ForeignKey(User, null = True, verbose_name=_("creator"))
    created_on = models.DateTimeField(_("created on"), default = datetime.now)
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2, null=True, blank=True)
    time=models.IntegerField(_('time'), null=True, blank=True)
    at_rate = models.BooleanField(_('standard rate?'), default=False)
    active = models.BooleanField(_('active'), default=True)
    order = models.IntegerField(_('order'), blank=True, null=True, max_length=3)

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        verbose_name = _('massage')
        verbose_name_plural = _('massages')

    def __unicode__(self):
	return self.title
		
    def get_absolute_url(self):
        return reverse('massage', args=[self.slug])

class Rate(models.Model):
	time = models.IntegerField(_('time in minutes'), max_length=4)
	price = models.DecimalField(_('price'), max_digits=6, decimal_places=2)
	
	class Meta:
   	    verbose_name = _('rate')
  	    verbose_name_plural = _('rates')
		
	def __unicode__(self):
	    return str(self.price) + '/' + str(self.time) + ' minutes'
		
class RateList(models.Model):
	title = models.CharField(_('title'), max_length=100)
	rates = models.ManyToManyField(Rate)
	active = models.BooleanField(_('active'), default=True)
	image = models.ImageField(_('rate list image'), upload_to='photos', null=True, blank=True)
	
	class Meta:
	    verbose_name = _('rate list')
	    verbose_name_plural = _('rate lists')
		
	def __unicode__(self):
	    return self.title
	'''
	def save(self):
	    if self.active==True:
                RateList.objects.all().update(active=False)
	    super(RateList, self).save
       '''
