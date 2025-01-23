import os
from pathlib import Path # to handle the path setup as it different for the linux("\") and windows("\") operating system

list_of_files =[
    #
    ".github/workflows/.gitkeep",
    # Source Code
    "src/__init__.py",
    # Training pipeline
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    # Prediction pipeline
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    # For utility
    "src/pipeline/utils.py",
    # For logs
    "src/logger/logging.py",
    # For exception
    "src/exception/exception.py",
    # Test case
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    # For setup
    "init_setup.sh",
    # Envrionment Requirement
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

# To Create all these above files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        #logging.info(f"Creating directory: {filedir} for file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
               pass # create an empty file
               
           

