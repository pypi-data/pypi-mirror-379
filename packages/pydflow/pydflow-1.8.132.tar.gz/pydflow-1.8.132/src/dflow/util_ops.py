from . import __path__
from .common import S3Artifact, jsonpickle
from .config import config
from .io import (InputArtifact, InputParameter, Inputs, OutputArtifact,
                 OutputParameter)
from .op_template import PythonScriptOPTemplate, ShellOPTemplate


class InitArtifactForSlices(PythonScriptOPTemplate):
    def __init__(self, template, image, command, image_pull_policy, key,
                 sliced_output_artifact=None, sliced_input_artifact=None,
                 sum_var=None, concat_var=None, auto_loop_artifacts=None,
                 group_size=None, format=None, post_script="",
                 tmp_root="/tmp"):
        name = template.name
        super().__init__(name="%s-init-artifact" % name, image=image,
                         command=command, image_pull_policy=image_pull_policy)
        self.origin = template
        self.key = key
        self.sliced_output_artifact = sliced_output_artifact \
            if sliced_output_artifact is not None else []
        self.sliced_input_artifact = sliced_input_artifact \
            if sliced_input_artifact is not None else []
        self.sum_var = sum_var
        self.concat_var = concat_var
        self.auto_loop_artifacts = auto_loop_artifacts
        self.template = template
        self.group_size = group_size
        self.format = format
        self.post_script = post_script
        self.tmp_root = tmp_root

        if self.key is not None:
            self.inputs.parameters["dflow_group_key"] = InputParameter()
            # For the case of reusing sliced steps, ensure that the output
            # artifacts are reused
            for name in self.sliced_output_artifact:
                self.outputs.artifacts[name] = OutputArtifact(
                    path="%s/outputs/artifacts/%s" % (self.tmp_root, name),
                    save=S3Artifact(key="{{workflow.name}}/{{inputs."
                                    "parameters.dflow_group_key}}/%s" % name),
                    archive=None)
            self.outputs.parameters["dflow_artifact_key"] = OutputParameter(
                value="{{workflow.name}}/"
                "{{inputs.parameters.dflow_group_key}}")
        else:
            self.outputs.parameters["dflow_artifact_key"] = OutputParameter(
                value="{{workflow.name}}/{{pod.name}}")
            for name in self.sliced_output_artifact:
                self.outputs.artifacts[name] = OutputArtifact(
                    path="%s/outputs/artifacts/%s" % (self.tmp_root, name),
                    save=S3Artifact(key="{{workflow.name}}/{{pod.name}}/%s"
                                    % name),
                    archive=None)

        if self.sliced_input_artifact:
            if self.key is not None:
                self.inputs.parameters["dflow_key"] = InputParameter()
                if config["save_keys_in_global_outputs"]:
                    self.outputs.parameters["dflow_global"] = OutputParameter(
                        value="{{pod.name}}",
                        global_name="{{inputs.parameters.dflow_key}}",
                    )
            if group_size is not None:
                for name in self.sliced_input_artifact:
                    self.inputs.artifacts[name] = InputArtifact(
                        path="%s/inputs/artifacts/%s" % (self.tmp_root, name),
                        optional=True)
                    self.outputs.artifacts[name] = OutputArtifact(
                        path="%s/outputs/artifacts/%s" % (self.tmp_root, name),
                        archive=None, optional=True)
                self.outputs.parameters["dflow_ngroups"] = OutputParameter(
                    value_from_path="%s/outputs/parameters/dflow_ngroups"
                    % self.tmp_root, type=int)
            else:
                for name in self.sliced_input_artifact:
                    self.inputs.artifacts[name] = InputArtifact(
                        path="%s/inputs/artifacts/%s" % (self.tmp_root, name),
                        optional=True, sub_path=config["catalog_dir_name"])
                    self.outputs.parameters["dflow_slices_path"] = \
                        OutputParameter(
                            value_from_path="%s/outputs/parameters/dflow_"
                            "slices_path" % self.tmp_root, type=dict)

        if self.sum_var is not None:
            name = self.sum_var.name
            self.inputs.parameters[name] = InputParameter()
            self.outputs.parameters["sum_%s" % name] = OutputParameter(
                value_from_path="%s/outputs/parameters/sum_%s" %
                (self.tmp_root, name), type=int)

        if self.concat_var is not None:
            name = self.concat_var.name
            self.inputs.parameters[name] = InputParameter()
            self.outputs.parameters["concat_%s" % name] = OutputParameter(
                value_from_path="%s/outputs/parameters/concat_%s" %
                (self.tmp_root, name), type=list)

        if self.auto_loop_artifacts:
            python_packages = []
            python_packages += __path__
            python_packages += jsonpickle.__path__
            self.python_packages = set(python_packages)
            self.inputs.artifacts["dflow_python_packages"] = InputArtifact(
                path="%s/inputs/artifacts/dflow_python_packages"
                % self.tmp_root)
            for name in self.origin.inputs.artifacts:
                if name in self.auto_loop_artifacts or (name.startswith(
                        "dflow_") and name[6:name.rfind("_")] in
                        self.auto_loop_artifacts):
                    self.inputs.artifacts[name] = InputArtifact(
                        path="%s/inputs/artifacts/%s" % (self.tmp_root, name),
                        optional=True)
            self.outputs.parameters["dflow_nslices"] = OutputParameter(
                value_from_path="%s/outputs/parameters/dflow_nslices" %
                self.tmp_root, type=int)

        self.render_script()

    def render_script(self):
        script = "import os, json\n"
        for name in self.sliced_output_artifact:
            script += "os.makedirs(r'%s/outputs/artifacts/%s/%s', "\
                "exist_ok=True)\n" % (self.tmp_root, name,
                                      config["catalog_dir_name"])
            script += "with open(r'%s/outputs/artifacts/%s/%s/init',"\
                " 'w') as f:\n" % (self.tmp_root, name,
                                   config["catalog_dir_name"])
            script += "    json.dump({'path_list': []}, f)\n"

        if self.sliced_input_artifact:
            required = []
            for i, name in enumerate(self.sliced_input_artifact):
                script += "path_list_%s = []\n" % i
                if self.group_size is not None:
                    script += "path = r'%s/inputs/artifacts/%s/%s'\n" % \
                        (self.tmp_root, name, config["catalog_dir_name"])
                else:
                    script += "path = r'%s/inputs/artifacts/%s'\n" % \
                        (self.tmp_root, name)
                script += "if os.path.exists(path):\n"
                script += "    for f in os.listdir(path):\n"
                script += "        with open(os.path.join(path, f), 'r')"\
                    " as fd:\n"
                script += "            for i in json.load(fd)['path_list']:\n"
                script += "                if i not in path_list_%s:\n" % i
                script += "                    path_list_%s.append(i)\n" % i
                script += "path_list_%s.sort(key=lambda x: x['order'])\n" \
                    % i
                if not self.origin.inputs.artifacts[name].optional:
                    required.append(i)

            if len(required) > 1:
                script += "assert " + " == ".join(
                    ["len(path_list_%s)" % i for i in required]) + "\n"

            if self.group_size is not None:
                script += "import math, shutil\n"
                script += "nslices = len(path_list_%s)\n" % required[0]
                script += "ngroups = math.ceil(nslices/%s)\n" % self.group_size
                if self.template.slices.shuffle:
                    script += "import random\n"
                    script += "random.seed(%s)\n" % \
                        self.template.slices.random_seed
                    script += "shuffled = list(range(nslices))\n"
                    script += "random.shuffle(shuffled)\n"
                    script += "random.seed()\n"  # unset seed
                script += "for i in range(ngroups):\n"
                for i, name in enumerate(self.sliced_input_artifact):
                    script += "    if not path_list_%s:\n" % i
                    script += "        continue\n"
                    script += "    group_dir = r'%s/outputs/artifacts/%s/"\
                        "group_' + ('%s' %% i)\n" % (
                            self.tmp_root, name, self.format or "%d")
                    script += "    os.makedirs(group_dir, exist_ok=True)\n"
                    if self.template.slices.shuffle:
                        script += "    path_list = [path_list_%s[j] for j in "\
                            "shuffled[%s*i:%s*(i+1)]]\n" % (
                                i, self.group_size, self.group_size)
                    else:
                        script += "    path_list = path_list_%s[%s*i:%s*(i+1)"\
                            "]\n" % (i, self.group_size, self.group_size)
                    script += "    for item in path_list:\n"
                    script += "        src = r'%s/inputs/artifacts/%s/'+item"\
                        "['dflow_list_item']\n" % (self.tmp_root, name)
                    script += "        dst = group_dir+'/'+item['dflow_list"\
                        "_item']\n"
                    script += "        os.makedirs(os.path.dirname(dst),"\
                        " exist_ok=True)\n"
                    script += "        if os.path.isfile(src):\n"
                    script += "            shutil.copy(src, dst)\n"
                    script += "        elif os.path.isdir(src):\n"
                    script += "            shutil.copytree(src, dst)\n"
                    script += "    cat = os.path.join(group_dir, '%s')\n" % \
                        config["catalog_dir_name"]
                    script += "    os.makedirs(cat, exist_ok=True)\n"
                    script += "    with open(os.path.join(cat, 'catalog'), "\
                        "'w') as f:\n"
                    script += "        json.dump({'path_list': path_list}, f)"\
                        "\n"
                script += "os.makedirs(r'%s/outputs/parameters', exist_ok="\
                    "True)\n" % self.tmp_root
                script += "with open(r'%s/outputs/parameters/dflow_ngroups'"\
                    ", 'w') as f:\n" % self.tmp_root
                script += "    f.write(str(ngroups))\n"
            else:
                script += "slices_path = []\n"
                script += "for i in range(len(path_list_%s)):\n" % required[0]
                if self.format:
                    script += "    item = {'order': '%s' %% i}\n" % self.format
                else:
                    script += "    item = {'order': i}\n"
                for i, name in enumerate(self.sliced_input_artifact):
                    script += "    item['%s'] = path_list_%s[i]"\
                        "['dflow_list_item'] if path_list_%s else None\n" % (
                            name, i, i)
                script += "    slices_path.append(item)\n"
                script += "os.makedirs(r'%s/outputs/parameters', exist_ok="\
                    "True)\n" % self.tmp_root
                script += "with open(r'%s/outputs/parameters/dflow_slices_"\
                    "path', 'w') as f:\n" % self.tmp_root
                script += "    json.dump(slices_path, f)\n"

        if self.sum_var is not None:
            name = self.sum_var.name
            script += """value = r'{{inputs.parameters.%s}}'
if "dflow_list_item" in value:
    dflow_list = []
    for item in json.loads(value):
        dflow_list += json.loads(item)
    var = list(map(lambda x: x['dflow_list_item'], dflow_list))
else:
    var = json.loads(value)
os.makedirs(r'%s/outputs/parameters', exist_ok=True)
with open(r'%s/outputs/parameters/sum_%s', 'w') as f:
    f.write(str(sum(map(int, var))))\n""" % (
                name, self.tmp_root, self.tmp_root, name)

        if self.concat_var is not None:
            name = self.concat_var.name
            script += """value = r'{{inputs.parameters.%s}}'
var = []
if "dflow_list_item" in value:
    for item in json.loads(value):
        for i in json.loads(item):
            var += i['dflow_list_item']
else:
    for item in json.loads(value):
        if isinstance(item, str):
            var += json.loads(item)
        else:
            var += item
os.makedirs(r'%s/outputs/parameters', exist_ok=True)
with open(r'%s/outputs/parameters/concat_%s', 'w') as f:
    f.write(json.dumps(var))\n""" % (
                name, self.tmp_root, self.tmp_root, name)

        if self.auto_loop_artifacts:
            from .python.python_op_template import handle_packages_script
            script += handle_packages_script(
                "%s/inputs/artifacts/dflow_python_packages" % self.tmp_root)
            script += "from dflow.python import Artifact\n"
            script += "from dflow.python.utils import handle_input_artifact\n"
            script += "from pathlib import Path\n"
            script += "from typing import List\n"
            script += "input = {}\n"
            required = []
            for name in self.auto_loop_artifacts:
                script += "input['%s'] = handle_input_artifact('%s', "\
                    "Artifact(List[Path]), None, r'%s', None, n_parts=%s, "\
                    "keys_of_parts=%s, prefix=%s)\n" % (
                        name, name, self.tmp_root,
                        self.origin.n_parts.get(name, None),
                        self.origin.keys_of_parts.get(name, None),
                        self.origin.input_artifact_prefix.get(name, None))
                if not self.origin.input_sign[name].optional:
                    required.append(name)

            if len(required) > 1:
                script += "assert " + " == ".join(
                    ["len(input['%s'])" % name for name in required]) + "\n"

            script += "os.makedirs(r'%s/outputs/parameters', "\
                "exist_ok=True)\n" % self.tmp_root
            script += "with open(r'%s/outputs/parameters/dflow_nslices', 'w')"\
                " as f:\n" % self.tmp_root
            script += "    f.write(str(len(input['%s'])))\n" % required[0]

        script += self.post_script.format(**{"tmp_root": self.tmp_root})
        self.script = script


