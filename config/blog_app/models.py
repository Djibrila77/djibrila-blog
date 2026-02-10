from django.db import models

class Publication(models.Model):
    # Choices for the nature/type field
    class Nature(models.TextChoices):
        ARTICLE = 'ARTICLE', 'Article'
        COMPETENCE = 'COMPETENCE', 'Compétence'
    
    titre = models.CharField(max_length=200, verbose_name="Titre")
    contenu = models.TextField(verbose_name="Contenu")
    slug = models.URLField(null=True, blank=True, unique=True, verbose_name="Slug")
    date_publication = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    date_mis_a_jour = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    image = models.ImageField(blank=True, null=True, verbose_name="Image")
    nature = models.CharField(
        max_length=20,
        choices=Nature.choices,
        default=Nature.ARTICLE,
        verbose_name="Nature"
    )
    
    def __str__(self):
        return f"{self.titre} - {self.get_nature_display()}"
    
    class Meta:
        verbose_name = "Contenu"
        verbose_name_plural = "Contenus"
        ordering = ['-date_publication']
class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    date_abonnement = models.DateTimeField(auto_now_add=True, verbose_name="Date d'abonnement")
        
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Abonné"
        verbose_name_plural = "Abonnés"