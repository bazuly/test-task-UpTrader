from django.db import models

CHOICES_MENU_STATUS = [
    ("Empty", "Empty"),
    ("Allowed", "Allowed"),
    ('Forbidden', 'Forbidden')
]


class Menu(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='menu_name',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=CHOICES_MENU_STATUS,
        default=CHOICES_MENU_STATUS[0][0]
    )

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name='menu',
        null=True,
        blank=True
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="parent",
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=128,
        verbose_name="name"
    )
    status = models.CharField(
        max_length=128,
        verbose_name="status",
        choices=CHOICES_MENU_STATUS,
        default=CHOICES_MENU_STATUS[0][0]
    )
    url = models.SlugField(
        verbose_name="URL",
        blank=True,
        null=True)

    # def get_absolute_url(self):
    #     return "/%s" % self.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu item"
        verbose_name_plural = "Menu item"
