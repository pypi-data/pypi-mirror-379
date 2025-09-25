import ast
from pathlib import Path

prov_names = [
    "csv_dump",
    "fig_dump",
    "json_dump",
    "rst_dump",
]


def iter_ext_paths(body):
    for node in body:
        if isinstance(node, ast.If):
            for pth in iter_ext_paths(node.body):
                yield pth
        elif isinstance(node, ast.Expr):
            if isinstance(node.value, ast.Call):
                if isinstance(node.value.func, ast.Name):
                    for func_name in prov_names:
                        if node.value.func.id == func_name:
                            yield func_name, node.value.lineno


def produce(pth, params):
    """Name of object produced by given script.

    The script need to save object using one of easyprov function.

    Args:
        pth (Path): path of python script
        params (dict): set of arguments passed to script

    Returns:
        (list[Path]): path to objects saved in the script
    """
    if not isinstance(pth, Path):
        pth = Path(pth)

    pt = ast.parse(pth.read_bytes(), str(pth))
    lines = open(pth, "r").readlines()
    for func_name, lineno in iter_ext_paths(pt.body):
        line = lines[lineno - 1].strip()
        assert line.startswith(func_name)
        assert line[-1] == ")"
        args = line[len(func_name) + 1 : -1].split(",")
        if func_name == "csv_dump":
            pth_arg = args[2].strip()
        else:
            pth_arg = args[1].strip()
        pth_fmt = eval(pth_arg, params)
        yield Path(pth_fmt)
