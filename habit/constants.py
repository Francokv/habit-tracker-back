from django.db import models

class ObjetiveDataTypes(models.TextChoices):
    TEXT = 'text', 'Text'
    NUMBER = 'number', 'Number'
    BOOLEAN = 'boolean', 'Boolean'
    SLIDER = 'slider', 'Slider'
    OPTIONS = 'options', 'Options'