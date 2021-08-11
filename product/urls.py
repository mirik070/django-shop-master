from rest_framework import routers

from other.views import ProjectViewSet

router = routers.SimpleRouter()
router.register(r'project', ProjectViewSet)
urlpatterns = router.urls
