# Packaged Model Example

This is an example repo containing a dummy microsimulation model, demonstrating:

- how `uv` manages environments/dependencies automatically
- how `uv.lock` (and `.python-version`) ensures everyone has identical environments
- how easy this makes things for the end user (and developer)
- a two-level configuration, using command-line arguments for the high-level and `.toml` files for the detail, of which there can be multiple configurations.


## Requirements

Just one: `uv` is installed on the host system.

## Use cases

### End user

End users do not need dev dependencies or write access to the source code. They can install this package as a uv tool directly from github or from a folder (which may be a remote drive):

```sh
uv tool install git+https://github.com/virgesmith/packaged-model-example.git
```

or

```sh
uv tool install <path-to-repo-on-local-or-remote-drive>
```

and then run the script directly:

```sh
run-example-model --in <input-path> --config <config-path> --out <output-path>
```

### Developer

Clone the package if necessary, then install with:

```sh
uv sync --dev
```

or

```sh
uv sync --group gregwt --dev
```

if using the optional gregwt module, which has extra dependencies

Then run the model using

```sh
uv run run-example-model --in <input-path> --config <config-path> --out <output-path>
```
