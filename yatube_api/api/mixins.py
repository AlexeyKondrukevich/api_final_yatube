from rest_framework import mixins, viewsets


class GetListCreateViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    pass
