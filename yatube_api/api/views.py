from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated)
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

from .permissions import IsOwnerOrReadOnly
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)
from posts.models import Post, Group, User


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """Вьюсет для методов просмотра и создания."""
    pass


class UpdateDeleteViewSet(mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    """Вьюсет для методов изменения и удаления."""
    pass


class PostViewSet(CreateListRetrieveViewSet,
                  UpdateDeleteViewSet):
    """Вьюсет для просмотра, создания, изменения, удаления постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    # pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Метод создания поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Вьюсет для просмотра групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # pagination_class = LimitOffsetPagination


class CommentViewSet(CreateListRetrieveViewSet,
                     UpdateDeleteViewSet):
    """Вьюсет для просмотра, создания, изменения, удаления комментариев."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    # pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """Метод получения определенного комментария."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод создания комментария."""
        serializer.save(author=self.request.user,
                        post=get_object_or_404(
                            Post, pk=self.kwargs.get('post_id')
                        ))


class FollowViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """Вьюсет для просмотра, создания подписки на авторов."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    # pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Метод получения определенного автора."""
        user = get_object_or_404(User, username=self.request.user)
        return user.follower.all()

    def perform_create(self, serializer):
        """Метод создания подписки на автора."""
        serializer.save(user=self.request.user)
