import pandas as pd
from IniRead import ConfigFile

def fetchOStndngAchv(roll):

    file = ConfigFile.Default['ResultFile']
    resultData = pd.read_excel(file, sheet_name=[
        'OutStandingAchieveMent'])
    sRecord = pd.DataFrame()
    for examName in resultData:
        rollColumn = resultData[examName].columns[0]
        x = resultData[examName].loc[resultData[examName][rollColumn] == roll]
        sRecord = sRecord.append(x)
    return sRecord
