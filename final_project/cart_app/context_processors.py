from .models import Cart,CartItem_View
from .views import _cart_id
def cart_counters(request):
    cart_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            cart_items=CartItem_View.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count+=cart_item.quantity
        except Cart.DoesNotExist:
            cart_count=0
    return dict(cart_count=cart_count)
    
