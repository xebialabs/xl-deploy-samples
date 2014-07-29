##################################################################################
# Jython script that is invoked when the respective REST endpoint specified in
# xl-rest-endpoint.xml is invoked.
# Standard XL Deploy services (repositoryService, deploymentService, 
# securityService etc.) are present in the context here. For more details on injected
# services, refer to server-extension api section on http://doc.xebialabs.com/
###################################################################################

ci_ids = repositoryService.query(None, None, "Infrastructure", None, None, None, 0, -1)

response.entity = map(lambda ci_id: repositoryService.read(ci_id.id), ci_ids)

