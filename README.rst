KeyCut
======

KeyCut (for keyboard shortcut) is a command line tool
that helps you remembering ALL the numerous keyboard shortcuts
of ALL your favorite programs, both graphical and command line ones.

Memo
----

 * Different notation of keyboard keys between vim, emacs, windows, mac, ...
 * All strings (actions and tags) are copied into translation files
 * YAML files notation:
   * app.yml
   * app-version.yml
   * app-custom.yml
   * app-custom-version.yml

   app and custom cannot contains hyphens (-),  
   version can contain any character.
 * Syntax of a YAML file:

```yaml
---
# with explicit values
action: Cut the current line
keys: [dd]
active: true
default: true
hotkey: false
binding: false
sacred: false
---
# active and default are true by default
# all the other are false by default
action: Paste the current buffer
keys: [p]
---
action: Copy the current line
keys: [yy]
```

 * Extra commands:
   * `inherits`: `app[-custom][-version]`  
     This file will then inherit from the specified file.
   * `inherits`: `true` or `false` (YAML also supports `on` and `off`)  
     KeyCut will then try to use the previous version
     of the given app[-custom].yml using Semantic Versioning.
