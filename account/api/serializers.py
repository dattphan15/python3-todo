from rest_framework import serializers
# from account.models import Account
from django.contrib.auth import get_user_model

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.ModelField(
        model_field=get_user_model()()._meta.get_field('password'), required=False)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'date_joined', 'last_login')
        read_only_fields = ('id', 'date_joined', 'last_login')

    def create(self, attrs):
        """
        If password is left as None, strip it when restoring. If set, change
        the password
        """
        password = attrs.get('password', None)
        print("things")
        del attrs['password']
        # Save the password on the object so we can use it for authentication
        # during create
        self.newpassword = password

        user = super(AccountSerializer, self).create(attrs)
        if password:
            user.set_password(password)
            user.save()
        return user