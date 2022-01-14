from cx_Freeze import setup, Executable
import os
import shutil
import subprocess

outdir = "dist"
plname = "dev.nadie.dcontrol"
cxout = "exe.win-amd64-3.9"
build_exe_options = {"excludes": ["tkinter", "setuptools", "lib2to3"], "include_msvcr": True, "optimize": 2}

try:
    shutil.rmtree(outdir)
except OSError as e:
    print("Error: %s : %s" % (outdir, e.strerror))

setup(
    name="dev.nadie.dcontrol",
    version="0.1", description="hmm",
    options={"build_exe": build_exe_options},
    executables=[Executable("dev.nadie.dcontrol.py")],
)

os.makedirs(outdir)
os.mkdir(f"{outdir}/{plname}.sdPlugin/")
print("copying files")
shutil.copytree("Plugin_files", f"{outdir}/{plname}.sdPlugin", dirs_exist_ok=True)
print("copying build from cx")
shutil.copytree(f"build/{cxout}", f"{outdir}/{plname}.sdPlugin", dirs_exist_ok=True)
subprocess.run(["sdc.exe", "-b", "-i", f"{plname}.sdPlugin", "-o", "%CD%"], shell=True, cwd="dist")
