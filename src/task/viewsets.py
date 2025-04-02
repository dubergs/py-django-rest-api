from rest_framework import viewsets, mixins
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .models import Task, TaskList, Attachment
from .permissions import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, IsAllowedToEditAttachmentElseNone

class TaskListViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditTaskListElseNone]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    
    
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAllowedToEditTaskElseNone]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        queryset = super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.profile
        update_queryset = queryset.filter(created_by=user_profile)
        return update_queryset
    
    
class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditAttachmentElseNone]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer