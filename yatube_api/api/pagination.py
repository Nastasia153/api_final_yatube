from rest_framework.pagination import LimitOffsetPagination


class PostsPagination(LimitOffsetPagination):
    page_size = 10
