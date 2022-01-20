from rest_framework.permissions import IsAuthenticated
from rest_framework import routers, serializers, viewsets, views, status
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, UpdateModelMixin, RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from .serializers import (ProfilRetruteurSerializer, SetPasswordSerializers, LogoutSerializer, MetierSerializer, UserSerializer, FindJobSerializer, LoginSerializer, RetruterSerializer, SetpassSerializers, FormationSerializer, CompetenceSerializer, ExperienceSerializer, JobSerializer, PostulerSerializer, ProfilUserSerializer)
from django.contrib.auth import logout, login, authenticate
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (Job, ProfilUser, ProfilRetruteur, Competence, Formation, Experience, Postuler, Metier,Travail, Choix)
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny, SAFE_METHODS
from django.contrib.auth.models import  User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


class SetPasswordView(GenericViewSet):
    """
    Description: Model Description
    """
    
    serializer_class =  SetPasswordSerializers

    @swagger_auto_schema(
        operation_description='send mail to a user and reset your password. ')
    @action(methods=["POST"], detail=False)
    def set_Password_mail(self, request, *args, **kwargs):
        user_lost_pass = SetPasswordSerializers(data=self.request.data)
        user_lost_pass.is_valid(raise_exception=True)
        userrs = user_have_job.validated_data.get('email')
        

       # user_find = UserSerializer(many=True, data=list_user_postuler)

        # do something with the book
      
        return Response({'resultat':''}, status=status.HTTP_200_OK)




class ProfilRetruteurViewset(RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                    UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """
    queryset = ProfilRetruteur.objects.all()
    serializer_class = ProfilRetruteurSerializer
    permission_classes = [IsAuthenticated, ]

# ViewSets define the view behavior.
class UserViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                  UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]


class PostulerVieset(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                  UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """
    queryset = Postuler.objects.all()
    serializer_class = PostulerSerializer
    permission_classes = [IsAuthenticated, ]

    
class RetruterPostuler(GenericViewSet):
    """
    Description: Model Description
    """
    serializer_class = RetruterSerializer
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        request_body=RetruterSerializer(),
        operation_description='method to find Job with  using the name of job. ')
    @action(methods=["POST"], detail=False)
    def retruter(self, request, *args, **kwargs):
        user_have_job = RetruterSerializer(data=self.request.data)
        user_have_job.is_valid(raise_exception=True)
        userrs = user_have_job.validated_data.get('user_id')
        postuler = Postuler.objects.all()
        list_user_postulers = postuler.filter(job_id=user_have_job.validated_data.get('job_id'))
        for user in list_user_postulers:
            user.response_status =  'REFUSER'
            user.save()

            
        list_user_postuler = []

        for retruter_job  in userrs:
            username = retruter_job.get('username')
            user = User.objects.get(username=username)
            

            try:
                job_id = user_have_job.validated_data.get('job_id')
                postul = postuler.get(job_id=job_id, user_id=user.pk)
            
                postul.set_retruter(user, job_id)
                list_user_postuler.append(user)

            except Exception as e:
                raise e
            
            
        list_user_postuler = UserSerializer(many=True, data=list_user_postuler)

        # do something with the book
      
        return Response({'resultat':print(list_user_postuler)}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=RetruterSerializer(),
        operation_description='get  the numbers of personne who have poster to a job. ')
    @action(methods=["POST"], detail=False)
    def get_number(self, request, *args, **kwargs):
        user_have_job = RetruterSerializer(data=self.request.data)
        user_have_job.is_valid(raise_exception=True)
        userrs = user_have_job.validated_data.get('user_id')
        postuler = Postuler.objects.all()
        list_user_postuler = postuler.filter(job_id=user_have_job.validated_data.get('job_id')).count()
        

        # do something with the book
      
        return Response({'postuler': str(list_user_postuler)}, status=status.HTTP_200_OK)




class FilterFind(GenericViewSet):
    """
    Description: Model Description
    """
    
    permission_classes = [AllowAny, ]
    serializer_class = FindJobSerializer
    filtering = {
        'titre':['startswith']
    }
    def index(request):
        lastest_Job_list = Travail.objects.order_by('-pub_date')[:10]
        context = {
        'lastest_job_list': lastest_Job_list,
    }
        return render(request, 'core/index.html', context)
def detail(request, job_id):
    try:
        job = Choix.objects.get(pk=job_id)
        context = {
                'job': job
        }
       # date = timezone.now()
    except Travail.DoesNotExist:
        raise Http404("job does not exist")
    return render(request, 'core/detail.html', context)
def nbre_place(request, travail_id):
    travail = get_object_or_404(Travail, pk=travail_id)
    try:
        selected_choice = travail.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choix.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, '/detail.html', {
            'travail': travail,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.nbre_place += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('core:results', args=(travail.id,)))
