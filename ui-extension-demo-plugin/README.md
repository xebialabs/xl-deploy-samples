Build the project:
```
gradle clean build
```

Copy the extension to the plugins folder of your XLD installation:
```
cp ./build/libs/ui-extension-demo-*-plugin.jar ~/my/xld/location/plugins
```
<p>
This sample is intended to show how to develop own extension UI plugins by means of AngularJS and Jython scripts.<br/>
This implementation shows the report of all the CIs that are located inside Infrastructure.<br/>
If you don't have anything there *"Please create some CIs inside Infrastructure folder and click Refresh icon"* message will be shown to you.
</p>