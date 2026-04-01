"""
 list indexing for CSS
"""
from django import template
register = template.Library()

@register.filter
def get_item_by_index(sequence, position):
    """
    function for getting item by index in django template
    :param sequence:
    :param position:
    :return:
    """
    print(sequence, position)
    try:
        return list(sequence)[position-1]
    except IndexError:
        return None
    except TypeError:
        return None
