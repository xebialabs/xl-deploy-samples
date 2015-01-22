echo "Undeploying file on Unix"
rm ${previousDeployed.container.home + "/context/" + previousDeployed.file.name}
echo "Done"
