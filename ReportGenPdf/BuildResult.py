from numpy import ceil
from SchoolDetailsGen import fetchSchoolDetails
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import utils
from IniRead import ConfigFile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.utils import ImageReader
from rotatedtext import vT
from datetime import datetime
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY,TA_LEFT,TA_CENTER,TA_RIGHT


stylep=getSampleStyleSheet()
stylep = stylep['Normal']
stylen = ParagraphStyle(name='Normal',alignment=TA_CENTER)
stylep.wordWrap = 'CJK'


def add_background(canvas, doc):
    canvas.saveState()
    canvas.drawImage(ImageReader('./Files/Background1.jpg'), 0, 0, 
                     width=A4[1], height=A4[0])
    canvas.restoreState()


def fetchResultSubject(roll,schoolDetails,sDetails,
                       result,overAll, attendance,
                       ScholasticAreasGrade,
                       DisciplneGrade,GeneralStudyGrade,
                       OutStandingAchievementGrade):
    elements = []
    data1 = []
    data2 = []
    data3 =[
        ['Scholastic Area',
         'Term-1', '', '', '','', '', '','',
         'Term-2', '', '', '','','','','',
         'Overall', '', '', '','',''],
        ['Subjects',
         vT('Marks in UT-1\n(MM 40)'),
         vT('Marks in UT-2\n(MM 40)'),
         vT('Marks in Best UT\n(MM 40)'), 
         vT('Marks in Half Yearly Examination\n( MM 80/70/60)'),
         vT('Practical/Internal Assessment\n( MM 20/30/40)'), 
         vT('Total marks(Theory) Half Yearly\nExamination + Best UT'),
         vT('Total of Theory Marks + Best UT\nConverted to 100 marks'),
         vT('Weightage (Theory ) Term-1\n(40% of H)'),
         
         vT('Marks in UT-3\n(MM 40)'),
         vT('Marks in UT-4\n(MM 40)'),
         vT('Marks in Best UT\n(MM 40)'), 
         vT('Marks in Yearly Examination\n( MM 80/70/60)'),
         vT('Practical/Internal Assessment\n( MM 20/30/40)'), 
         vT('Total Marks(Theory) Yearly\nExamination + Best UT'),
         vT('Total of Theory Marks + Best UT\nConverted to 100 marks'),
         vT('Weightage (Theory ) Term-2\n(60% of P )'),
         
         vT('Total of Weightage of Theory\nMM 100( I + Q)'),
         vT('Over all Theory marks\nConverted to MM 80/70/60'),
         vT('Average marks of Practical/Internal\nAssessment MM 20/30/40)\n(Average of F & N )'),
         vT('Total of Theory & Practical/Internal\nAssessment MM 100(S+T)'),
         vT('Grade\n(In Particular Subject)'),
         vT('Rank\n(Subject Wise)')
         ],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W'],
        ]

    data41 = [['Overall Marks']]
    data42 = [['Percentage']]
    data43 = [['Grade']]
    data44 = [['Overall Rank']]
    data45=[['Result']]
    

    data51 = [['Activity', 'T1', 'T2']]
    data52 = [['Activity', 'T1', 'T2']]
    data53 = [['Activity', 'T1', 'T2']]
    
    data61=[['Days', 'T1', 'T2']]
    data62=[['Participation', 'T1', 'T2'],
            ['Yes/No', 'Yes', 'Yes'],]
    data63=[]
    
    data71=[['GRADE','Description'],
            ['A1',Paragraph('Top 1/8<super>th</super> of the passed candidates',stylep)],
            ['A2',Paragraph('Next 1/8<super>th</super> of the passed candidates',stylep)],
            ['B1',Paragraph('Next 1/8<super>th</super> of the passed candidates',stylep)],
            ['B2',Paragraph('Next 1/8<super>th</super> of the passed candidates',stylep)],
            ['C1',Paragraph('Next 1/8<super>th</super> of the passed candidates',stylep)],
            ['C2',Paragraph('Next 1/8<super>th</super> of the passed candidates',stylep)],
            ['D1',Paragraph('Next 1/8<super>th</super> of the passed candidates',stylep)],
            ['D2',Paragraph('Next 1/8<super>th</super> of the passed candidates',stylep)],
            ['E','Essential Repeat']
            ]
    data72=[['GRADE','CONNOTATION'],
            ['A','EXEMPLARY'],
            ['B','PROFICIENT'],
            ['C','DEVELOPING'],
            ['D','EMERGING'],
            ['E','BEGINNER']
            ]
    data73=[['GRADE','CONNOTATION'],
            ['A','OUTSTANDING'],
            ['B','VERY GOOD'],
            ['C','FAIR'],
            ]
    
    data81=[['Class Teacher','Principal']]
    data82=[['**Congratulation Promoted To Class XII-SC',
            'Date : 31/03/2023']]
    
    data841=[]

    
    getSchoolDetails(roll,schoolDetails,data1)
    getStudentDetails(sDetails,data2,data841)
    resultExamWise(result, data3)
    getOverAll(overAll,data41,data42,data43,data44,data45)
    getAttendance(attendance,data61)
    CoScholasticGrade(ScholasticAreasGrade, data51)
    GenStdGrade(GeneralStudyGrade,data52)
    DiscplineGrade(DisciplneGrade, data53)
    OutStndgAchivmnt(OutStandingAchievementGrade, data63)

    t1 = Table(data1, colWidths=[125, 580, 90], 
               rowHeights=[40, None, None, None, None, None, None],
               style=[
        #('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('SPAN', (0, 0), (0, 3)),
        ('SPAN', (2, 0), (2, 3)),
        ('SPAN', (0, 4), (2, 4)),
        ('SPAN', (0, 5), (2, 5)),
        ('SPAN', (0, 6), (2, 6)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (2, 0), 20),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (2, -1), 13),
        ('TEXTCOLOR', (0, 0), (2, 0), colors.HexColor('#fc4108')),
        ('TEXTCOLOR', (0, 1), (2, -1), colors.HexColor('#088afc'))
    ])

    t2 = Table(data2,
               colWidths=[125, 240, 120,90,130,90],
               style=[
                   ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                   ('SPAN', (1, 4), (3, 4)),
                   ('BACKGROUND', (0, 0), (-1,-1), colors.HexColor('#fafcd4')),
                   ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
               ])

    t3 = Table(data3, colWidths=[125, 30, 30, 30, 30, 30,
                                 30, 30, 30, 30, 30, 30,
                                 30, 30, 30,30,30, 30, 30,
                                 40,30,30,30],
        style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (0, 0), (0, 2), 'CENTER'),
        ('SPAN',(1, 0), (8, 0)),
        ('SPAN',(9, 0), (16, 0)),
        ('SPAN',(17, 0), (22, 0)),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BACKGROUND', (0, 0), (0,-1), colors.HexColor('#fcd4d4')),
        ('BACKGROUND', (1, 0), (8,-1), colors.HexColor('#e1fcdc')),
        ('BACKGROUND', (9, 0), (16,-1), colors.HexColor('#fcdcf1')),
        ('BACKGROUND', (17, 0), (22,-1), colors.HexColor('#d2f8fa')),
        ('FONTNAME', (0,2), (-1,2), 'Helvetica-Bold'),
        ('FONTNAME', (20,2), (20,-1), 'Helvetica-Bold')
    ])

    t41 = Table(data41,colWidths=[80,45],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1,-1), colors.HexColor('#c9c9f5')),
        ],)
    t42 = Table(data42,colWidths=[90,60],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1,-1), colors.HexColor('#c9c9f5')),
        ],)
    t43 = Table(data43,colWidths=[60,60],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1,-1), colors.HexColor('#c9c9f5')),
        ],)
    t44 = Table(data44,colWidths=[90,30],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1,-1), colors.HexColor('#c9c9f5')),
        ],)
    t45 = Table(data45,colWidths=[100,60],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1,-1), colors.HexColor('#c9c9f5')),
        ],)
               
    
    data4=[[t41,t42,t43,t44,t45]]
    
    t4 = Table(data4,colWidths=[155,180,132,162,160],
               style=[
        #('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LEFTPADDING', (0, 0), (2, 0), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (3, 0), (3, 0), 18),
        ],)

    t51 = Table(data51, colWidths=[155, 50, 50],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])

    t52 = Table(data52, colWidths=[155, 50, 50],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])
    
    t53 = Table(data53, colWidths=[155, 50, 50],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])

    data5 = [
        ['Co-Scholastic Areas\n(Grading scale A1,A2,B1,B2,C1,C2,D1,D2,E)',
        'General Studies\n(Grading scale A1,A2,B1,B2,C1,C2,D1,D2)',
        'Discipline\n(3 Points grading scale A,B,C)',
         ],
        [t51, t52, t53]
    ]

    t5 = Table(data5,colWidths=[265,265,265],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (1, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (1, 0), (-1, -1), 5),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ],)
    
    t61 = Table(data61, colWidths=[155, 50, 50],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])

    t62 = Table(data62, colWidths=[155, 50, 50],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])
    
    data6 = [
        ['Attendance','10 Bagless Days',
         'Any Outstanding Achievement During The Session'],
        [t61,t62,Paragraph(data63[0][1],stylep)]
    ]

    t6 = Table(data6,colWidths=[265,265,265],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (1, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (1, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ],)
    
    t71 = Table(data71, colWidths=[50, 205],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])

    t72 = Table(data72, colWidths=[100, 155],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])
    
    t73 = Table(data73, colWidths=[100,155],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
        ('ALIGN', (1, 1), (9, 9), 'CENTER'),
    ])

    data7 = [
        ['Grading Scale for Subject',
        'Grading Scale for\nCo-scholastic Areas/General Studies',
        'Grading Scale for Discipline',
         ],
        [t71, t72, t73]
    ]

    t7 = Table(data7,colWidths=[265,265,265],
               style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (1, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (1, 0), (-1, -1), 5),
        ('ALIGN', (0, 0), (2, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ],)
    
    data84=[
        ['Name',data841[0]],
        ['Overall Marks',data41[0][1]],
        ['Overall Rank',data44[0][1]]
        ]
    t84 = Table(data84, colWidths=[75, 180],
                style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (1, 2), 'MIDDLE'),]
        )
    data8=[['Class Teacher','Principal',t84],
           ['**Congratulation Promoted To Class XII-SC', '',
            'Date : 31/03/2023'],] 
    t8=Table(data8,colWidths=[265,265,265],
        style=[
        ('GRID', (0, 0), (2,0), 0.5, colors.grey),
        ('TOPPADDING', (0, 0), (1, 0), 10),
        ('TOPPADDING', (0, 1), (1, 1), 30),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (1, 1), 'BOTTOM'),
        ]
     )

    data = [
        [t1],
        [t2],
        [t3],
        [t4],
        [t5],
        [t6],
        [t7],
        [t8],
    ]

    t = Table(data,
              style=[
                  #('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                  ('TOPPADDING', (0, 0), (-1, -1), 5),
                  ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
                  
              ])

    elements.append(t)
    fname = roll
    print(str(fname)+".pdf")
    doc = SimpleDocTemplate('./Files/ResultPdf/'+str(fname)+".pdf",
                            bottomMargin=5, topMargin=5,
                            rightMargin=10, leftMargin=10,pagesize=landscape(A4))
    doc.build(elements, onLaterPages=add_background)

