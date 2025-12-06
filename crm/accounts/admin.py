from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Page Adimin Dashboard
admin.site.site_header = "ACLEDA University of Business"
admin.site.site_title = "ACLEDA University of Business Admin Panel"
admin.site.index_title = "ACLEDA University of Business Admin Panel"

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.productImage:
            return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.productImage.url)
        return "No Image"
    
    image_preview.short_description = 'Image Preview'
    
    # Using camelCase to match your CURRENT models.py
    list_display = ["image_preview", "productName", "categoryID", "price", "quantity", "productDate"]
    list_filter = ["productDate"]
    search_fields = ["productName"]
    date_hierarchy = "productDate"
    list_per_page = 10
   
    readonly_fields = ["image_preview"]
    

admin.site.register(Products, ProductAdmin)
admin.site.register(Image)
admin.site.register(ImageType)


#===========================
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductDetailImage)
admin.site.register(Book)

admin.site.register(Item)

admin.site.register(BillingDetail)
