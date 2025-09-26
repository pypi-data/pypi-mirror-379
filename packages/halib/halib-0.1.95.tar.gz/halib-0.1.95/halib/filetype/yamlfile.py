import time
import networkx as nx
from rich import inspect
from rich.pretty import pprint
from omegaconf import OmegaConf
from rich.console import Console
from argparse import ArgumentParser

from ..research.mics import *

console = Console()


def _load_yaml_recursively(
    yaml_file, yaml_files=[], share_nx_graph=nx.DiGraph(), log_info=False
):
    conf = OmegaConf.load(yaml_file)
    yaml_files.append(yaml_file)
    if "__base__" in conf:
        parent = conf["__base__"]
        if isinstance(parent, str):
            parent = [parent]
        for p in parent:
            edge = (yaml_file, p)
            share_nx_graph.add_edge(*edge)
            for cycle in nx.simple_cycles(share_nx_graph):
                assert False, f"Cyclic dependency detected: {cycle}"
            # update conf with parent; BY loading parent and merging with conf (the child)
            conf = OmegaConf.merge(
                _load_yaml_recursively(p, yaml_files, share_nx_graph), conf
            )
    if log_info:
        console.rule()
        console.print(f"current yaml_file: {yaml_file}")
        inspect(yaml_files)
        pprint(OmegaConf.to_container(conf, resolve=True))
        time.sleep(1)
    return conf


def load_yaml(yaml_file, to_dict=False, log_info=False):
    yaml_files = []
    share_nx_graph = nx.DiGraph()
    omgconf = _load_yaml_recursively(
        yaml_file,
        yaml_files=yaml_files,
        share_nx_graph=share_nx_graph,
        log_info=log_info,
    )

    if to_dict:
        return OmegaConf.to_container(omgconf, resolve=True)
    else:
        return omgconf

def load_yaml_with_PC_abbr(
    yaml_file, pc_abbr_to_working_disk=DEFAULT_ABBR_WORKING_DISK
):
    # current PC abbreviation
    pc_abbr = get_PC_abbr_name()

    # current plaftform: windows or linux
    current_platform = platform.system().lower()

    assert pc_abbr in pc_abbr_to_working_disk, f"The is no mapping for {pc_abbr} to <working_disk>"

    # working disk
    working_disk = pc_abbr_to_working_disk.get(pc_abbr)

    # load yaml file
    data_dict = load_yaml(yaml_file=yaml_file, to_dict=True)

    # Normalize paths in the loaded data
    data_dict = normalize_paths(data_dict, working_disk, current_platform)
    return data_dict


def parse_args():
    parser = ArgumentParser(description="desc text")
    parser.add_argument(
        "-cfg", "--cfg", type=str, help="cfg file", default="cfg__default.yaml"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    cfg_file = args.cfg
    cfg = load_yaml(cfg_file, to_dict=True)
    console.rule()
    pprint(cfg)


if __name__ == "__main__":
    main()
