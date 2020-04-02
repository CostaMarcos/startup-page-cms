from django.db import models


class Main(models.Model):
    Template = models.CharField(max_length=30)
    FirstPlaceTitle = models.CharField(max_length=30)
    FirstPlaceDescription = models.TextField(max_length=150)
    SecondPlaceTitle = models.CharField(max_length=30)
    SecondPlaceDescription = models.TextField(max_length=150)
    ThirdlaceTitle = models.CharField(max_length=30)
    ThirdPlaceDescription = models.TextField(max_length=150)

    def __str__(self):
        return self.Template


class Header(models.Model):
    StartupName = models.CharField(max_length=100)
    TitleDescription = models.CharField(max_length=100)
    Description = models.TextField(max_length=300)
    Main = models.ForeignKey(Main, on_delete=models.CASCADE)

    def __str__(self):
        return self.StartupName