def getSchoolDetails(roll,schooldetails,data1):
    
    img = utils.ImageReader('./Files/StudentPics/'
                            +str(roll)+'.jpg')
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    width=2.5*cm
    #height=width * aspect
    height=3*cm

    StudentPic = Image('./Files/StudentPics/'
                       +str(roll)+'.jpg'
                       ,width,height)
    
    
    logo = Image('./Files/logo.png')
    logo.drawHeight = .75*inch*logo.drawHeight / logo.drawWidth
    logo.drawWidth = .90*inch

    org = schooldetails.loc[0].to_string(index=False)
    affliation = schooldetails.loc[1].to_string(index=False)
    address = schooldetails.loc[2].to_string(index=False)
    ph_email = schooldetails.loc[3].to_string(index=False)
    report_card = schooldetails.loc[4].to_string(index=False)
    cls= schooldetails.loc[5].to_string(index=False)
    acad_session= schooldetails.loc[6].to_string(index=False)

    data1.append([logo,org,StudentPic])
    data1.append(['',affliation,''])
    data1.append(['',address,''])
    data1.append(['',ph_email,''])
    data1.append([report_card])
    data1.append([cls])
    data1.append([acad_session])

def getStudentDetails(sdetails,data2,data841):
    
    colroll = sdetails.columns[0]
    colano = sdetails.columns[1]
    colname = sdetails.columns[2]
    coldob = sdetails.columns[3]
    colcls = sdetails.columns[4]
    colsection = sdetails.columns[5]
    colgender = sdetails.columns[6]
    colcategory = sdetails.columns[7]
    colmname= sdetails.columns[8]
    colfname= sdetails.columns[9]
    coladdress= sdetails.columns[10]
    

    roll = sdetails[sdetails.columns[0]].to_string(index=False)
    ano = sdetails[sdetails.columns[1]].to_string(index=False)
    name = sdetails[sdetails.columns[2]].to_string(index=False)
    dob = sdetails[sdetails.columns[3]].to_string(index=False)
    cls = sdetails[sdetails.columns[4]].to_string(index=False)
    section = sdetails[sdetails.columns[5]].to_string(index=False)
    gender = sdetails[sdetails.columns[6]].to_string(index=False)
    category = sdetails[sdetails.columns[7]].to_string(index=False)
    mname= sdetails[sdetails.columns[8]].to_string(index=False)
    fname= sdetails[sdetails.columns[9]].to_string(index=False)
    address= sdetails[sdetails.columns[10]].to_string(index=False)
    
    dateobj = datetime.strptime(dob, '%Y-%m-%d')
    newdob = dateobj.strftime('%d.%m.%Y')
    data2.append([colname,Paragraph(name,stylep),colroll,roll,coldob,newdob])
    data2.append([colfname,fname,colano,ano,colcategory,category])
    data2.append([colmname,mname,colgender,gender])
    #data2.append([coldob,dob,colcategory,category])
    #data2.append([coladdress,Paragraph(address,stylep)])
    data841.append([Paragraph(name,stylen)])


