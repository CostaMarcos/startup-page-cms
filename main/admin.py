from django.contrib import admin
from .models import Navigation
from .models import FirstPlace
from .models import AboutYou
from .models import YourService
from .models import Images
from .models import DownloadSession
from .models import Contact
from .models import All


admin.site.register(Contact)
admin.site.register(DownloadSession)
admin.site.register(Images)
admin.site.register(YourService)
admin.site.register(AboutYou)
admin.site.register(FirstPlace)
admin.site.register(Navigation)
admin.site.register(All)
