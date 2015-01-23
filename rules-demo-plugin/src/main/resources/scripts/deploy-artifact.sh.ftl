echo "Deploying file on Unix"
mkdir -p ${deployed.container.home + "/context"}
cp ${deployed.file.path} ${deployed.container.home + "/context"}
echo "Done"

