class SerializerActionViewSetMixin:
    """
    Mixin class for Django Rest Framework viewsets that allows
    to specify different serializer classes for different actions
    (e.g., list, create, update, etc.) in the viewset.
    """
    serializer_action_classes = {}
    default_serializer_class = None

    def get_serializer_class(self):
        action = self.action
        try:
            return self.serializer_action_classes[action]
        except KeyError:
            if self.default_serializer_class is not None:
                return self.default_serializer_class
            raise KeyError(f'Invalid action "{action}"')
