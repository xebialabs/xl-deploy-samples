echo "Undeploying ${previousDeployed.file.name} on Windows"
del ${previousDeployed.container.home + "/context/" + previousDeployed.file.name}
echo "Done"
