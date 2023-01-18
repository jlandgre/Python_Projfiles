This shares the **projfiles.py** code base for tracking file and folder locations within a Python project. In consulting work, this has worked well for modeling tools and data used by multiple users and where users conduct analysis case studies that need to reference project data that is refreshed/updated on an ongoing basis.  **projfiles** and use of a standard, predictable folder structure make it possible for the case studies to always access the latest data without making unecessary copies.

The Github project contains an example folder structure for a project with the projfiles.py library folder in its **example_scripts** subfolder.  "example" is a generic prefix that would be customized to a project-specific string. Any additional code for the project would also be placed in **example_scripts**. Data (permanent and refreshed) go in **example_data**.  The folders contain the **Pytest** tests file for **projfiles.py**. As it would in a Python project, **tests_projfiles.py** resides in the scripts/tests (aka **example_scripts/tests**) subfolder in the project structure. The Github project also contains the **test_projfiles.py** Pytest testing to validate **projfiles.py**.

__An example project's folder structure__</br>
```
├── Example_Project_With_ProjFiles_Code
│   ├── example_case_studies
│   ├── example_data
│   ├── example_documentation
│   └── example_scripts
│       ├── jupyter_notebooks
│       ├── projfiles
│       │   └── projfiles.py
│       └── tests
│           └── test_projfiles.py
```

Investigational analyses can be placed in subfolders in **example_cases_studies**. By importing **projfiles**, these can seamlessly reference files in **example_data** to have access to the project's latest data. In a multi-investigator environment, a good naming convention for the case study folders is **yyyy_mmdd_username or initials_short description of investigation**. This allows folders to collaboratively contain all investigators' case studies while being easily filterable by date and/or user in either Microsoft Windows Explorer or Mac OSX.

J.D. Landgrebe,
Data-Delve Engineer LLC
