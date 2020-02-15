# Proof of Concept SOAR commandline application.

Soarpy is a Python written (WIP) commandline application which enables a user to create simple pythonfiles and chain them together with (boolean)logic.

This way, playbooks can be created which can be executed upon certain actions, contain predefined logic on how to respond to what events and can be used to automate almost all scripting into a single framework.

#### Current limitations:
- Cannot have the same state twice without overriding the old one.
