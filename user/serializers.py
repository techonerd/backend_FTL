from rest_framework import serializers
from .models import User, Activity


class GetActivityPeriods(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ('start_time', 'end_time')

    def get_start_time(self, obj):
        return obj.start_time.strftime("%b %-d %Y %-I:%-M%p")

    def get_end_time(self, obj):
        return obj.end_time.strftime("%b %-d %Y %-I:%-M%p")


class GetUserSerializer(serializers.ModelSerializer):
    Activity = GetActivityPeriods(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'tz', 'Activity')
