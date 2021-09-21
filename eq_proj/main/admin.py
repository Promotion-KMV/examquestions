from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Question
from .models import Exam
from .models import Vendor
from .models import Order



admin.site.register(Vendor)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Order)
