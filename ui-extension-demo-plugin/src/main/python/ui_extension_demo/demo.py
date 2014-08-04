##################################################################################
# Jython script that is invoked when the respective REST endpoint specified in
# xl-rest-endpoint.xml is invoked.
# Standard XL Deploy services (repositoryService, deploymentService, 
# securityService etc.) are present in the context here. For more details on injected
# services, refer to server-extension api section on http://doc.xebialabs.com/
###################################################################################

from ui_extension_demo.modules.repo import RepositoryHelper

repository_helper = RepositoryHelper(repositoryService)
ci_ids = repository_helper.get_all_infrastucture_cis()

response.entity = map(lambda ci_id: repositoryService.read(ci_id.id), ci_ids)

