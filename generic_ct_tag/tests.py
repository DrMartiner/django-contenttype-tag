# -*- coding: utf-8 -*-

from django.utils import unittest
from django.contrib.auth.models import User
from django.template import Context, Template


class TemplateTagsTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(
            username='name',
            email='user@example.com',
        )
        self.user.save()

        self.template = '{% load generic_ct %}'

    def tearDown(self):
        self.user.delete()

    def test_render_type(self):
        template = Template(self.template + '{% content_type obj %}')
        context = Context({'obj': self.user})
        html = template.render(context)
        self.assertIn('auth.user', html, 'Content type was not render')

    def test_render_as_name(self):
        template = Template(
            self.template + '{% content_type obj as ct %}{{ ct.app_label }}.{{ ct.model }}')
        context = Context({'obj': self.user})
        html = template.render(context)
        self.assertIn('auth.user', html, 'Content type was not render')