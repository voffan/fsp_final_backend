from django.urls import path
from .views import ResultView, FSResultsView
from .views import ColumnPreviewAPIView
from .views import ResultUploadAPIView


urlpatterns = [
    path('', ResultView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ResultView.as_view({'get': 'retrieve'})),
    path('filter/', FSResultsView.as_view({'get': 'list', 'post':'search'})),
    path("preview-column/", ColumnPreviewAPIView.as_view(), name="preview_column"),
    path("upload/", ResultUploadAPIView.as_view(), name="upload"),
]