def resultExamWise(result, data3):
    
    s1 = result.columns[1]
    s2 = result.columns[2]
    s3 = result.columns[3]
    s4 = result.columns[4]
    s5 = result.columns[5]
    s6 = result.columns[6]
    s7 = result.columns[7]

    sub1 = []
    sub2 = []
    sub3 = []
    sub4 = []
    sub5 = []
    sub6 = []
    sub7 = []

    sub1 = result[s1].tolist().copy()
    sub1.insert(0, result.columns[1])
    sub2 = result[s2].tolist().copy()
    sub2.insert(0, result.columns[2])
    sub3 = result[s3].tolist().copy()
    sub3.insert(0, result.columns[3])
    sub4 = result[s4].tolist().copy()
    sub4.insert(0, result.columns[4])
    sub5 = result[s5].tolist().copy()
    sub5.insert(0, result.columns[5])
    sub6 = result[s6].tolist().copy()
    sub6.insert(0, result.columns[6])
    sub7= result[s7].tolist().copy()
    sub7.insert(0, result.columns[7])
    
    data3.append(int(ceil(num))
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub1)
    data3.append(int(ceil(num)) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub2)
    data3.append(int(ceil(num)) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub3)
    data3.append(int(ceil(num)) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub4)
    data3.append(int(ceil(num)) 
                if isinstance(num, int)
                or isinstance(num, float) else num for num in sub5)
    if 0 in sub6:
        data3.append(int(ceil(num)) 
                    if isinstance(num, int)
                    or isinstance(num, float) else num for num in sub7)
    else:
        data3.append(int(ceil(num)) 
                    if isinstance(num, int)
                    or isinstance(num, float) else num for num in sub6)


