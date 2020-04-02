from django.contrib import admin
from .models import Navigation
from .models import First
from .models import Second
from .models import Third
from .models import Images
from .models import DownloadSession
from .models import Contact
from .models import All


admin.site.register(Contact)
admin.site.register(DownloadSession)
admin.site.register(Images)
admin.site.register(Third)
admin.site.register(Second)
admin.site.register(First)
admin.site.register(Navigation)
admin.site.register(All)
