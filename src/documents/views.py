import re
from io import BytesIO
from documents.helpers import handle_file
from src.constanst import PLAIN_DOCUMENT_TYPES
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from django.http import JsonResponse
from documents.models import DocumentFormat
from django.http.response import HttpResponseBadRequest
from documents.serializers import DocumentFormatSerializer
from rest_framework.pagination import PageNumberPagination
from django.http import FileResponse

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class DocumentsView(CreateAPIView,ListAPIView):
    model=DocumentFormat
    serializer_class = DocumentFormatSerializer
    queryset =  DocumentFormat.objects.all()
    pagination_class = CustomPagination
    def post(self,request):
        file = None
        try:
            source = request.data.dict()
            if not "format" in source.keys():
                return HttpResponseBadRequest("You must specify file or format on the payload, please read the doc")
            file = source["format"]
            file_buffer = BytesIO(file.read())
            file_type = file.content_type.upper().split("/")[-1]
            if file_type not in PLAIN_DOCUMENT_TYPES and not("XLSX" in file_type or "SPREADSHEETML" in file_type) and not("WORDPROCESSINGML" in file_type or "DOCX" in file_type):
                return HttpResponseBadRequest("This type of doc is not allowed")
            if "XSLX" in file_type or "SPREADSHEETML" in file_type:
                file_type="XLSX"
            elif "WORDPROCESSINGML" in file_type or "DOCX" in file_type:
                file_type="DOCX"
            plain_text = handle_file(file_buffer,file_type)

        except AttributeError as e:
            if not "format" in request.data.keys():
                return HttpResponseBadRequest("You must specify file or format on the payload, please read the doc")
            plain_text = request.data["format"]
            file_type = "PLAIN"
        expression_to_find = re.findall(r'{{(.*?)}}',plain_text)
        if expression_to_find == []:
            return HttpResponseBadRequest("Your document does not have a {{}} elements , pls check")
        if file:
            new_format = DocumentFormat(format=expression_to_find,file_type=file_type,plain=plain_text,original_file=file)
        else:
            new_format = DocumentFormat(format=expression_to_find,file_type=file_type,plain=plain_text)
        new_format.save()
        return JsonResponse({"message":f"New format Document Created, your format document has these keys","format_id":new_format.id,"keys":expression_to_find})
    

class DocumentsDetailView(RetrieveAPIView):
    model=DocumentFormat
    serializer_class = DocumentFormatSerializer
    queryset =  DocumentFormat.objects.all()


class FillDocument(RetrieveAPIView):
    model=DocumentFormat
    serializer_class = DocumentFormatSerializer
    queryset =  DocumentFormat.objects.all()

    def get(self,request,pk):
        document = self.get_object()
        file_buffer = BytesIO(document.original_file.read())
        #write_pdf(file_buffer,{"nombre_contratante":"Juanito","cedula_contratante":"1000"})
        print(document.original_file.path)
        return FileResponse(open(document.original_file.path, "rb"))