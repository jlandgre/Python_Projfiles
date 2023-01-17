#Version 1/17/23
#J.D. Landgrebe/Data-Delve Engineer LLC
#Covered under MIT Open Source License per 
import inspect
import os

#Set paths to libraries
#PF_thisfile = inspect.getframeinfo(inspect.currentframe()).filename
#path_thisfile = str(os.path.dirname(os.path.abspath(PF_thisfile)))
#path_libs = os.sep.join(path_thisfile.split(os.sep)[0:-1]) + os.sep + 'libs' + os.sep
#if not path_libs in sys.path: sys.path.append(path_libs)

class Files():
    """
    Class for keeping track of project files in standard project folder structure
    
    __init__() Arguments:
      proj_abbrev [String] project prefix string for folder names
      sPFHome [String] name of a Home subdirectory within 
        proj/proj_case_studies folder
      IsTest [Boolean] Toggles between production and testing (IsTest=True).
      sTestsSubdir[String] allows files (related to specific issues) to be placed
        in subfolders within the Proj/proj_scripts/tests subfolder. 
        
        For example, if Issues List issue 42 relates to solving a bug, the folder 
        "tests/issue_042_2023_10_BugFix" subfolder would contain example files 
        recreate the issue along with text or Word doc documentation exlaining 
        the cause of the bug and how it was fixed

    Naming and Case Conventions:
    * lowercase for project-specific attributes except if creates ambiguity; 
      then use underscore to separate words
    * self.path_xxx is a complete directory path with os-specific separator as 
      last character
    * self.pf_xxx is a complete directory path + filename
    * self.f_xxx is a filename with extension
    * self.path_subdir_xxx is a folder name or directory path suffix
    * Camelcase names such as "PFHome" are informational and/or inputs
      to construct folder name strings

    JDL Updated 1/17/23
    """

    def __init__(self, proj_abbrev, PFHome='', IsTest=False, TestsSubdir=''):
        """
        JDL Updated 1/17/23
        """
        self.IsTest = IsTest
        self.TestsSubdir = TestsSubdir
        self.proj_abbrev = proj_abbrev

        #Initialize Class attributes
        self.path_root = '' 
        self.path_scripts = ''
        self.path_tests = ''
        self.path_data = ''
        self.path_case_studies = ''
        self.path_home = ''
        self.path_subdir_tests = ''
        self.path_subdir_home = ''
        self.lstpaths = []

        #Optional Case Study "Home" directory (subfolder in proj/proj_case_studies)
        if len(PFHome) > 0: self.path_subdir_home = PFHome

        #Optional subdirectory within tests folder - to contain issue-specific files
        if IsTest: self.path_subdir_tests = TestsSubdir

    def SetAllProjectPaths(self):  
        """
        Set strings for project-specific files and paths
        """
        #Instance Project Paths and set top-level folder names and paths
        self.BuildLstPaths(iLevel=3)
        self.SetPathRoot()
        self.SetFolderPaths()

        #Store user-specific credentials/tokens outside of main project folder
        self.pf_credentials = self.path_root + 'credentials.csv'

        #ColInfo location
        self.spf_colinfo = self.spathscripts + 'colinfo.xlsx'
        if self.IsTest: self.spf_colinfo = self.path_root + 'colinfo.xlsx'

        #Example for Standalone project file
        self.pf_xyz = self.path_data + 'xyz.xlsx'
        
        #Example for Feather or xlsx database in colinfo.xlsx
        self.f_abcdata = 'abcdata.feather'
        self.pf_abcdata = self.path_data + self.f_abcdata
        self.colCI_abcdata = 'dfabcdata'

    def SetFolderPaths(self):
      """
      Set Project subfolder paths
      """        
      self.path_scripts = self.lstpaths[1]
      self.path_tests = self.path_scripts + 'tests' + os.sep
      self.path_data = self.path_root + self.proj_abbrev + '_data' + os.sep
      sName = self.proj_abbrev + '_case_studies'
      self.path_case_studies = self.path_root + sName + os.sep

      if len(self.path_subdir_home) > 0:
        self.path_home = self.path_case_studies + os.sep + self.path_subdir_home

      #If testing, reassign root and data directories to proj/proj_scripts/tests
      if self.IsTest:
        self.path_root = self.path_tests
        self.path_data = self.path_tests

        #reassign data path if tests subdirectory specified
        if len(self.TestsSubdir) > 0: 
          self.path_subdir_tests = self.TestsSubdir
          self.path_data = self.path_data + self.path_subdir_tests + os.sep

    def SetPathRoot(self):
      """
      Return project's root directory path
      Example usage: iLevelSelf = 2 Structure: root/scripts/libs/dirpathutil.py
      JDL 4/20/22; updated 1/16/23
      """
      PF_thisfile = inspect.getframeinfo(inspect.currentframe()).filename
      self.path_thisfile = str(os.path.dirname(os.path.abspath(PF_thisfile))) + os.sep

      #Build list of paths based on depth of folders relative to projfiles.py
      iLevels = 3
      self.BuildLstPaths(iLevels)
      self.path_root = self.lstpaths[2]

    def BuildLstPaths(self, iLevels):
        """
        Build list of nested directory paths based on location of projfiles.py
        JDL Updated 1/16/23
        """
        # List paths to iLevels levels - starting with home/top, lst[0]; 4/8/22
        PF_thisfile = inspect.getframeinfo(inspect.currentframe()).filename
        path_thisfile = str(os.path.dirname(os.path.abspath(PF_thisfile))) + os.sep
        lstdirs = path_thisfile.split(os.sep)

        self.lstpaths = []
        for i in range(len(lstdirs)-1, len(lstdirs) - iLevels-1, -1):
            self.lstpaths.append(os.sep.join(lstdirs[0:i]) + os.sep)