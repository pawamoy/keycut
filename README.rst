KeyCut
======

KeyCut (for keyboard shortcut) is a command line tool
that helps you remembering ALL the numerous keyboard shortcuts
of ALL your favorite programs, both graphical and command line ones.

Memo
----

1. Different notation of keyboard keys between vim, emacs, windows, mac, ...
2. All strings (actions and tags) are copied into translation files
3. YAML files notation:
  * app.yml
  * app-version.yml
  * app-custom.yml
  * app-custom-version.yml

   app and custom cannot contains hyphens (-),  
   version can contain any character.
4. Syntax of a YAML file: take a look at YAML files in data folder
5. Extra commands:
  * `inherits`: `app[-custom][-version]`  
     This file will inherit from the specified file.
  * `inherits`: `true` or `false` (YAML also supports `on` and `off`)  
     KeyCut will try to use the previous version
     of the given app[-custom].yml using Semantic Versioning.
