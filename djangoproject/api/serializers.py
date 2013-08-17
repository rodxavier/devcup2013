from rest_framework import serializers

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile')
        
    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.username = attrs.get('username', instance.username)
            instance.email = attrs.get('email', instance.email)
            instance.mobile = attrs.get('mobile', instance.mobile)
            return instance
        # Create new instance
        return User(**attrs)
