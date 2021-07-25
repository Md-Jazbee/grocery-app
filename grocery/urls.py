from . import views
from django.urls import path


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='grocery.signup'),
    path("", views.GroceryListView.as_view(), name="grocery.all"),
    path('add/', views.add_grocery, name="grocery.add"),
    path('delete/<int:id>', views.delete_grocery, name="grocery.delete"),
    path('update/<int:id>', views.update_grocery, name="grocery.update"),
]
