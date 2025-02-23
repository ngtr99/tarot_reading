from django.db import models

# Create your models here.
class TarotCard(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    item = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name

class Love(models.Model):
    tarot_card = models.ForeignKey(TarotCard, on_delete=models.CASCADE, related_name='love_readings')
    description = models.TextField()

    def __str__(self):
        return self.tarot_card.name

class Career(models.Model):
    tarot_card = models.ForeignKey(TarotCard, on_delete=models.CASCADE, related_name='career_readings')
    description = models.TextField()

    def __str__(self):
        return self.tarot_card.name

class Health(models.Model):
    tarot_card = models.ForeignKey(TarotCard, on_delete=models.CASCADE, related_name='health_readings')
    description = models.TextField()

    def __str__(self):
        return self.tarot_card.name

class Finance(models.Model):
    tarot_card = models.ForeignKey(TarotCard, on_delete=models.CASCADE, related_name='finance_readings')
    description = models.TextField()

    def __str__(self):
        return self.tarot_card.name
