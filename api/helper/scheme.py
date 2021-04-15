from collections import OrderedDict
from pymongo.errors import CollectionInvalid

class Scheme():
    @classmethod
    def createTable(cls, data_schema, db, collection):
        validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
        required = []

        for field_key in data_schema:
            field = data_schema[field_key]
            properties = {'bsonType': field['type']}
            minimum = field.get('minlength')

            if type(minimum) == int:
                properties['minimum'] = minimum

            if field.get('required') is True: required.append(field_key)

            validator['$jsonSchema']['properties'][field_key] = properties

        if len(required) > 0:
            validator['$jsonSchema']['required'] = required

        query = [('collMod', collection),
                ('validator', validator)]

        try:
            db.create_collection(collection)
        except CollectionInvalid:
            pass

        command_result = db.command(OrderedDict(query))

        return command_result