from django import template
register = template.Library()
@register.filter
def get_item_by_index(sequence, position):
    print(sequence, position)
    try:
        return list(sequence)[position-1]
    except IndexError:
        return None
    except TypeError:
        return None