#****************************************************************************
#* util.py
#*
#* Copyright 2023-2025 Matthew Ballance and Contributors
#*
#* Licensed under the Apache License, Version 2.0 (the "License"); you may 
#* not use this file except in compliance with the License.  
#* You may obtain a copy of the License at:
#*
#*   http://www.apache.org/licenses/LICENSE-2.0
#*
#* Unless required by applicable law or agreed to in writing, software 
#* distributed under the License is distributed on an "AS IS" BASIS, 
#* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
#* See the License for the specific language governing permissions and 
#* limitations under the License.
#*
#* Created on:
#*     Author: 
#*
#****************************************************************************
import difflib
import os
import yaml
from ..package_loader import PackageLoader
from ..task_data import TaskMarker, TaskMarkerLoc, SeverityE

def loadProjPkgDef(path, listener=None):
    """Locates the project's flow spec and returns the PackageDef"""

    dir = path
    ret = None
    loader = None
    found = False
    while dir != "/" and dir != "" and os.path.isdir(dir):
        for name in ("flow.dv", "flow.yaml", "flow.yml"):
            if os.path.exists(os.path.join(dir, name)):
                with open(os.path.join(dir, name)) as f:
                    data = yaml.load(f, Loader=yaml.FullLoader)
                    if "package" in data.keys():
                        found = True
                        listeners = [listener] if listener is not None else []
                        loader = PackageLoader(marker_listeners=listeners)
                        ret = loader.load(os.path.join(dir, name))
                        break
        if found:
            break
        dir = os.path.dirname(dir)
    
    if not found:
        if listener:
            listener(TaskMarker(
                msg="Failed to find a 'flow.dv' file that defines a package in %s or its parent directories" % path,
                severity=SeverityE.Error))
    
    return loader, ret

