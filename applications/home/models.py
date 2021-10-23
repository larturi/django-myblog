from django.db import models
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=100)
    about_text = models.TextField()
    contact_email = models.EmailField('Email Contacto', blank=True, null=True)
    contact_phone = models.CharField('Telefono Contacto', max_length=20)

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        return self.title

class Suscribers(TimeStampedModel):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    full_name = models.CharField('Nombre Completo', max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.full_name
