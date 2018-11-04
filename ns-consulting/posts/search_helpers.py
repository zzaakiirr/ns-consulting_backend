from .models import PostPluginModel


def get_duplicate_ids():
    existing_links = {}
    duplicate_ids = []

    for post in PostPluginModel.objects.all():
        if existing_links.get(post.link, False):
            duplicate_ids.append(post.id)
        else:
            existing_links[post.link] = True

    return duplicate_ids
