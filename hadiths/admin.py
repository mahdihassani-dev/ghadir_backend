from django.contrib import admin
from .models import Hadith

@admin.register(Hadith)
class HadithAdmin(admin.ModelAdmin):
    # فیلدهایی که در جدول لیست ادمین نمایش داده میشن
    list_display = ('id', 'short_arabic_text', 'short_persian_text')
    
    # اضافه کردن باکس جستجو بر اساس متن عربی و فارسی
    search_fields = ('arabic_text', 'persian_text')

    # متد برای خلاصه کردن متن عربی در لیست (برای جلوگیری از شلوغی صفحه)
    def short_arabic_text(self, obj):
        if len(obj.arabic_text) > 50:
            return obj.arabic_text[:50] + ' ...'
        return obj.arabic_text
    short_arabic_text.short_description = 'متن عربی'

    # متد برای خلاصه کردن متن فارسی در لیست
    def short_persian_text(self, obj):
        if len(obj.persian_text) > 50:
            return obj.persian_text[:50] + ' ...'
        return obj.persian_text
    short_persian_text.short_description = 'متن فارسی'