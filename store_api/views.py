from django.db.models import Q
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StoreSerializer
from .models import store
from datetime import datetime
# Create your views here.


class StoreCreateView(mixins.CreateModelMixin,generics.ListAPIView,mixins.UpdateModelMixin):
    lookup_field = 'pk'
    serializer_class = StoreSerializer
    def get_queryset(self):
        qs= store.objects.all()
        search= self.request.GET.get("q")
        if search is not None:
            qs= qs.filter(Q(key__icontains=search)|Q(value__icontains=search))
            for item in qs:
                item.time= datetime.now()
                item.save()
            return qs

        return store.objects.all()
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

class StoreRudView(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin, APIView):
    lookup_field = 'pk'
    serializer_class = StoreSerializer

    def get_queryset(self):
        return store.objects.all()



    def get_object(self, pk):
        try:
            return store.objects.get(pk=pk)
        except store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        value = self.get_object(pk)
        value.time= datetime.now()
        value.save()
        serializer= StoreSerializer(value)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        value = self.get_object(pk)
        value.time= datetime.now()
        value.save()
        serializer = StoreSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        value = self.get_object(pk)
        value.time= datetime.now()
        value.save()
        serializer = StoreSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)