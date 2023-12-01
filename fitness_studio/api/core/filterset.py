from django_filters import FilterSet


class FilterSetWithInitial(FilterSet):
    """
    Custom FilterSet that allows setting initial values for each field.

    This FilterSet extends the default behavior by using the 'initial' value as the default
    for each field when the filter is applied. Caution is advised when using initial values
    as defaults.

    Reference: https://django-filter.readthedocs.io/en/stable/guide/tips.html#using-initial-values-as-defaults
    """

    def __init__(self, data=None, *args, **kwargs):
        # if filterset is bound, use initial values as defaults
        if data is not None:
            # get a mutable copy of the QueryDict
            data = data.copy()

            for name, f in self.base_filters.items():
                initial = f.extra.get('initial')

                # filter param is either missing or empty, use initial as default
                if not data.get(name) and initial:
                    data[name] = initial

        super().__init__(data, *args, **kwargs)
