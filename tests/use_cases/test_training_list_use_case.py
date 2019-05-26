import uuid

import pytest
import unittest

from unittest import mock

from trainings.domain.training import Training
from trainings.use_cases import training_use_cases as uc
from trainings.use_cases import request_objects as ro
from trainings.shared import response_object as res

@pytest.fixture
def domain_trainigns():
    training1 = Training(
        code=uuid.uuid4(),
        planing_day='2019-05-01',
        description='wop',
        motivation=5,
        tired=2,
        strong=4
    )

    training2 = Training(
        code=uuid.uuid4(),
        planing_day='2019-05-02',
        description='wop wop',
        motivation=5,
        tired=2,
        strong=3
    )

    training3 = Training(
        code=uuid.uuid4(),
        planing_day='2019-05-03',
        description='pow',
        motivation=4,
        tired=4,
        strong=4
    )

    training4 = Training(
        code=uuid.uuid4(),
        planing_day='2019-05-05',
        description='pow pow',
        motivation=4,
        tired=3,
        strong=3
    )

    return [training1, training2, training3, training4]


def test_trainings_list_without_parameters(domain_trainigns):
    repo = mock.Mock()
    repo.list.return_value = domain_trainigns

    training_list_use_case = uc.TrainingListUseCase(repo)   
    request_object = ro.TrainingListRequestObject.from_dict({})

    response_object = training_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == domain_trainigns

def test_trainings_list_with_filters(domain_trainigns):
    repo = mock.Mock()
    repo.list.return_value = domain_trainigns

    training_list_use_case = uc.TrainingListUseCase(repo)
    qry_filters = {'a': 5}
    request_object = ro.TrainingListRequestObject.from_dict({'filters': qry_filters})

    response_object = training_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_trainigns

def test_trainings_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    trainings_list_use_case = uc.TrainingListUseCase(repo)
    request_object = ro.TrainingListRequestObject.from_dict({})

    response_object = trainings_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_trainings_list_handles_bad_request():
    repo = mock.Mock()

    trainings_list_use_case = uc.TrainingListUseCase(repo)
    request_object = ro.TrainingListRequestObject.from_dict({'filters': 5})

    response_object = trainings_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }