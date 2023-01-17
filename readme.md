This shares the projfiles.py project for tracking file and folder locations within a Python project.

The project contains an example folder structure for a project with the projfiles.py library folder in its **example_scripts** subfolder.  Any additional code for the project would be placed in **airia_scripts**. Data (permanent and refreshed) go in **example_data**.  The folders contain the **Pytest** tests file for **projfiles.py**. As it would in a Python project, **tests_projfiles.py** resides in the scripts/tests (aka **example_scripts/tests**) subfolder in the project structure

__An example project's folder structure__</br>
```
{
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
}
```

Investigational analyses can be placed in subfolders in **example_cases_studies** and can reference **example_data** to have access to the project's latest data. In a multi-investigator environment, a good naming convention for the case study folder is **yyyy_mmdd_username or initials_short description of investigation**. This allows folders to be easily filtered by.

J.D. Landgrebe,
Data-Delve Engineer LLC
