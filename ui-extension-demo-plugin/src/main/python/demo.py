ci_ids = repositoryService.query(None, None, "Infrastructure", None, None, None, 0, -1)

response.entity = map(lambda ci_id: repositoryService.read(ci_id.id), ci_ids)

