import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent

class DataFrames:
    _sp1500_cross_sectional = None
    _sp1500_panel = None
    
    @property
    def sp1500_cross_sectional(self):
        if self._sp1500_cross_sectional is None:
            self._sp1500_cross_sectional = pd.read_excel(DATA_DIR / 'sp1500_cross_sectional.xlsx')
        return self._sp1500_cross_sectional
    
    @property
    def sp1500_panel(self):
        if self._sp1500_panel is None:
            self._sp1500_panel = pd.read_excel(DATA_DIR / 'sp1500_panel.xlsx')
        return self._sp1500_panel

# Create a single instance
_data = DataFrames()

# Define module-level functions that return the data
def sp1500_cross_sectional():
    return _data.sp1500_cross_sectional

def sp1500_panel():
    return _data.sp1500_panel
