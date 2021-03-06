# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict



def profile_picture_document_destination(instance, filename):
    return '/'.join(['documentos_del_usuario', str(instance.user.id), 'profile_' + filename])



# Create your models here.
class ERPUser(models.Model):
    ADMINISTRATOR = "AD"
    DIRECTIVO = "DI"

    ROLES_CHOICES = (
        (ADMINISTRATOR, 'Administrador General'),
        (DIRECTIVO, 'Directivo'),
    )

    user = models.OneToOneField(User)
    rol = models.CharField(max_length=2, choices=ROLES_CHOICES, default=ADMINISTRATOR)
    # projects = models.ManyToManyField(through=AccessToProject,null=True,blank=True)

    profile_picture = models.FileField(blank=True, null=True, upload_to=profile_picture_document_destination,
                                       verbose_name="Foto de Perfil")

    class Meta:
        verbose_name_plural = 'Usuarios'

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['name'] = str(self.user.first_name)
        ans['lastname'] = str(self.user.last_name)
        return ans

    def __str__(self):
        return self.user.get_username()


        # Create your models here.


