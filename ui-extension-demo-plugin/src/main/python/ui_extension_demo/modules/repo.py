
class RepositoryHelper:
    
    def __init__(self, repositoryService):
        self._repositoryService = repositoryService

    def get_all_infrastucture_cis(self):
		return self._repositoryService.query(None, None, "Infrastructure", None, None, None, 0, -1)
