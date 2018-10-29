from django.utils.translation import ugettext_lazy as _
from djangocms_file.models import File
from djangocms_link.models import Link

from colorfield.fields import ColorField


class FileLinkWithBackgroundColor(File):
    file_background_color = ColorField(
        verbose_name=_('Цвет фона'),
        default='#ffffff'
    )


class LinkWithBackgroundColor(Link):
    background_color = ColorField(
        verbose_name=_('Цвет фона'),
        default='#ffffff'
    )
