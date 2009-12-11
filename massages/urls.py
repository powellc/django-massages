from django.conf import settings
from django.conf.urls.defaults import *
from massages import views
from massages.models import Massage, RateList
#from tagging.views import tagged_object_list


# custom views vendors
urlpatterns = patterns('massages.views',
    url(r'^$', view=views.massage_index, name="massage_index"),
)
