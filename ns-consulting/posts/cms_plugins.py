from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PostPluginModel


@plugin_pool.register_plugin
class PostPluginPublisher(CMSPluginBase):
    model = PostPluginModel
    module = _("Новости")
    name = _("Новость")
    render_template = "posts/post_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
