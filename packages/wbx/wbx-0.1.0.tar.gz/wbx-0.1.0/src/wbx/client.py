import json
import os
from typing import Any, Dict, List, Optional, Union

import pandas as pd
import wandb
from rich import print
from tqdm import tqdm

from .utils import _is_scalar


class WBX:
    def __init__(self, api: wandb.Api, entity: str) -> None:
        self.api = api
        self.entity = entity

    def list_configs(self, project_name: str) -> None:
        runs = self.api.runs(f"{self.entity}/{project_name}")

        try:
            first = next(iter(runs))
        except StopIteration:
            print("[yellow]No runs found.[/yellow]")
            return

        print(first.config)


    def list_projects(self, quick_see: bool = False, max_val: int = 20) -> pd.DataFrame:
        projects = self.api.projects(self.entity)
        rows: List[Dict[str, Any]] = []

        for project in projects:
            rows.append(
                {
                    "name": getattr(project, "name", ""),
                    "created_at": getattr(project, "created_at", ""),
                }
            )

        projects = pd.DataFrame(rows)

        if quick_see:
            print(projects.head(max_val))

        return projects


    def get_runs(
        self,
        project_name: str,
        group_keys: Union[str, List[str]],
        summary_keys: Optional[List[str]] = None,
        json_encode_non_scalars: bool = False,
    ) -> pd.DataFrame:
        runs = self.api.runs(f"{self.entity}/{project_name}")
        rows: List[Dict[str, Any]] = []
        count: int = 0

        if isinstance(group_keys, str):
            group_keys = [group_keys]

        for run in tqdm(runs):
            cfg = getattr(run, "config", {}) or {}
            summ = getattr(run, "summary", {}) or {}
            raw_summary = getattr(summ, "_json_dict", dict(summ)) or {}
            meta = {
                "run_id": getattr(run, "id", ""),
                "name": getattr(run, "name", ""),
                "state": getattr(run, "state", ""),
                "created_at": getattr(run, "created_at", ""),
            }
            filtered_cfg: Dict[str, Any] = {}

            for k in group_keys:
                if k in cfg:
                    v = cfg[k]
                    filtered_cfg[f"cfg.{k}"] = v if _is_scalar(v) else json.dumps(v, ensure_ascii=False)

            filtered_summ: Dict[str, Any] = {}
            items = raw_summary.items()

            if summary_keys is not None:
                items = ((k, raw_summary.get(k, None)) for k in summary_keys)

            for k, v in items:
                if _is_scalar(v):
                    filtered_summ[str(k)] = v
                elif json_encode_non_scalars:
                    filtered_summ[str(k)] = json.dumps(v, ensure_ascii=False)

            if not cfg:
                print(f"[yellow][warn][/yellow] Run {meta['name']} ({meta['run_id']}) has empty config.")
            if not raw_summary:
                print(f"[yellow][warn][/yellow] Run {meta['name']} ({meta['run_id']}) has empty summary.")

            rows.append({**meta, **filtered_cfg, **filtered_summ})
            count += 1

        df = pd.DataFrame(rows)

        return df

    def to_parquet(self, df: pd.DataFrame, folder_path: str, project_name: str) -> None:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)

        df.to_parquet(f"{folder_path}/{project_name}.parquet", index=False, engine="pyarrow")