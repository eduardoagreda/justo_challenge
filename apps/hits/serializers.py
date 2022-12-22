from rest_framework.serializers import ModelSerializer

from apps.hits.models import Hit

class HitModelSerializer(ModelSerializer):
    class Meta:
        model = Hit
        fields = ['id', 'name', 'description', 'failed_mission', 'assign_hitmans', 'owner']

    def create(self, validated_data):
        return Hit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.failed_mission = validated_data.get('failed_mission', instance.failed_mission)
        instance.assign_hitmans = validated_data.get('assign_hitmans', instance.assign_hitmans)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance