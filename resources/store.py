from flask_restful import Resource
from models.store_model import StoreModal

class Store(Resource):
    def get(self, name):
        store = StoreModal.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModal.find_by_name(name):
            return {"message": "A store with name '{}' had already exists.".format(name)}, 400
        
        store = StoreModal(name)
        try:
            store.save_to_db()
        except:
            return {"message" : "An error occured while creating the store."}, 500

    def delete(self, name):
        store = StoreModal.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {"message": "Store deleted"}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModal.query.all()]}