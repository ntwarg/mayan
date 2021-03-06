from django import template
from django.conf import settings
from django.core.urlresolvers import reverse


register = template.Library()


@register.inclusion_tag('dynamictwain/upload.html')
def upload_scan():
    return {}

@register.inclusion_tag('dynamictwain/submit.html')
def submit_form_with_scan():
    return {}

@register.inclusion_tag('dynamictwain/widget.html')
def scan_widget(size="600x800", multiple=True):
    if multiple == "False":
        multiple = False
    elif multiple == "True":
        multiple = True

    size = size.split('x')
    width = size[0]
    height = size[1]

    if multiple:
        multiple = 'true'
    else:
        multiple = 'false'

    default_upload_path = reverse('dynamictwain:upload')

    data = {
        'base_url': getattr(settings,'DYNAMIC_TWAIN_MEDIA_ROOT',"/usr/share/dev1/scan/mayan/apps/dynamictwain/media/"),
        'default_resolution': getattr(settings,'DYNAMIC_TWAIN_DEFAULT_RESOLUTION', 150),
        'server': getattr(settings, 'DYNAMIC_TWAIN_SERVER', 'localhost'),
        'upload_path': getattr(settings, 'DYNAMIC_TWAIN_UPLOAD_PATH', default_upload_path),
        'width': width,
        'height': height,
        'multiple': multiple,
    }
    return data
