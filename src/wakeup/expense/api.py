
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *






class ExpenseView(ViewSet):
    base_url = r'/expense'
    base_name = ''

    def create(self, request):
        if not request.user.is_authenticated():
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
        try:
            data = request.data
            name = data['name'] if 'name' in data.keys() else ""
            amount = data['amount'] if 'amount' in data.keys() else 0
            date = data['date'] if 'date' in data.keys() else None
            result = True
            try:
                DailyExpenses.objects.create(user=request.user, name=name, amount=amount,day=date)
            except Exception as e:
                print str(e)
                result = False

            if result:
                return Response({"result": "Amount added", "status": True})
            else:
                return Response({"result": "Failed to add amount", "status": False})
        except Exception as e:
            print str(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        if not request.user.is_authenticated():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if request.method == "GET":
            result = []
            for obj in DailyExpenses.objects.all():
                result.append({"date":obj.day,"amount":obj.amount,"description":obj.name,"user":obj.user.username})
            return Response(result)

    def retrieve(self, request, code=None):
        if not request.user.is_authenticated():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

