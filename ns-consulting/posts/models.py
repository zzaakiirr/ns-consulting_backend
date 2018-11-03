from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PageField
from djangocms_text_ckeditor.models import AbstractText


class PostPluginModel(AbstractText):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        default='',
        max_length=255,
        blank=False,
    )
    link = PageField(
        verbose_name=_('Ссылка'),
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __unicode__(self):
        if self.title:
            return self.title
        return 'новость %d' % self.id
