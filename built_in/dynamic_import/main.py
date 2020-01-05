import importlib
from traceback import format_exc
import os
import sys
import re
from shutil import copyfile


INDENT = " " * 4
prefix = "temp_"
module_name = "imported"
temp_module_name = f"{prefix}{module_name}"
module_path = r"C:\Repos\python\built_in\dynamic_import"


def get_exception_line(mname, tb_message):
    regex = r"{0}\.py\", line (\d+), in <module>".format(mname)
    match = re.search(regex, tb_message, re.MULTILINE)
    line = match.group(1)
    return int(line)


def append_try_except_block(mpath, mname, line_num):
    with open(os.path.join(mpath, mname + ".py"), "r") as f:
        file_lines = f.readlines()

    exception_line = file_lines[line_num - 1]
    standard_indention = " " * 4
    current_indention = " " * (len(exception_line) - len(exception_line.lstrip()))
    appended_file_lines = (
        file_lines[: line_num - 1]
        + [current_indention + "try:\n"]
        + [standard_indention + exception_line]
        + [current_indention + "except:\n"]
        + [current_indention + standard_indention + "pass\n"]
        + file_lines[line_num:]
    )
    with open(os.path.join(mpath, mname + ".py"), "w") as f:
        f.writelines(appended_file_lines)


def make_temp_module(module_path, prefix, module_name):
    source = os.path.join(module_path, module_name + ".py")
    destination = os.path.join(module_path, prefix + module_name + ".py")
    copyfile(source, destination)


make_temp_module(module_path, prefix, module_name)

while True:
    try:
        sys.path.append(module_path)
        imp_module = importlib.import_module(temp_module_name)
        print(imp_module.__dict__.keys())
        break
    except Exception as ex:
        tb_message = format_exc()
        ex_line_num = get_exception_line(temp_module_name, tb_message)
        print(ex_line_num)
        append_try_except_block(module_path, temp_module_name, ex_line_num)

