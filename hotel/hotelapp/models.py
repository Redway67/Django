from django.db import models
from phone_field import PhoneField
from usersapp.models import GuestUser


# Номерной фонд
class Room(models.Model):
    number = models.PositiveSmallIntegerField()
    TYPE_CHOICES = (
        ('D', 'Одна двуспальная кровать'),
        ('S', 'Две односпальные кровати'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return f' {self.number} {self.type}'


# Клиенты
class Client(models.Model):
    family_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = PhoneField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.family_name} {self.name}'


# Бронирования
class BookingOrder(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    who = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    data_in = models.DateField(db_index=True)
    data_out = models.DateField()
    is_breakfast = models.BooleanField()
    user = models.ForeignKey(GuestUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Гость:{self.who} Заезд:{self.data_in} Выезд:{self.data_out} Номер:{self.room}'


# Прайс
class HistoryPrice(models.Model):
    data = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.data} {self.price}'


class Gallery(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery', null=True, blank=True)
    description = models.TextField(blank=True)
