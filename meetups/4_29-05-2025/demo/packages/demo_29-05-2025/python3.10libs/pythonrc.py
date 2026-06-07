from pathlib import Path
import inspect
import hou

# set env variables
current_file = Path(inspect.getfile(lambda: None)) # Note: Cannot do Path(__file__) because __file__ attribute does not exist when executed
houdini_package_folder = current_file.parents[1].readlink() # Note: We want the parent to be relative to this dir and not the symlinked folder
package_folder = houdini_package_folder.parents[3]
assets_folder = houdini_package_folder / "assets"
hou.putenv("DEMO_29052025_ASSETS", str(assets_folder))