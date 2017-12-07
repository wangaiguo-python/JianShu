import csv
from django.http import HttpResponse
import datetime

def export_as_csv_action(description='Export selected objects as CSV file',
                         fields=None, exclude=None, header=True):
    '''
    this function returns an export csv action 
    :param fields:  :param exclude:   work  like in django ModelForm
    :param header:   is whether or not to output the column names as the first row
    '''
    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        if not fields:
            field_names = [field.name for field in opts]
        else:
            field_names = fields


        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name.encode('utf-8')) #转化下显示格式

        writer = csv.writer(response)
        if header:
            writer.writerow(field_names)
        for obj in queryset:
            # 正常的这样处理就行了
            row = [getattr(obj, field)() if callable(getattr(obj, field)) else getattr(obj, field) for field in field_names]

            # 如果新添处理功能  比如处理下时间的显示格式
            # row = []
            # for field in field_names:
            #     value = getattr(obj, field)
            #     if isinstance(value, datetime.datetime):
            #         value = value.strftime('%d/%m/%Y')
            #     row.append(value)

            writer.writerow(row)

        return response

    export_as_csv.short_description = description
    return export_as_csv