def getOverAll(overAll,data41,data42,data43,data44,data45):
    overall_col=overAll.columns[8]
    over_All=overAll[overall_col].tolist().copy()
    percentage=round(over_All[0]*100/600,2)
    data41[0].append(str(round(over_All[0],2))+"/600")
    data42[0].append(percentage)
    data43[0].append(over_All[1])
    data44[0].append(over_All[2])
    data45[0].append("Pass")

def CoScholasticGrade(ScholasticAreasGrade, data51):
    c1 = ScholasticAreasGrade.columns[1]
    c2 = ScholasticAreasGrade.columns[2]
    cosc1 = []
    cosc2 = []
    cosc1 = ScholasticAreasGrade[c1].tolist().copy()
    cosc1.insert(0, ScholasticAreasGrade.columns[1])
    cosc2 = ScholasticAreasGrade[c2].tolist().copy()
    cosc2.insert(0, ScholasticAreasGrade.columns[2])
    data51.append(cosc1)
    data51.append(cosc2)

    
def GenStdGrade(GeneralStudyGrade, data52):
    g1 = GeneralStudyGrade.columns[1]
    gstd1 = []
    gstd1 = GeneralStudyGrade[g1].tolist().copy()
    gstd1.insert(0, GeneralStudyGrade.columns[1])
    data52.append(gstd1)

def DiscplineGrade(DisciplneGrade, data53):
    d1 = DisciplneGrade.columns[1]
    disc1 = []
    disc1 = DisciplneGrade[d1].tolist().copy()
    disc1.insert(0, DisciplneGrade.columns[1])
    data53.append(disc1)
    

def OutStndgAchivmnt(OutStandingA, data63):
    o1 = OutStandingA.columns[1]
    og1 = []
    og1 = OutStandingA[o1].tolist().copy()
    og1.insert(0, OutStandingA.columns[1])
    data63.append(og1)
    

def getAttendance(attendance,data61):
    a1 = attendance.columns[1]
    a2 = attendance.columns[2]
    a3 = attendance.columns[3]
    
    ga1 = []
    ga2 = []
    ga3 = []
    
    ga1 = attendance[a1].tolist().copy()
    ga2 = attendance[a2].tolist().copy()
    ga3 = attendance[a3].tolist().copy()
    ga1.insert(0, attendance.columns[1])
    ga2.insert(0, attendance.columns[2])
    ga3.insert(0, attendance.columns[3])
    data61.append(ga1)
    data61.append(ga2)
    data61.append(ga3)