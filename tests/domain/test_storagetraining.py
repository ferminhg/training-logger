import uuid
import datetime
import unittest

from trainings.domain.training import Training

class TestTrainins(unittest.TestCase):

    def test_storagetraining_model_init(self):
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

    def test_storagetraining_model_from_dict(self):
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