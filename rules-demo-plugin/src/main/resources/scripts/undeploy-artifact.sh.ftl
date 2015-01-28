echo "Undeploying ${previousDeployed.file.name} on Unix"
rm ${previousDeployed.container.home + "/context/" + previousDeployed.file.name}
echo "Done"
