# wbx

A Weight & Biases extension to fetch runs for further analysis.

## Installation

```bash
pip install wbx
```

## Usage

Get projects first

```python
import wandb
from wbx import WBX


api = wandb.Api()
entity = "you-entity"

wbx = WBX(api, entity)
projects = wbx.list_projects(quick_see=True, max_val=10)
```

Then get runs from a specific project

```python
project_name = "your-project-name"
wbx.list_configs(project_name)  # list all configs from runs in the project (for further filtering useless configs)

config_to_use = ["config1", "config2"]

runs_df = wbx.get_runs(
    project_name,
    group_keys=config_to_use,
    summary_keys=None,
    json_encode_non_scalars=False
)
```

After that, you can do analysis based on the `runs_df` DataFrame.

Or you can save it as a `parquet` file for later use.

```python
wbx.to_parquet(runs_df, path="path/to/your/folder")
```

## Contributing

Feel free to submit issues or pull requests.

## License

MIT License. See `LICENSE` file for details.
