from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    """Custom limit/offset pagination style."""
    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'limit': self.limit,
                'offset': self.offset,
                'count': self.count,
            },
            'results': data,
        })
