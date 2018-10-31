from django.utils.translation import ugettext_lazy as _

from django.db import models


class Poll(models.Model):
    question = models.CharField(
        verbose_name=_('Вопрос'),
        max_length=255,
        blank=False,
        default=None,
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    percent = models.IntegerField(default=0, editable=False)

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'

    def __str__(self):
        return self.choice_text
