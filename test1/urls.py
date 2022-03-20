from django.urls import path
from . import views

urlpatterns = [
    path("fund/<int:fund_id>", views.UpdateFundView.as_view(), name="fund_update"),
    path("", views.IndexView.as_view(), name="index"),
]
