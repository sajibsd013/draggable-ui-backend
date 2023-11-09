from rest_framework import serializers
from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username', 'password']

    def save(self):
        user = MyUser(
            username=self.validated_data['username'])

        user.set_password(self.validated_data['password'])
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(
                {'current_password': 'Does not match'})
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["id","username","full_name","email","birthday","is_admin","user_type"]
        # fields = "__all__"

