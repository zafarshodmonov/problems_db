from database.models import add_topic

def get_or_create_topic(name):
    """ Agar mavzu mavjud bo'lmasa, uni yaratadi """
    return add_topic(name)
