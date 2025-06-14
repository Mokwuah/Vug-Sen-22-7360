from rest_framework.routers import DefaultRouter
from .views import ListJobView

router = DefaultRouter()
router.register('Job-Trackerpy', ListJobView)

urlpatterns = router.urls

#http://127.0.0.1:8000/Job-Trackerpy/ link for access


