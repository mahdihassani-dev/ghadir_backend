# your_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hadith
import random


@api_view(['GET'])
def random_hadith(request):
    count = Hadith.objects.count()
    if count == 0:
        return Response({"error": "هیچ حدیثی وجود ندارد."}, status=404)

    random_index = random.randint(0, count - 1)
    hadith = Hadith.objects.all()[random_index]

    return Response({
        "person": hadith.person,
        "text": hadith.text,
        "source": hadith.source
    })
