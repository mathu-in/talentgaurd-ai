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
8. 