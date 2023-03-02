import pyexcel
from django.http.response import HttpResponse

from base.response import *


class ExportExcel:

    @staticmethod
    def create_xlsx(data, payload, serializer, filename):
        rows = [list(payload.values())]
        for obj in data:
            row = []
            data_serializer = serializer.to_representation(obj)
            for key in payload:
                row.append(data_serializer.get(key))
            rows.append(row)
        sheet = pyexcel.Sheet(rows)

        response = HttpResponse(sheet.xlsx, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        response.status_code = status.HTTP_200_OK

        return response

    contacts_payload = {
        'id': 'ID',
        'contact_name': 'NOMBRE DEL CONTACTO',
        'contact_phone': 'TELÉFONO DEL CONTACTO',
        'contact_email': 'CORREO DEL CONTACTO',
        'address': 'DIRECCIÓN',
        'birthday': 'FECHA CUMPLEAÑOS',
        'notes': 'NOTAS',
        'is_active': 'ESTA ACTIVO',
        'created_at': 'FECHA DE CREACIÓN',
        'updated_at': 'FECHA DE ACTUALIZACIÓN'
    }
