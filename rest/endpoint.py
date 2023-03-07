from flask import Blueprint, request

class Endpoint:
    def __init__(self, model):
        self.model = model
        model_name = model.__name__
        self.blueprint = Blueprint(model_name, import_name)
        @self.blueprint.route(f'/api/{model_name}/<int:model_id>', methods=['GET'])
        def api_create():
            return self.model.create(**request.get_data())
        @self.blueprint.route(f'/api/{model_name}/create', methods=['POST'])
        def api_get(model_id):
            return self.model.get(User.id == model_id)
        @self.blueprint.route(f'/api/{model_name}/update/<int:model_id>', methods=['POST'])
        def api_update(model_id):
            return self.model.update(**request.get_data()).where(User.id == model_id).execute()
        @self.blueprint.route(f'/api/{model_name}/delete/<int:model_id>')
        def api_delete(model_id):
            retrun 
