# -*- coding: utf-8 -*-

import django
from django.conf import settings
from django.contrib.admin.templatetags.admin_static import static
from django.forms.util import flatatt
from django.forms.widgets import Select
from django.utils.safestring import mark_safe


if django.VERSION >= (1, 2, 0) and getattr(
        settings,
        'USE_DJANGO_JQUERY', True):
    USE_DJANGO_JQUERY = True
else:
    USE_DJANGO_JQUERY = False
    JQUERY_URL = getattr(
        settings,
        'JQUERY_URL',
        'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js')

URL_PREFIX = getattr(settings, "CHAINED_SELECTS_URL_PREFIX", "")


class ChainedSelectWidget(Select):

    class Media:
        if USE_DJANGO_JQUERY:
            js = [static('admin/%s' % i) for i in
                  ('js/jquery.min.js', 'js/jquery.init.js')]
        elif JQUERY_URL:
            js = (
                JQUERY_URL,
            )
        js += (static('chained_selects/delayed_fill.js'), )

    def __init__(self, parent_name, app_name, model_name, method_name,
                                                        *args, **kwargs):
        self.datas = {
            'data-parent-id': 'id_%s' % parent_name,
            'data-url': (
                '/%(prefix)s'
                '/%(app_name)s'
                '/%(model_name)s'
                '/%(method_name)s/') % {
                    'prefix': kwargs.get('url_prefix', 'chained'),
                    'app_name': app_name,
                    'model_name': model_name,
                    'method_name': method_name
                },
            'data-empty-label': '---------'}
        super(ChainedSelectWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = ''
        attrs.update(dict(self.datas, **{'class': 'chained'}))
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append(u'</select>')
        return mark_safe(u'\n'.join(output))
