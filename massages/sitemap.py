from django.contrib.sitemaps import Sitemap
from massages.models import Massage


class MassageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Massge.active_objects.all()

    def lastmod(self, obj):
        return obj.created_on
