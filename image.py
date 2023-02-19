from django.conf import settings
from django.conf.urls.static import static

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')