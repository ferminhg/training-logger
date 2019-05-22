import datetime
import json
import uuid

import unittest
import pytest

from trainings.serializers import training_serializer as ts
from trainings.domain.training import Training

class TestTraininSerializa(unittest.TestCase):

    def test_serialize_domain_training(self):
        code = uuid.uuid4()

        training = Training(
            code=code, 
            planing_day='', 
            description='',
            motivation=0,
            tired=0, 
            strong=0
        )

        expected_json = """
            {{
                "code": "{}",
                "planing_day": "",
                "description": "",
                "motivation": 0,
                "tired": 0,
                "strong": 0
            }}
        """.format(code)

        json_training = json.dumps(training, cls=ts.TrainingEncoder)
        assert json.loads(json_training) == json.loads(expected_json)

    def test_serialize_domain_training_wrong_type(self):
        with pytest.raises(TypeError):
            json.dumps(datetime.datetime.now(), cls=ts.TrainingEncoder)
