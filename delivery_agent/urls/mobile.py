from django.urls import path

from delivery_agent.views import mobile

urlpatterns = [
    path("order/list/", mobile.OrderListAPI.as_view()),
    path("order/status/picked/<str:id>/", mobile.OrderStatusPickedAPI.as_view()),
    path("order/status/delivered/<str:id>/", mobile.OrderStatusDeliveredAPI.as_view()),
]
