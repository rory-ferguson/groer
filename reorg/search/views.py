import xlwt

from django.views.generic import ListView
from django.http import HttpResponse, JsonResponse

from connect.models import OpenPayments


class SearchResultsView(ListView):
    model = OpenPayments
    template_name = 'search/search.html'

    def get_queryset(self):
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            self.request.session['results'] = query
            object_list = OpenPayments.objects.filter(physician_first_name__icontains=query)
            return object_list
        
    def post(self, request, *args, **kwargs):
        query = request.session['results']
        results = OpenPayments.objects.filter(physician_first_name__icontains=query).values()
        response = create_xls(results)
        return response



def autocomplete(request):
    model = OpenPayments
    query = list(OpenPayments.objects.values_list('physician_first_name', flat=True).distinct())
    return JsonResponse(query, safe=False)

def create_xls(results):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=General-Payment-Data-Detailed-Dataset-2015-Reporti.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dataset')

    columns = [i for i in results[0].keys()]  # define columns

    for j, col in enumerate(columns):  # Write columns
        ws.write(0, j, col)

    for i, row in enumerate(results, 1):  # Write rows
        for j, col in enumerate(columns):
            ws.write(i, j, row[col])

    wb.save(response)
    return response