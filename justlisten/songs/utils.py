from django.utils.text import slugify


def simple_unique_slug(instance, field_value, slug_field_name='slug'):
    base_slug = slugify(field_value)
    similar = instance.__class__.objects.filter(**{f"{slug_field_name}__startswith": base_slug}).count()
    return f"{base_slug}-{similar + 1}"