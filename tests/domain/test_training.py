import uuid
import datetime
import unittest

from trainings.domain.training import Training

class TestTrainins(unittest.TestCase):

    def test_training_model_init(self):
        code = uuid.uuid4()
        
        training = Training(code, 
                            planing_day='', 
                            description='',
                            motivation=0,
                            tired=0, 
                            strong=0)
        assert training.code == code
        assert training.planing_day == ''
        assert training.description == ''
        assert training.motivation == 0
        assert training.tired == 0
        assert training.strong == 0

    def test_training_model_from_dict(self):
        code = uuid.uuid4()
        
        training = Training.from_dict(
            {
                'code': code,
                'planing_day': '',
                'description': '',
                'motivation': 0,
                'tired': 0,
                'strong': 0,
            }
        )
        assert training.code == code
        assert training.planing_day == ''
        assert training.description == ''
        assert training.motivation == 0
        assert training.tired == 0
        assert training.strong == 0
    
    def test_training_model_to_dict(self):
        traingin_dict = {
            'code': uuid.uuid4(),
            'planing_day': '',
            'description': '',
            'motivation': 0,
            'tired': 0,
            'strong': 0,
        }
        training1 = Training.from_dict(traingin_dict)
        training2 = Training.from_dict(traingin_dict)

        assert training1 == training2
