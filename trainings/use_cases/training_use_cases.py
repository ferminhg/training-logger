from trainings.shared import response_object as ro

class TrainingListUseCase(object):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object):
        if not request_object:
            return ro.ResponseFailure.build_from_invalid_request_object(request_object)

        try:
            trainings = self.repo.list(filters=request_object.filters)
            return ro.ResponseSuccess(trainings)
        except Exception as exc:
            return ro.ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc)))

