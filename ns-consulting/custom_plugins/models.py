from django.utils.translation import ugettext_lazy as _
from djangocms_file.models import File
from djangocms_link.models import Link

from colorfield.fields import ColorField


class FileWithBackgroundColor(File):
    file_background_color = ColorField(
        verbose_name=_('Цвет фона'),
        default='#f8f8f8'
    )


class LinkWithBackgroundColor(Link):
    background_color = ColorField(
        verbose_name=_('Цвет фона'),
        default='#f8f8f8'
    )
