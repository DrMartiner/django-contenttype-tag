=====
django-contenttype-tag
=====

It's easy app for get content type of instance at templates

=====
How to use
=====

1. Add 'generic_ct_tag' at INSTALLED_APPS::

      INSTALLED_APPS = (
            ...
            'generic_ct_tag',
      )

3. At template::

      {% load generic_ct %}

      {% content_type obj as ct %}
      {{ ct.app_label }}
      {{ ct.model }}

      {# or #}

      {% content_type obj %} {# The resulr: <app_label>.<model> #}
