from trainings.shared import response_object as ro

class TrainingListUseCase(object):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object):
        trainings = self.repo.list()
        return ro.ResponseSuccess(trainings)
