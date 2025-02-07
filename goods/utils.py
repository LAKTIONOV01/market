from goods.models import Product


def q_search(query):
    if query.isdigit() and len(query)<=5:
        return Product.objects.filter(id=int(query))

    return Product.objects.filter(description__search=query)