class CheckNumSuccess(ShellOPTemplate):
    def __init__(self, name="check-num-success", image=None,
                 image_pull_policy=None):
        super().__init__(name=name, image=image,
                         image_pull_policy=image_pull_policy)
        self.command = ["python3"]
        self.script = "import json\n"
        self.script += "succ = '''{{inputs.parameters.success}}'''\n"
        self.script += "try:\n"
        self.script += "    succ = sum([int(i) for i in json.loads(succ)])\n"
        self.script += "except:\n"
        self.script += "    succ = 0\n"
        self.script += "print('Num success: ' + str(succ))\n"
        self.script += "print('Threshold: {{inputs.parameters.threshold}}')\n"
        self.script += "assert succ >= {{inputs.parameters.threshold}}\n"
        self.inputs = Inputs(
            parameters={"success": InputParameter(),
                        "threshold": InputParameter()})


class CheckSuccessRatio(ShellOPTemplate):
    def __init__(self, name="check-success-ratio", image=None,
                 image_pull_policy=None):
        super().__init__(name=name, image=image,
                         image_pull_policy=image_pull_policy)
        self.command = ["python3"]
        self.script = "import json\n"
        self.script += "succ = '''{{inputs.parameters.success}}'''\n"
        self.script += "try:\n"
        self.script += "    succ = sum([int(i) for i in json.loads(succ)])\n"
        self.script += "except:\n"
        self.script += "    succ = 0\n"
        self.script += "threshold = {{inputs.parameters.threshold}} * "\
            "{{inputs.parameters.total}}\n"
        self.script += "print('Num success: ' + str(succ))\n"
        self.script += "print('Threshold: ' + str(threshold))\n"
        self.script += "assert succ >= threshold\n"
        self.inputs = Inputs(
            parameters={"success": InputParameter(),
                        "total": InputParameter(),
                        "threshold": InputParameter()})
