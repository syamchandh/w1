from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include("connectionApp.urls"))
    path('',views.start),
    path('adding_emp',views.adding_emp,name="adding_emp"),
    path('show_emp',views.show_emp,name='show_emp'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_pro_details/<int:pk>',views.edit_pro_details,name='edit_pro'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('delete_product/<int:pk>',views.delete_product,name='deletepro')
]