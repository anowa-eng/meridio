from database import models
model_list = [
    models.User,
    models.UserProfile
]

def serialize_object(obj):
    fields = obj.__class__._meta.fields.keys()
    serialized_dict = {}
    for field in fields:
        value = getattr(obj, field)
        if value.__class__ in model_list:
            serialized_dict[field] = serialize_object(value)
        else:
            serialized_dict[field] = getattr(obj, field)
    return serialized_dict
        