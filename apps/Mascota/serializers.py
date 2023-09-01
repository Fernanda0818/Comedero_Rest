from rest_framework import serializers,viewsets
 
# import the todo data model
from apps.Mascota.models import Mascota
 

# create a serializer class
class MascotaSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Mascota
        fields = '__all__'