from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PollPluginModel


@plugin_pool.register_plugin
class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel
    module = _("Опросы")
    name = _("Опрос")
    render_template = "polls_cms_integration/poll_plugin.html"

    def render(self, context, instance, placeholder):
        if context['request'].session.get('poll_has_been_voted', False):
            self.render_template = 'polls_cms_integration/results.html'
        context.update({'instance': instance})
        return context
