# Documentation

Documentation is made using [ Sphinx ](https://www.sphinx-doc.org/en/master/), with the aim to be published to [ Read the Docs ](https://readthedocs.org/) when production ready.

## Producing documentation

Documentation can be added to by editing [ source/index.rst ](source/index.rst) for the landing page. Other `.rst` files can be added in the `source/` dir.

## Updating existing docstring documentation

Edit the given docstring within the code then run

```bash
# on windows
make.bat html
# or on linux
make html
```

With errors try,

```bash
make.bat clean
#or
make clean
```

## Adding new docstring documentation

With new modules and docstring documentation this needs to be added to the
track. This is done by

```bash
sphinx-apidoc -o ./source ../build/lib
```

This will document the package build code.

## Further sphinx information

A good tutorial that has been followed can be found [here](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/build-the-docs.html#modifying-the-files-generated-by-sphinx-apidoc).
