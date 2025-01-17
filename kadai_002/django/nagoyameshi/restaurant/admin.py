from django.contrib import admin
from .models import Category, Restaurant, Reservation, Review, Favorite, CompanyInfo, TermsOfService


admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Favorite)

admin.site.register(CompanyInfo)
admin.site.register(TermsOfService)
