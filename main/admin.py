from django.contrib import admin
from .models import Category,Portfel,AboutMe,Skill,Service,ContactMessage,SocialMedia


admin.site.register(Portfel)
admin.site.register(Category)
admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(SocialMedia)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'has_author_info','message')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)
    
    # Foydalanuvchi ma'lumotlari va sizning ma'lumotlaringizni alohida guruhlash
    fieldsets = (
        ('Foydalanuvchi Xabari', {
            'fields': ('name', 'email', 'phone', 'subject', 'message')
        }),
        ('Mening Kontakt Maʼlumotlarim', {
            'fields': ('author_email', 'author_phone', 'position', 'address'),
            'description': 'Bu maʼlumotlar saytning kontakt boʻlimida koʻrsatiladi'
        }),
        ('Qoʻshimcha', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def has_author_info(self, obj):
        return bool(obj.author_email)
    has_author_info.boolean = True
    has_author_info.short_description = 'Author info'

admin.site.register(ContactMessage, ContactMessageAdmin)
