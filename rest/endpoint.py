from flask import Blueprint, request, jsonify
from .serialize_model import serialize_object

def jsonify_object(object):
    return jsonify(serialize_object(object))
class Endpoint:
    def __init__(self, model):
        self.model = model
        model_name = str.lower(model.__name__)
        endpoint_name = f'{model_name}_endpoint'
        self.blueprint = Blueprint(endpoint_name, endpoint_name)
        @self.blueprint.route(f'/api/{model_name}/create', methods=['POST'])
        def api_create():
            entity = self.model.create(**request.get_data())
            return jsonify_object(entity)
        @self.blueprint.route(f'/api/{model_name}/<int:model_id>', methods=['GET'])
        def api_get(model_id):
            entity = self.model.get(self.model.id == model_id)
            return jsonify_object(entity)
        @self.blueprint.route(f'/api/{model_name}/update/<int:model_id>', methods=['POST'])
        def api_update(model_id):
            old_entity = self.model.get(self.model.id == model_id)
            new_entity = self.model.update(**serialize_object(old_entity), **request.get_data()).where(self.model.id == model_id).execute()
            return jsonify_object(new_entity)
        @self.blueprint.route(f'/api/{model_name}/delete/<int:model_id>')
        def api_delete(model_id):
            self.model.delete().where(self.model.id == model_id).execute()
            return ''
    @staticmethod
    def register(model):
        if Endpoint.app:
            Endpoint.app.register_blueprint(Endpoint(model).blueprint)
        else:
            raise TypeError('An app was not provided.')
    
