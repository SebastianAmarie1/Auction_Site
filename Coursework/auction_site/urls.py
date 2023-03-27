from django.urls import path
from . import views

app_name = "auction_site"

urlpatterns = [
    
    path('api/products/', views.products_api),
    path('api/products/<int:product_id>/', views.product_api_indv),
    path('api/reviews/', views.reviews_api),
    path('api/reviews/<int:rev_id>/', views.reviews_api_indv),
    path('api/replies/', views.replies_api),
    path('api/replies/<int:rep_id>/', views.replies_api_indv),
    path('api/bids/', views.bids_api),
    path('api/bids/<int:pro_id>/', views.bids_api_indv),
    path('api/usersup/', views.users_api_indv),
    path('api/sign_in/', views.sign_in),
    path('api/sign_up/', views.sign_up),
    path('api/sign_out/', views.sign_out),
    path('api/check_logged_in/', views.check_logged_in),
]