def cart_quantity(request):
    cart = request.session.get("shopping_cart", {})
    return {
        'shopping_cart':cart,
        'cart_quantity':len(cart),
    }