from django.db.models import Manager

class ActiveManager(Manager):
    """Returns active massages."""

    def active(self):
        return self.get_query_set().filter(active=True)
