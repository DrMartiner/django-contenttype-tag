# -*- coding: utf-8 -*-
import re

from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


class ContentTypeNode(template.Node):
    def __init__(self, instance, var_name):
        self.object = template.Variable(instance)
        self.var_name = var_name

    def render(self, context):
        instance = self.object.resolve(context)
        ct = ContentType.objects.get_for_model(instance)
        if self.var_name:
            context[self.var_name] = ct
        else:
            return '%s.%s' % (ct.app_label, ct.model)

@register.tag
def content_type(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, '%r tag requires exactly one argument' % token.contents.split()[0]

    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        instance, var_name = m.groups()
    else:
        instance, var_name = arg, None

    return ContentTypeNode(instance, var_name)