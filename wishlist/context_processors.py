from .models import Wishlist


def wishlist_count(request):
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        return {'wishlist_count': wishlist.items.count()}
    return {'wishlist_count': 0}
