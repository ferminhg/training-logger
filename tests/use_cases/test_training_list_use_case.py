import uuid

import pytest
import unittest

from unittest import mock

from trainings.domain.training import Training
from trainings.use_cases import training_use_cases as uc


@pytest.fixture
def domain_traingins():
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


def test_traingin_list_without_parameters(domain_traingins):
    repo = mock.Mock()
    repo.list.return_value = domain_traingins

    training_list_use_case = uc.TrainingListUseCase(repo)
    result = training_list_use_case.execute()

    repo.list.assert_called_with()
    assert result == domain_traingins

    