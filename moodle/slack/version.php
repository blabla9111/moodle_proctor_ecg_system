<?php
/*  DOCUMENTATION
    .............

    version.php defines the version of your block which allows to make sure your block plugin is compatible with the given
    Moodle site, as well as spotting whether an upgrade is needed.

    defined('MOODLE_INTERNAL') || die();
    It's a basic check if a php file should not be loaded on it's own (class files etc). It is best to use this line in
    every moodle page.

    $plugin enable you to add additional features and functionality to the Moodle core.

    $plugin->version:
    The version number of the plugin. The format is partially date based with the format, YYYYMMDDXX 
    (Year Month Day 24-hr time) where 24-hr time can be from 1 to 99. A new plugin version must have this number increased
    in this file, which is detected by the Moodle core and the upgrade process is triggered.
    ex: plugin->version = 2022122700; // Plugin released on 27th December 2022.

    $plugin->requires:
    Specifies the minimum version number of the Moodle core that your plugin requires. It is only possible to install version
    4.1, unless you have 3.9 or later. Moodle core's version number is defined in the file version.php located in Moodle
    root directory, in the $version variable.
    ex: $plugin->requires = 2019111200; // Moodle 3.8 is required.

    $plugin->component:
    The frankenstyle component name in the form of plugintype_pluginname. It is used during the installation and upgrade
    process for diagnostics and validation purpose to make sure the component is a block or a module or a course or a local
    component.
*/

defined('MOODLE_INTERNAL') || die();

$plugin->version = 2024051213;  // YYYYMMDDHH (Year Month Day 24-hr time).
$plugin->requires = 2022041200; // YYYYMMDDHH (The release version of Moodle 4.1).
$plugin->component = 'block_slack'; // Name of your plugin (used for diagnostics).
