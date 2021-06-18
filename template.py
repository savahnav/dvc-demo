import os

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",
    "parameters.yaml",
    ".gitignore",      ##which is not meant to be pushed
    os.path.join("src","_init_.py")    ##ust to read source as the python package
]


for file_ in files:
    with open(file_,"w") as f:
        pass

