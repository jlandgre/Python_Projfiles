#Version 1/17/23
#python -m pytest test_projfiles.py -v -s
#2345678901234567890123456789012345678901234567890123456789012345678901234567890

#Add libs sub-directory to paths and import custom libraries
import pytest
import sys, os
import inspect
from pathlib import Path

#Global variables for Project Name (e.g. root folder name) and project folder prefix
ProjName = 'Example_Project_With_ProjFiles_Code'
proj_abbrev = 'example'

#Set paths to enable importing projfiles as library
pf_thisfile = inspect.getframeinfo(inspect.currentframe()).filename
path_tests = str(os.path.dirname(os.path.abspath(pf_thisfile)))
path_projfiles = os.sep.join(path_tests.split(os.sep)[0:-1] + ['projfiles', ''])
if not path_projfiles in sys.path: sys.path.append(path_projfiles)
import projfiles

"""
Fixtures for Files and ProjectPaths testing
"""
@pytest.fixture
def files():
    """
    Files Class fixture for testing
    JDL 1/16/23
    """
    return projfiles.Files(proj_abbrev)

@pytest.fixture
def files_IsTest():
    """
    Files Class fixture for testing - IsTest=True
    JDL 1/17/23
    """
    return projfiles.Files(proj_abbrev, IsTest=True, subdir_tests='xxx')

"""
ProjectPaths Class testing
"""
def test_Files_SetAllProjectPaths(files):
    """
    JDL 1/17/23; Modified 4/12/23 after SetGenericProjectPaths added to __init__
    """
    assert files.path_scripts.split(os.sep)[-2] == proj_abbrev + '_scripts'
    assert files.path_tests.split(os.sep)[-2] == 'tests'
    assert files.path_data.split(os.sep)[-2] == proj_abbrev + '_data'
    assert files.path_case_studies.split(os.sep)[-2] == proj_abbrev + '_case_studies'

def test_Files_SetFolderPathsIsTest(files_IsTest):
    """
    JDL 1/16/23; Modified 4/12/23 after SetGenericProjectPaths added to __init__
    """
    sExpected = files_IsTest.path_scripts + 'tests' + os.sep
    assert files_IsTest.path_root == sExpected
    assert files_IsTest.path_data.split(os.sep)[-3] == 'tests'
    assert files_IsTest.path_data.split(os.sep)[-2] == 'xxx'

def test_Files_SetFolderPaths(files):
    """
    JDL 1/16/23; Modified 4/12/23 after SetGenericProjectPaths added to __init__
    """
    assert files.path_scripts.split(os.sep)[-2] == proj_abbrev + '_scripts'
    assert files.path_tests.split(os.sep)[-2] == 'tests'
    assert files.path_data.split(os.sep)[-2] == proj_abbrev + '_data'
    assert files.path_case_studies.split(os.sep)[-2] == proj_abbrev + '_case_studies'

def test_Files_SetPathRoot(files):
    """
    JDL 1/16/23
    """
    assert files.path_root.split(os.sep)[-2] == ProjName

def test_Files_BuildLstPaths(files):
    """
    JDL 1/16/23
    """
    #Build directory string for projfiles.py path + file and then its path
    pf_projfiles = path_projfiles+ 'projfiles.py'
    assert pf_projfiles.split(os.sep)[-1] == 'projfiles.py'
    assert pf_projfiles.split(os.sep)[-3] == proj_abbrev + '_scripts'

    #Check the trailing item in each directory path (last item is '' due to delim at end)
    assert files.lstpaths[2].split(os.sep)[-2] == ProjName
    assert files.lstpaths[1].split(os.sep)[-2] == proj_abbrev + '_scripts'
    assert files.lstpaths[0].split(os.sep)[-2] == 'projfiles'

def test_Files_ClassInstance(files):
    """
    Test that Files class is instanced
    JDL Jan 16, 2023
    """
    assert files.proj_abbrev == proj_abbrev

def test_Files_LocatePaths():
    """
    filename depends on where a *.py is run from.
    With $python tests/test_projfiles.py, filename = tests/test_projfiles.py
    With $cd tests then $python test_projfiles.py, filename = test_projfiles.py

    But os.path.dirname(os.path.abspath(filename)) always returns the 
    directory path for the file being run regardless of where run from
    JDL Jan 16, 2023
    """
    #A robust (for *.py not *.ipynb) way to get the directory for a file being run
    pf_thisfile = inspect.getframeinfo(inspect.currentframe()).filename
    path_tests = str(os.path.dirname(os.path.abspath(pf_thisfile)))
    assert path_tests.split(os.sep)[-1] == 'tests'

    #A robust way to get the filename
    assert str(Path(__file__)).split(os.sep)[-1] == 'test_projfiles.py'

    #parent directory (e.g. proj_scripts folder containing tests)
    path_scripts = os.sep.join(path_tests.split(os.sep)[0:-1])
    assert path_scripts.split(os.sep)[-1] == proj_abbrev + '_scripts'

    #Project home directory
    path_proj_home = os.sep.join(path_tests.split(os.sep)[0:-2])
    assert path_proj_home.split(os.sep)[-1] == ProjName