def results(request, travail_id):
    question = get_object_or_404(Travail, pk=travail_id)
    return render(request, 'core/results.html', {'question': question})
    # Logout Ressource

    @swagger_auto_schema(
        request_body=FindJobSerializer(),
        operation_description='method to find Job with  using the name of job. ')
    @action(methods=["POST"], detail=False)
    def findbyname(self, request, *args, **kwargs):
        
        seria_job = FindJobSerializer(data=self.request.data)
        seria_job.is_valid(raise_exception=True)

        
        name =  seria_job.validated_data.get('titre')
        
        job = Job.objects.all()
        result = Job.objects.filter(titre__startswith=name).all()
        
        
        if result:

            result_de_recherche  = JobSerializer(result, many=True).data
            
             
            return Response({'resultat':result_de_recherche}, status=status.HTTP_200_OK)

             
        return Response({}, status=status.HTTP_404_NOT_FOUND)



    @swagger_auto_schema(
        request_body=FindJobSerializer(),
        operation_description='method to find Job with  using the name of job. ')
    @action(methods=["POST"], detail=False)
    def findName_metier(self, request, *args, **kwargs):
        
        seria_job = FindJobSerializer(data=self.request.data)
        seria_job.is_valid(raise_exception=True)

        
        name =  seria_job.validated_data.get('titre')
        metier = seria_job.validated_data.get('metier')
        
        job = Job.objects.all()
        result = Job.objects.filter(titre__startswith=name, metier__contains=metier).all()
        
        
        if result:

            result_de_recherche  = JobSerializer(result, many=True).data
            
             
            return Response({'resultat':result_de_recherche}, status=status.HTTP_200_OK)

             
        return Response({}, status=status.HTTP_404_NOT_FOUND)


    @swagger_auto_schema(
        request_body=FindJobSerializer(),
        operation_description='method to find Job with  using the name of job. ')
    def findName_metier_salaire(self, request, *args, **kwargs):
        
        seria_job = FindJobSerializer(data=self.request.data)
        seria_job.is_valid(raise_exception=True)

        
        name =  seria_job.validated_data.get('titre')
        metier = seria_job.validated_data.get('metier')
        salaire_min = seria_job.validated_data.get('salaire_min')
        
        job = Job.objects.all()
        result = Job.objects.filter(titre__startswith=name, metier__contains=metier, salaire_min=salaire_min).all()
        
        
        if result:

            result_de_recherche  = JobSerializer(result, many=True).data
            
             
            return Response({'resultat':result_de_recherche}, status=status.HTTP_200_OK)

             
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    

class AuthViewSet(GenericViewSet):
    """
    Description: Model Description
    """
    serializer_class = LoginSerializer
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        request_body=LoginSerializer(),
        operation_description="Check the credentials and return the REST Token if the credentials are valid and authenticated. Calls Django Auth login method to register User ID in Django session framework Accept the following POST parameters: username, password Return the REST Framework Token Object\'s key.")
    @action(methods=["POST"], detail=False)

    def signin(self, request, *args, **kwargs):

        seria = LoginSerializer(data=self.request.data)
        seria.is_valid(raise_exception=True)

        username = seria.validated_data.get('username')
        password = seria.validated_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                token = Token.objects.get_or_create(user=user)[0].key

                data = {
                    'message': 'user has logged in successfuly',
                    'email': user.email,
                    'username': user.username,
                }

                res = LoginSerializer(user).data
                return Response(res, status=status.HTTP_200_OK)
            else:

                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        return JsonResponse(UserSerializer(user).data)


class LogoutView(GenericViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class =  LogoutSerializer

    # Logout Ressource

    @swagger_auto_schema(
        operation_description='Calls Django logout method and delete the Token object assigned to the current User object.')
    @action(methods=["POST"], detail=False)
    def post(self, request, format=None):
        user = request.user.username
        request.user.auth_token.delete()
        #        Simple Call on /logout in post. No arguments
        logout(request)

        return Response({'deconnecter': f'bye bye {user}'}, status=status.HTTP_200_OK)


class SetPassword(GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = SetpassSerializers
    
    # Logout Ressource

    @swagger_auto_schema(
        operation_description='Calls Django password reset  method and change the password.')
    @action(methods=["POST"], detail=False)
    def post(self, request, format=None):
        user = request.user.username
        print(user)
        seria = SetpassSerializers(data=self.request.data)
        seria.is_valid(raise_exception=True)

        old_password = seria.validated_data.get('old_password')
        newpassword = seria.validated_data.get('newpassword')

        user = authenticate(username=user, password=old_password)
        if user is not None:
            user.set_password(newpassword)
            user.save()
            login(request,user)
            return Response({'password': f'password has change'}, status=status.HTTP_200_OK)

        return Response({'password': f'password does\'nt match'}, status=status.HTTP_400_BAD_REQUEST)

        #        Simple Call on /logout in post. No arguments


class FormationViewset(RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                    UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """
    

    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
    permission_classes = [IsAuthenticated, ]


class JobViewset(RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                    UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, ]



class ExperienceViewset(RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                    UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """


    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated, ]


class ProfilUserViewset(RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                    UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """

    queryset = ProfilUser.objects.all()
    serializer_class = ProfilUserSerializer
    permission_classes = [IsAuthenticated, ]


class CompetenceViewset(RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                    UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """


    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = [IsAuthenticated, ]



class MetierViewset(RetrieveModelMixin, CreateModelMixin, ListModelMixin,
                    UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Description: Model Description
    """
    

    queryset = Metier.objects.all()
    serializer_class = MetierSerializer
    permission_classes = [IsAuthenticated, ]