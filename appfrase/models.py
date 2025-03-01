from django.db import models

class Frase(models.Model):
    texto = models.TextField()
    advice_id = models.IntegerField(null=True, blank=True)  # ID do conselho associado
    advice_text = models.TextField(null=True, blank=True)   # Texto do conselho

    def __str__(self):
        return self.texto