from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('principal', 'Principal'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Ensure unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Ensure unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username