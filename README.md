# lektor-htmlmin

HTML minifier for Lektor that automatically minifies generated .html files. This plugin is based on [htmlmin](https://github.com/mankyd/htmlmin).

## Installation

You can install lektor-htmlmin using Lektor's plugin installer:

```
lektor plugins add lektor-htmlmin
```

Or modifying your lektorproject file, adding the plugin to the packages section:

```
[packages]
lektor-htmlmin = 0.3
```

## Usage

To enable minification, pass the `htmlmin` flag when starting the development server or when running a build:

```
lektor build -O my_build_folder -f htmlmin
```

When the flag is present, htmlmin will overwrite all HTML files in the output directory with their minified counterparts.

*Note:* The htmlmin plugin currently minifies every file in the project after a build.
Not just files that have been changed. This should have no ill effects, but
might increase build times if there are many files to minify.
