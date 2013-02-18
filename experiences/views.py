# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions

from .serializers import ExperienceSerializer, ChapterDetailSerializer
from .models import Experience, Chapter
from .permissions import ExperienceIsOwnerOrReadOnly, ChapterIsOwnerOrReadOnly


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'experiences': reverse('experience-list', request=request, format=format),
    })


class ExperienceList(generics.ListCreateAPIView):
    model = Experience
    paginate_by = 30
    serializer_class = ExperienceSerializer

    def pre_save(self, obj):
        obj.user = self.request.user


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Experience
    serializer_class = ExperienceSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, ExperienceIsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.user = self.request.user


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Chapter
    serializer_class = ChapterDetailSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, ChapterIsOwnerOrReadOnly)
