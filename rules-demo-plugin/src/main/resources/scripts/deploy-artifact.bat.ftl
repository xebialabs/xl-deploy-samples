echo "Deploying ${deployed.file} on Windows"
mkdir ${deployed.container.home + "/context"}
copy ${deployed.file.path} ${deployed.container.home + "/context"}
echo "Done"

