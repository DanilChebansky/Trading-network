from rest_framework.serializers import ModelSerializer
from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone",
            "first_name",
            "last_name",
            "is_active",
        )
