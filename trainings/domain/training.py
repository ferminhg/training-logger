from trainings.shared.domain_model import DomainModel

class Training(object):

    def __init__(self, code, planing_day, description, motivation, tired, strong):
        self.code = code
        self.planing_day = planing_day
        self.description = description
        self.motivation = motivation
        self.tired = tired
        self.strong = strong

    @classmethod
    def from_dict(cls, adict):
        training = Training(
            code=adict['code'],
            planing_day=adict['planing_day'],
            description=adict['description'],
            motivation=adict['motivation'],
            tired=adict['tired'],
            strong=adict['strong']
        )

        return training

    def to_dict(self):
        return {
            'code': self.code,
            'planing_day': self.planing_day,
            'description': self.description,
            'motivation': self.motivation,
            'tired': self.tired,
            'strong': self.strong,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

# DomainModel.register(Training)
