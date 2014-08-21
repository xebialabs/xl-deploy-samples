# Example plugin for rules.

This plugin is a dummy plugin that shows off various features for rule based planning. The Plugin defines some dummy types and some dummy rules that create a dummy deployment plan.

The code for this example plugin is also used by the Rules Tutorial. The Rules Tutorial is bundled with the standard XL Deploy documentation.

## Usage

To use the example please do the following.

You can either copy the contents from `src` to your XL Deploy `ext` folder.

Or you can build a jar file with Gradle. To do so:

1. At a command prompt, navigate to the root folder of the sample.
2. Execute the Gradle command `gradle clean build`. This creates the file `./build/libs/rules-demo-*-plugin.jar`.
3. Copy `rules-demo-*-plugin.jar` to `XLDEPLOY_SERVER_HOME/plugins`.

## Contents

Here is a brief description of what some of the contained files do:

* `src\synthetic.xml` defines all the types used by this plugin.
* `src\xl-rules.xml` defines all the rules for the plugin. This file refers to other scripts and templates.

## Example package (optional)

The `example-package` folder contains an example application that can be used with the rules demo plugin. You can copy the folder to `importablePackages` to import it with XL Deploy.
