from cmath import e
from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize
from .models import corporate,user
from .serializers import corporateSerializer,userSerializer

from rest_framework.response import Response
class CompanyBasedListView(APIView):
    def get(self,request, *args, **kwargs):

        try:
            corporate_id = request.GET.get('corporate_id')
            if corporate_id != None:
                corporate_user = corporate.objects.filter(id=corporate_id)
                company_name= [str(i.company_name) for i in corporate_user][0]
                users = user.objects.filter(company = company_name)
                serializer = userSerializer(users,many=True)
                return Response({"corporate_user":serializer.data})
            else:
                return Response({"corporate id params required"})
                
        except :
            return Response('errror occurs')
    
