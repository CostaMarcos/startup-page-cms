from django.db import models


class Navigation(models.Model):
    StartupName = models.CharField(max_length=100)
    FirstSession = models.CharField(max_length=20, default="About")
    SecondSession = models.CharField(max_length=20, default="Services")
    ThirdSession = models.CharField(max_length=20, default="Portifolio")
    FourthSession = models.CharField(max_length=20, default="Contact")

    def __str__(self):
        return self.StartupName


class FirstPlace(models.Model):
    Template = models.CharField(max_length=50, default="Template 1")
    Title = models.CharField(max_length=200, default="The best startup ever")
    Description = models.TextField(max_length=300, default="We can help you build better websites using the Bootstrap CSS framework! Just download your template and start going, no strings attached!")
    ButtonText = models.CharField(max_length=20, default="Find out more")
    ButtonLink = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Template


class AboutYou(models.Model):
    Template = models.CharField(max_length=50,default="Template 1")
    Title = models.CharField(max_length=100, default="We've got what you need!")
    Description = models.TextField(max_length=300)
    ButtonText = models.CharField(max_length=50, default="Get started!")
    ButtonLink = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Template


class YourService(models.Model):
    Template = models.CharField(max_length=50,default="Template 1")
    MainTitle = models.CharField(max_length=100, default="At Your Service")
    FirstItemTitle = models.CharField(max_length=100)
    FirstItemDescription = models.TextField(max_length=300)
    SecondItemTitle = models.CharField(max_length=100)
    SecondItemDescription = models.TextField(max_length=300)
    ThirdItemTitle = models.CharField(max_length=100)
    ThirdItemDescription = models.TextField(max_length=300)
    FourthItemTitle = models.CharField(max_length=100, default="")
    FourthItemDescription = models.TextField(max_length=300, default="")

    def __str__(self):
        return self.Template


class Images(models.Model):
    ImagesName = models.CharField(max_length=50, default="Template 1")
    category1 = models.CharField(max_length=50, blank=True, default="Category")
    title1 = models.TextField(max_length=100,blank=True, default="Name")
    category2 = models.CharField(max_length=50, blank=True, default="Category")
    title2 = models.TextField(max_length=100,blank=True, default="Name")
    category3 = models.CharField(max_length=50, blank=True, default="Category")
    title3 = models.TextField(max_length=100,blank=True, default="Name")
    category4 = models.CharField(max_length=50, blank=True, default="Category")
    title4 = models.TextField(max_length=100,blank=True, default="Name")
    category5 = models.CharField(max_length=50, blank=True, default="Category")
    title5 = models.TextField(max_length=100,blank=True, default="Name")
    category6 = models.CharField(max_length=50, blank=True, default="Category")
    title6 = models.TextField(max_length=100,blank=True, default="Name")

    def __str__(self):
        return self.ImagesName


class DownloadSession(models.Model):
    Template = models.CharField(max_length=50, default="Template 1")
    Title = models.CharField(max_length=100, default="Heading")
    Description = models.TextField(max_length=200, blank=True, default="Text Here")
    ButtonText = models.CharField(max_length=100, default="Download Now")
    ButtonLink = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.Template


class Contact(models.Model):
    Template = models.CharField(max_length=50, default="Template 1")
    Title = models.CharField(max_length=200, default="Your title here")
    Description = models.TextField(max_length=200)
    Phone = models.IntegerField()
    Email = models.TextField(max_length=150)

    def __str__(self):
        return self.Template


class All(models.Model):
    navigation = models.ForeignKey(Navigation, on_delete=models.CASCADE, verbose_name="Chose a navigation")
    session1 = models.ForeignKey(FirstPlace, on_delete=models.CASCADE, verbose_name="Chose a session 1")
    session2 = models.ForeignKey(AboutYou, on_delete=models.CASCADE, verbose_name="Chose a session 2")
    session3 = models.ForeignKey(YourService, on_delete=models.CASCADE, verbose_name="Chose a session 3")
    images = models.ForeignKey(Images, on_delete=models.CASCADE, verbose_name="Chose an images description")
    download = models.ForeignKey(DownloadSession, on_delete=models.CASCADE, verbose_name="Download session")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name="Contact session")