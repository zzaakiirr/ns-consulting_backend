from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool

from djangocms_link.cms_plugins import LinkPlugin
from djangocms_file.cms_plugins import FilePlugin

from djangocms_link.models import Link
from djangocms_file.models import File


@plugin_pool.register_plugin
class FileWithBackgoundImagePlugin(FilePlugin):
    name = _("Ссылка на файл с изображением на фоне")
    model = File
    allow_children = True

    @classmethod
    def get_render_template(self, context, instance, placeholder):
        return 'file_background_img.html'


@plugin_pool.register_plugin
class LinkWithBackgoundImagePlugin(LinkPlugin):
    name = _("Ссылка с изображением на фоне")
    model = Link

    @classmethod
    def get_render_template(self, context, instance, placeholder):
        return 'link_background_img.html'
