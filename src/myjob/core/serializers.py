from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import fields, serializers
from .models import (Job, ProfilUser, ProfilRetruteur, Competence, Formation, Experience)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash


class SetpassSerializers(Serializer):
    """
    Description: Model Description
    """
    old_password = fields.CharField(write_only=True, required=True)
    newpassword = fields.CharField(write_only=True, required=True)



class LoginSerializer(Serializer):
    """
    Description: Model Description
    """
    username = fields.CharField()
    password = fields.CharField(write_only=True, required=True)
    token = fields.SerializerMethodField()

    def get_token(self, instance: User):
        return Token.objects.get(user=instance).key

    class Meta:
        extra_kwargs = {'password': {"write_only": True}}


class UserSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    password = fields.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data):

        validated_data.pop('password')

        for key, value in validated_data.items():

            setattr(instance, key, value)

            instance.save()

        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'email',)
        extra_kwargs = {'password': {"write_only": True}}




class FormationSerializer(ModelSerializer):
    """
    Description: Model Description
    """

    class Meta:
        model = Formation
        fields = ('id', 'date_debut', 'date_fin', 'nom', 'lieux', 'description')
        pass


class CompetenceSerializer(ModelSerializer):
    """
    Description: Model Description
    """
     

    class Meta:
        model = Competence
        fields = ('id', 'niveau', 'description', 'nom')
        pass


class ExperienceSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    
   
    class Meta: 
         model = Experience
         fields = ('id', 'date_de_debut', 'date_de_fin', 'title,Description', 'lieux')


class ProfilRetruteurSerializer(ModelSerializer):
    """
    Description: Model Description
    """

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        abstract = False
        
        

class JobSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    

    class Meta:
       model = Job
       fields = ('id','titre', 'type_contra', 'salaire', 'date_debut', 'date_fin', 'description', 'competences', 'formations', 'experiences', 'Job_statue', 'domaine', 'nombres_experiences', 'postuler')



class ProfilUserSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    

    class Meta:
        model = ProfilUser
        fields = ('id','user', 'location','Description','adresse','nationalite '
,'birthday','cv', 'competences', 'formation', 'experience')
         