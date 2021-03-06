from django.db import models
from django.urls import reverse

from adverts.models import Advert, Location
from django.utils.translation import gettext_lazy as _


class Item(Advert, Location):
    CONDITIONS = [('0', _('Used')),
                  ('1', _('Acceptable')),
                  ('2', _('Very Good')),
                  ('3', _('Like New')),
                  ('4', _('New')),
                  ]
    condition = models.CharField(
        max_length=1,
        choices=CONDITIONS,
        default='0'
    )
    image = models.ImageField(upload_to='items', default='none/no-img.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))

    def get_absolute_url(self):
        return reverse('items:detail', args=[self.id])

