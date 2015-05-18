You must build the sample with Gradle. To do so:

1. At a command prompt, navigate to the root folder of the sample.
2. Execute the Gradle command `gradle clean build`. This creates the file `./build/libs/ui-extension-demo-plugin-*.jar`.
3. Copy `ui-extension-demo-plugin-*.jar` to `XLDEPLOY_SERVER_HOME/plugins`.


This sample is intended to show how to develop an extension UI plugins by means of AngularJS and Jython scripts.


The extension shows the report of all the CIs that are located inside the selected root.

Note that although AngularJS has been used for the frontend, you are free to use any technology involving HTML and JavaScript. For the backend part, you can use the XL Deploy <a hre="http://docs.xebialabs.com/releases/latest/deployit/rest-api/index.html">REST api</a> or can expose and use your custom REST api.

Here is a brief description of what some of the contained files does:

1. **xl-ui-plugin.xml**: is the file where you specify the tabs (top menu items) you want to add in XL Deploy UI. Each tab must be wired-up with some html file via the 'uri' property.

2. **xl-rest-endpoint.xml**: is the file where you declare your custom REST api, backed by a python files. Note that the entered URIs are prepended with '/api/extension'. For example, if you specified '/test/demo' as an REST endpoint, the actual endpoint becomes '/api/extension/test/demo'

3. **web/demo-plugin/demo.html**: The entry point html file that is displayed to a user when he clicks on 'demo' tab

4. **cis.py**: Jython script that is invoked via the rest endpoint /test/cis. Any Jython script invoked through the REST api has access to XL Deploy services like DeploymentService, RepositoryService and so on. For more details about the available services in python context, look at the rest api.

### Related articles

* <a href="https://docs.xebialabs.com/xl-deploy/how-to/writing-jython-scripts-for-xl-deploy.html">Writing Jython scripts for XL Deploy</a>
