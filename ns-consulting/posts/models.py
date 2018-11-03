from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField
from djangocms_text_ckeditor.fields import HTMLField


class Post(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=255,
        blank=True,
    )

    description = HTMLField(
        verbose_name=_('Описание'),
        blank=True,
    )

    link = PageField(
        verbose_name=_('Ссылка'),
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        if self.title:
            return self.title
        return 'новость %d' % self.id


class PostPluginModel(CMSPlugin):
    post = models.ForeignKey(Post)

    def __unicode__(self):
        if self.post.title:
            return self.post.title
        return 'новость %d' % self.post.id

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
