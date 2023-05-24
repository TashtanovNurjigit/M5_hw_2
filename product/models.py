from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    @property
    def products_count(self):
        return self.category_product.count()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product', null=True)

    @property
    def product_reviews(self):
        return self.product_reviews.text if self.product_reviews else ''

    @property
    def rating(self):
        count = self.product_reviews.count()
        if count == 0:
            return 0
        else:
            total = 0
            for i in self.product_reviews.all():
                total += i.stars
            return total/count

    def __str__(self):
        return self.title


STARS_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* ')
)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews', null=True)
    stars = models.IntegerField(default=5, choices=STARS_CHOICES)
