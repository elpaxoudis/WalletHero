from rest_framework import serializers
from register.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'surname', 'username', 'password')

	# creates a new instance
	def create(self, validated_data):
		return User.objects.create(**validated_data)