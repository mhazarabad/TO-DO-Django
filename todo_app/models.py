from django.db import models

class TodoStatusTranslatorMixin:
    @staticmethod
    def _check_unknown_status_state(unknown_status,status_choices:tuple):
        if unknown_status in [choice[0] for choice in status_choices]:
            return 'id'
        elif unknown_status in [choice[1] for choice in status_choices]:
            return 'verbose'
        else:
            raise Exception("invalid status")
        
    @classmethod
    def get_status_id(cls,unknown_status,status_choices:tuple) -> str:
        match cls._check_unknown_status_state(unknown_status=unknown_status,status_choices=status_choices):
            case 'id':
                return unknown_status
            case 'verbose':
                return dict((status_verbose, status_id) for status_id, status_verbose in status_choices)[unknown_status]
            
    @classmethod
    def get_status_verbose(cls,unknown_status,status_choices:tuple) -> str:
        match cls._check_unknown_status_state(unknown_status=unknown_status,status_choices=status_choices):
            case 'id':
                return dict((status_id, status_verbose) for status_id, status_verbose in status_choices)[unknown_status]
            case 'verbose':
                return unknown_status

class DateTimeTranslatorMixin:
    from datetime import datetime

    @staticmethod
    def create_datetime_object_from_string(datetime_string:str):
        from datetime import datetime
        from pytz import timezone
        
        if len(datetime_string.split(' '))!=3:
            raise Exception("datetime string format is not valid, should be: 'D/M/Y H:M:S tz', sample: '14/5/2022 12:15:23 utc'")
        date_string,time_string,timezone_string=datetime_string.split(' ')

        date_string=date_string.split('/')
        date_string=[int(data) for data in date_string]
        if len(date_string)!=3:
            raise Exception("date format is not valid, should be: D/M/Y, sample: '24/5/2023' ")
        
        time_string=time_string.split(':')
        time_string=[int(data) for data in time_string]
        if len(time_string)!=3:
            raise Exception("date format is not valid, should be: H:M:S, sample: '16:17:23' ")
        
        try:
            timezone_object=timezone(zone=timezone_string)
        except:
            raise Exception("zone string is not valid, sample: 'utc'")
        
        return datetime(year=date_string[2],month=date_string[1],day=date_string[0],hour=time_string[0],minute=time_string[1],second=time_string[2],tzinfo=timezone_object)

    @staticmethod
    def convert_timezone(datetime:datetime,desierd_timezone:str='utc'):
        from datetime import datetime
        from pytz import timezone
        if not datetime.tzinfo:
            datetime.replace(timezone('utc'))
        return datetime.astimezone(timezone(desierd_timezone))
    
    @staticmethod
    def export_to_visible_datetime(time_object:datetime):
        return time_object.strftime('%d/%m/%Y %H:%M:%S %Z')
    


class CommonFieldsAbs(models.Model):
    from uuid import uuid4
    id=models.UUIDField(primary_key=True,editable=False,default=uuid4)
    creation_datetime=models.DateTimeField(auto_now_add=True,editable=False)
    last_update_datetime=models.DateTimeField(auto_now=True,editable=False)
    from django.contrib.auth.models import User

    class Meta:
        ordering=('-last_update_datetime',)
        abstract=True
        
class Todo(CommonFieldsAbs,TodoStatusTranslatorMixin,DateTimeTranslatorMixin):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    STATUS_CHOICES=(
        ('1','todo'),
        ('2','in progress'),
        ('3','done'),
    )
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,default='1')
    start_date=models.DateTimeField(blank=True,null=True)
    due_date=models.DateTimeField(blank=True,null=True)


    @classmethod
    def filter_query_with_paginator(cls,page:int=1,result_per_page:int=9,**kwargs):
        page=page if page>=1 else 1
        total_result_number=cls.objects.all().count()
        total_pages=total_result_number//result_per_page
        total_pages=total_pages if total_pages>0 else 1
        max_page=total_pages if total_result_number%result_per_page == 0 else total_pages+1
        page=max_page if page>max_page else page
        return cls.objects.filter(**kwargs)[(page-1)*result_per_page:page*result_per_page],max_page

    def _display_start_date_for_admin(self):
        return DateTimeTranslatorMixin.export_to_visible_datetime(time_object=self.start_date) if self.start_date else '-'
    _display_start_date_for_admin.short_description = 'start date'

    def _display_due_date_for_admin(self):
        return DateTimeTranslatorMixin.export_to_visible_datetime(time_object=self.due_date) if self.due_date else '-'
    _display_due_date_for_admin.short_description = 'due date'

    @classmethod
    def filter_missed_start_todo(cls,**kwargs):
        from django.utils import timezone
        return cls.objects.filter(start_date__lte=timezone.now(),status__in=['1'],**kwargs).order_by('start_date')

    @classmethod
    def sort_todo_by_closer_due_date(cls,**kwargs):
        return cls.objects.filter(**kwargs).order_by('due_date')
    
    @classmethod
    def sort_todo_by_closer_start_date(cls,**kwargs):
        return cls.objects.filter(**kwargs).order_by('start_date')
    
    @classmethod
    def sort_todo_by_passed_deadline(cls,**kwargs):
        from django.utils import timezone
        return cls.objects.filter(due_date__lte=timezone.now(),status__in=['1','2'],**kwargs).order_by('due_date')

    @property
    def export_to_response(self):
        return {
            "id":str(self.id),
            "name":self.name,
            "description":self.description,
            "status_id":self.status,
            "status_verbose":self.get_status_display(),
            "start_date":DateTimeTranslatorMixin.export_to_visible_datetime(time_object=self.start_date) if self.start_date else None,
            "due_date":DateTimeTranslatorMixin.export_to_visible_datetime(time_object=self.due_date) if self.due_date else None,
            "creation_datetime":DateTimeTranslatorMixin.export_to_visible_datetime(time_object=self.creation_datetime),
            "last_update_datetime":DateTimeTranslatorMixin.export_to_visible_datetime(time_object=self.last_update_datetime),
        }

    @property
    def export_for_json_response(self):
        from json import dumps
        return dumps(self.export_to_response)

    class Meta(CommonFieldsAbs.Meta):
        verbose_name='ToDo'
        verbose_name_plural='ToDos'
    
    def __str__(self) -> str:
        return '{}'.format(self.name[:20])
    
