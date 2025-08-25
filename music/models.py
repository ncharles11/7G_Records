from django.db import models

class Artiste(models.Model):
    nom = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.nom

class Chanson(models.Model):
    titre = models.CharField(max_length=200)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name='chansons')
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    fichier_audio = models.FileField(upload_to='songs/')

    def __str__(self):
        return f"{self.titre} - {self.artiste.nom}"