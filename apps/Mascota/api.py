from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from apps.Mascota.models import Mascota
from apps.Mascota.serializers import MascotaSerializer
from rest_framework.parsers import MultiPartParser, JSONParser

@api_view(['GET','POST'])
@parser_classes([MultiPartParser , JSONParser])
def mascota_api_view(request):
    # list
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        mascotas_serializer = MascotaSerializer(mascotas,many=True)
        return Response( mascotas_serializer.data, status=status.HTTP_200_OK )

    # Create
    elif request.method == 'POST':
        mascotas_serializer = MascotaSerializer(data=request.data)
        if mascotas_serializer.is_valid():
            mascotas_serializer.save()
            return Response( {
                'message':'¡Mascota registrada correctamente!',
                'mascota': mascotas_serializer.data
            }, status=status.HTTP_201_CREATED )
        return Response( mascotas_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET','PUT','DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def mascotas_detail_api_view(request, pk=None):
    # Queryset
    mascota = Mascota.objects.filter( idMascota = pk ).first()
    
    # Validacion
    if mascota:
        # Retrieve
        if request.method == 'GET':
            mascotas_serializer =  MascotaSerializer(mascota)
            return Response( mascotas_serializer.data, status=status.HTTP_200_OK )
        
        # Update
        elif request.method == 'PUT':
            mascotas_serializer = MascotaSerializer(mascota, data = request.data)
            if mascotas_serializer.is_valid():
                mascotas_serializer.save()
                return Response( { 
                    'message':'¡Mascota actualizada correctamente!',
                    'mascota': mascotas_serializer.data
                }, status=status.HTTP_200_OK)
            print('ERROR MASCOTA')
            print(mascotas_serializer.errors)
            return Response(mascotas_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            mascota = Mascota.objects.filter( idMascota = pk ).first()
            mascota.delete()
            return Response(
                {'message':'¡Mascota eliminado correctamente!'}, 
                status=status.HTTP_200_OK
            )
    return Response(
        {'message':'No se encontró la mascota'}, 
        status=status.HTTP_400_BAD_REQUEST
    )