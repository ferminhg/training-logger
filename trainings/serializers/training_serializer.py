import json

class TrainingEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'code': str(o.code),
                'planing_day': str(o.planing_day),
                'description': str(o.description),
                'motivation': int(o.motivation),
                'tired': int(o.tired),
                'strong': int(o.strong),
            }
            return to_serialize
        except AttributeError:
            return super().default(0)