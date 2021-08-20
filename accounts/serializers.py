from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'first_name', 'Last_name', 'is_active']