import pandas as pd
from CoScholasticAreasGradeGen import fetchCoScholasticAreasGrade
from DisciplineGradeGen import fetchDisciplneGrade
from BuildResult import fetchResultSubject
from StudentsDeatailsGen import fetchAllStudentDetails,fetchStudentDetails
from SchoolDetailsGen import fetchSchoolDetails
from GenStudyGradeGen import fetchGenStdGrade
from OutStandignAchievmentGen import fetchOStndngAchv
from AttendanceGen import fetchAttendance

from IniRead import ConfigFile
def fetchResult(roll):
    file = ConfigFile.Default['ResultFile']
    resultData = pd.read_excel(file, sheet_name=['UT1','UT2','BestUT1', 
                                                 'HY', 'HYP',
                                                 'T1UT','T1UT100','T1UT40',
                                                 'UT4','UT5','BestUT2', 
                                                 'Y', 'YP',
                                                 'T2UT','T2UT100','T2UT40',
                                                 'GT','GTT','GTP',
                                                 'Final', 'Grade',
                                                 'Rank'])
    sRecord = pd.DataFrame()
    for examName in resultData:
        rollColumn = resultData[examName].columns[0]
        x = resultData[examName].loc[resultData[examName][rollColumn] == roll]
        sRecord = sRecord.append(x)
    sRecord=sRecord.fillna('')
    return sRecord

def fetchOverAll(roll):
    file = ConfigFile.Default['ResultFile']
    resultData = pd.read_excel(file, sheet_name=['Final', 'Grade',
                                                 'Rank'])
    sRecord = pd.DataFrame()
    for examName in resultData:
        rollColumn = resultData[examName].columns[0]
        x = resultData[examName].loc[resultData[examName][rollColumn] == roll]
        sRecord = sRecord.append(x)
    sRecord=sRecord.fillna('')
    return sRecord

def MarksGenAll():
    sData = fetchAllStudentDetails()
    rolColumnName = sData['StudentDetails'].columns[0]
    rollColData = sData['StudentDetails'][rolColumnName]
    #rollColData=[1,2,39]
    for roll in rollColData:
        schoolDetails=fetchSchoolDetails()
        sDetails=fetchStudentDetails(roll)
        result = fetchResult(roll)
        overAll=fetchOverAll(roll)
        attendance=fetchAttendance(roll)
        Cograde= fetchCoScholasticAreasGrade(roll)
        DiscGrade= fetchDisciplneGrade(roll)
        GenStdGrade=fetchGenStdGrade(roll)
        OStndngAchv=fetchOStndngAchv(roll)
        
        fetchResultSubject(roll, schoolDetails, sDetails, 
                           result, overAll, attendance,
                           Cograde, DiscGrade,GenStdGrade,
                           OStndngAchv)
