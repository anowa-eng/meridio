def serialize_object(obj):
    fields = obj.__class__._meta.fields.keys()
    serialized_dict = {}
    for field in fields:
        serialized_dict[field] = getattr(obj, field)
    return serialized_dict
        