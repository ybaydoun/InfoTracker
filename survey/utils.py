from django.contrib.auth.models import Group
from import_export.formats import base_formats


def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        return True if user and group in user.groups.all() else False
    except Group.DoesNotExist:
        return False


def get_default_formats():
    """
    Return available export formats.
    """
    return (
        base_formats.XLS,
        base_formats.XLSX,
        base_formats.JSON
    )
