from trainings.use_cases import request_objects as ro

def test_build_training_list_request_object_without_parameters():
    req = ro.TrainingListRequestObject()

    assert bool(req) is True


def test_build_file_list_request_object_from_emtpy_dict():
    req = ro.TrainingListRequestObject.from_dict({})

    assert bool(req) is True