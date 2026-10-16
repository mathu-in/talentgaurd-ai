#Talent Gaurd - AI
Employee Attrition Prediction Application

##Technologies
- Python
- Machine Learning
- Postgre SQL
- Fast API
- Streamlit
- Docker
- AWS

##Status
Project under development


##library installation
```
pip install -r requirements.txt
```

Note:

python -m pip cache purge
1. installation command for pandas:
        python -m pip install pandas==2.2.3 --no-cache-dir
        python -m pip install --no-cache-dir matplotlib
        python -m pip install scikit-learn==1.7.2  ---- failed
        python -m pip install --index-url https://pypi.org/simple joblib
        python -m pip install --index-url https://pypi.org/simple scikit-learn==1.6.1

 

2. Dataset 
        https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

3. Unable to run this command in talent-gaurd directory
        python .\src\main.py
        - After moving data_ingestion.py and data_validation.py unable to run main.py -- so mentioning directory
        - Talent_Gaurd) PS D:\Talent_Gaurd\src> python -m components.data_validation 

*4. data_ingestion.py / main.py : data/data2/df
*5. refractor: purpose : move/edit/rename
        - Option not available while creating new file

*6. git push ---> No configured push destination.(Sometimes)  -- After restarting py-charm issue resolved.

(Talent_Gaurd) PS D:\Talent_Gaurd\src> git remote -v
(Talent_Gaurd) PS D:\Talent_Gaurd\src> git remote add origin https://github.com/mathu-in/talentgaurd-ai          
(Talent_Gaurd) PS D:\Talent_Gaurd\src> git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/mathu-in/talentgaurd-ai'

Note: Always run git push command in "D:\Talent_Gaurd>" path

(Talent_Gaurd) PS D:\Talent_Gaurd\src>git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

(Talent_Gaurd) PS D:\Talent_Gaurd> git push
Everything up-to-date
7. def main
        main() is written in data_validation.py also in main.py --- shall we import main() from data_validation.py?
8. path.py:
        - PROJECT_ROOT = Path(__file__).resolve().parents[2]
        - parents[2] --- 2 directories outside considered as parent/root project directory

9. (Talent_Gaurd) PS D:\Talent_Gaurd> python -m src.components.data_ingestion


Columns:

['numerical__Age' 'numerical__DailyRate' 'numerical__DistanceFromHome'
 'numerical__Education' 'numerical__EmployeeCount'
 'numerical__EmployeeNumber' 'numerical__EnvironmentSatisfaction'
 'numerical__HourlyRate' 'numerical__JobInvolvement' 'numerical__JobLevel'
 'numerical__JobSatisfaction' 'numerical__MonthlyIncome'
 'numerical__MonthlyRate' 'numerical__NumCompaniesWorked'
 'numerical__PercentSalaryHike' 'numerical__PerformanceRating'
 'numerical__RelationshipSatisfaction' 'numerical__StandardHours'
 'numerical__StockOptionLevel' 'numerical__TotalWorkingYears'
 'numerical__TrainingTimesLastYear' 'numerical__WorkLifeBalance'
 'numerical__YearsAtCompany' 'numerical__YearsInCurrentRole'
 'numerical__YearsSinceLastPromotion' 'numerical__YearsWithCurrManager'
 'categorical__BusinessTravel_Non-Travel'
 'categorical__BusinessTravel_Travel_Frequently'
 'categorical__BusinessTravel_Travel_Rarely'
 'categorical__Department_Human Resources'
 'categorical__Department_Research & Development'
 'categorical__Department_Sales'
 'categorical__EducationField_Human Resources'
 'categorical__EducationField_Life Sciences'
 'categorical__EducationField_Marketing'
 'categorical__EducationField_Medical' 'categorical__EducationField_Other'
 'categorical__EducationField_Technical Degree'
 'categorical__Gender_Female' 'categorical__Gender_Male'
 'categorical__JobRole_Healthcare Representative'
 'categorical__JobRole_Human Resources'
 'categorical__JobRole_Laboratory Technician'
 'categorical__JobRole_Manager'
 'categorical__JobRole_Manufacturing Director'
 'categorical__JobRole_Research Director'
 'categorical__JobRole_Research Scientist'
 'categorical__JobRole_Sales Executive'
 'categorical__JobRole_Sales Representative'
 'categorical__MaritalStatus_Divorced'
 'categorical__MaritalStatus_Married' 'categorical__MaritalStatus_Single'
 'categorical__Over18_Y' 'categorical__OverTime_No'
 'categorical__OverTime_Yes']