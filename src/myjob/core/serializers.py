from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import fields
from .models import (Job, ProfilUser, ProfilRetruteur, Competence, Formation, Experience)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


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
        read_only_fields = ['id', 'password']
        fields = ('id', 'username', 'password', 'first_name', 'email',)
        extra_kwargs = {'password': {"write_only": True}}




class FormationSerializer(ModelSerializer):
    """
    Description: Model Description
    """

    def create(self, validated_data):
        return Formation.objects.create(**validated_data)

    def update(self, instance:Formation, validated_data):
        
        for key, value in validated_data.items():

            setattr(instance, key, value)
            
            instance.save()

        return instance

    class Meta:
        model = Formation

        fields = ('id', 'date_debut', 'date_fin', 'nom', 'lieux', 'description')
        pass


class CompetenceSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    def create(self, validated_data):
        return Competence.objects.create(**validated_data)
     
    def update(self, instance:Competence, validated_data):
        
        for key, value in validated_data.items():

            setattr(instance, key, value)
            
            instance.save()

        return instance

    class Meta:
        model = Competence
        fields = ('id', 'niveau', 'description', 'nom')
        pass


class ExperienceSerializer(ModelSerializer):
    """
    Description: Model Description
    """

    def create(self, validated_data):
        return Experience.objects.create(**validated_data)

    def update(self, instance:Experience, validated_data):
        
        for key, value in validated_data.items():

            setattr(instance, key, value)
            
            instance.save()

    class Meta: 
         model = Experience
         fields = ('id', 'date_de_debut', 'date_de_fin', 'title','Description', 'lieux')


class ProfilRetruteurSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    def create(self, validated_data):
        return ProfilRetruteur.objects.create(**validated_data)

    def update(self, instance:ProfilRetruteur, validated_data):
        validated_data.pop('user')

        for key, value in validated_data.items():

            setattr(instance, key, value)
            
            instance.save()

    class Meta:
        model = ProfilRetruteur
        fields = ('id','user', 'location','Description','adresse','nationalite',)
        

class ProfilUserSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    

    def create(self, validated_data):
        #create a users instance 
        
        #creat
        competences_serialize = validated_data.get('competences')
        formations_serialize = validated_data.get('formations')
        experiences_serialize = validated_data.get('experiences') 
        Description = validated_data.get('Description')
        adresse = validated_data.get('adresse')
        nationalite = validated_data.get('nationalite')
        validated_data.pop('competences')
        validated_data.pop('formations')
        validated_data.pop('experiences')

        profil =ProfilUser.objects.create(**validated_data)
        #profil.competences.add()


        for comp in competences_serialize:
            profil.competences.add(comp)
            
        for comp in formations_serialize:
            profil.formations.add(comp)
        
        for comp in experiences_serialize:
            profil.experiences.add(comp)
        

        return profil

    def update(self, instance:ProfilUser, validated_data):
        validated_data.pop('user')
        
        for key, value in validated_data.items():

            setattr(instance, key, value)
            
            instance.save()

    class Meta:
        model = ProfilUser
        fields = ('id','user', 'location','Description','adresse','nationalite'
,'birthday','cv', 'competences', 'formations', 'experiences')


class JobSerializer(ModelSerializer):
    """
    Description: Model Description
    """
    postuler = ProfilUserSerializer(many=True)
    
    def create(self, validated_data):

        return Job.objects.create(**validated_data)


    def update(self, instance:Job, validated_data):
        validated_data.pop('user')
        
        for key, value in validated_data.items():

            setattr(instance, key, value)
            
            instance.save()

    class Meta:
       model = Job
       fields = ('id','titre', 'type_contrat', 'salaire_min','salaire_max','postuler', 'date_debut', 'date_fin', 'description', 'work_location', 'nombres_experiences')



class FindJobSerializer(Serializer):
    """
    Description: Model Description
    """
    titre = fields.CharField(write_only=True, required=True)
    type_contrat = fields.CharField(write_only=True,required=False)
    salaire_min =  fields.IntegerField(default=0)
    date_debut = fields.DateTimeField()
    date_fin = fields.DateTimeField()
    description = fields.CharField(write_only=True, required=False)
    salaire_max = fields.IntegerField(default=0)
    work_location =  fields.CharField(max_length=200)
    nombres_experiences = fields.IntegerField(default=0)
   
    

         