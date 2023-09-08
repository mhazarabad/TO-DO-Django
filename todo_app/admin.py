from django.contrib import admin,messages
from . import models


from django.contrib.admin import SimpleListFilter


class PassedTodo(SimpleListFilter):
    title = 'time management' # or use _('country') for translated title
    parameter_name = 'time_management'

    def lookups(self, request, model_admin):
        return [('0','missed deadline'),('1','missed to start')]

    def queryset(self, request, queryset):
        match self.value():
            case '0':
                return queryset.filter(id__in=models.Todo.sort_todo_by_passed_deadline().values_list('id',flat=True))
            case '1':
                return queryset.filter(id__in=models.Todo.filter_missed_start_todo().values_list('id',flat=True))
            case _:
                return queryset

@admin.register(models.Todo)
class ClientAdmin(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        try:
            return super().add_view(request, form_url, extra_context)
        except Exception as e:

            request.method = 'GET'
            messages.error(request, e)
            return super().add_view(request, form_url, extra_context)
        
    def delete_view(self, request, form_url='', extra_context=None):
        try:
            return super().delete_view(request, form_url, extra_context)
        except Exception as e:

            request.method = 'GET'
            messages.error(request, e)
            return super().delete_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        try:
            return super().change_view(request, object_id, form_url, extra_context)
        except Exception as e:

            request.method = 'GET'
            messages.error(request, e)
            return super().change_view(request, object_id, form_url, extra_context)
        
    list_per_page = 15

    list_display = ['name','description','status','_display_start_date_for_admin','_display_due_date_for_admin']

    list_display_links = ['name']
    search_fields = ['name','description','start_date','due_date']
    sortable_by = ['name','status','_display_start_date_for_admin','_display_due_date_for_admin']
    list_filter = ['status',PassedTodo]
    list_editable = ['status']

