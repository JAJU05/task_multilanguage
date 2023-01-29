from django.db.models import Model, CharField, TextField, DateTimeField, SlugField, ForeignKey, CASCADE, ImageField
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(max_length=255),
    )
    slug = SlugField(max_length=255, unique=True)


class Blog(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(max_length=255),
        description=TextField(null=True, blank=True),
    )
    slug = SlugField(max_length=255, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    category = ForeignKey('home.Category', CASCADE)
    blog_image = ImageField(upload_to='blogs/')

    # def __str__(self):
    #     return self.