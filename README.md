# lektor-htmlmin

HTML minifier for Lektor that automatically minifies generated .html files. This plugin is based on htmlmin.

## Installation

You can install lektor-htmlmin using Lektor's plugin installer:

```
lektor plugins add lektor-htmlmin
```

Or modifying your lektorproject file, adding the plugin to the packages section:

```
[packages]
lektor-htmlmin = 0.1.1
```

## Usage
lektor-htmlmin will automatically minify .html files in the build destination 
folder, after lektor has finished building them. 
The original files will be overwritten by their minified counterpart.

```
lektor build -O my_build_folder
```

