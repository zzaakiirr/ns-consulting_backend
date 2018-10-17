from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from djangocms_link.cms_plugins import LinkPlugin
from djangocms_file.cms_plugins import FilePlugin
from djangocms_link.models import Link
from djangocms_file.models import File

from .models import FileLinkWithBackgroundColor, LinkWithBackgroundColor


@plugin_pool.register_plugin
class FileLinkWithBackgroundColorPlugin(FilePlugin):
    name = _("Ссылка на файл с цветом фона")
    model = FileLinkWithBackgroundColor
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'file_src',
                'file_background_color',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                ('link_target', 'link_title'),
                'show_file_size',
                'attributes',
            )
        }),
    ]

    @classmethod
    def get_render_template(self, context, instance, placeholder):
        return 'file_with_background_color.html'


@plugin_pool.register_plugin
class LinkWithBackgroundColorPlugin(LinkPlugin):
    name = _("Ссылка с цветом фона")
    model = LinkWithBackgroundColor

    fieldsets = [
        (None, {
            'fields': (
                'name',
                ('external_link', 'internal_link'),
                'background_color',
            )
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('mailto', 'phone'),
                ('anchor', 'target'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                'attributes',
            )
        }),
    ]

    @classmethod
    def get_render_template(self, context, instance, placeholder):
        return 'link_with_background_color.html'


@plugin_pool.register_plugin
class FileLinkWithBackgoundImagePlugin(FilePlugin):
    name = _("Ссылка на файл с изображением на фоне")
    model = File
    allow_children = True

    @classmethod
    def get_render_template(self, context, instance, placeholder):
        return 'file_link_background_img.html'


@plugin_pool.register_plugin
class LinkWithBackgoundImagePlugin(LinkPlugin):
    name = _("Ссылка с изображением на фоне")
    model = Link

    @classmethod
    def get_render_template(self, context, instance, placeholder):
        return 'link_background_img.html'
