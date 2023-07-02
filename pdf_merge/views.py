import os
from django.conf import settings
from django.shortcuts import render
from PyPDF2 import PdfMerger
from django.http import FileResponse


def merge_pdfs(request):
    if request.method == 'POST':
        files = request.FILES.getlist('pdf_files')
        merger = PdfMerger()

        for file in files:
            merger.append(file)

        merged_pdf_path = os.path.join(settings.MEDIA_ROOT, 'merged.pdf')
        merger.write(merged_pdf_path)
        print("Merged PDF path:", merged_pdf_path)
        merger.close()

        response = FileResponse(open(merged_pdf_path, 'rb'), as_attachment=True, filename='merged.pdf')
        return response

    return render(request, 'pdf_merge/index.html')