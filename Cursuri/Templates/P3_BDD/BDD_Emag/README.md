Emag BDD Automation Framework

Site tested: emag.ro\
Design pattern used: page object model\
Methodology: behavior driven development

To import project\
git clone https://github.com/Andy-ITFactory/emag.git

Libraries to install:\
pip install -U selenium\
pip install behave\
pip install behave-html-formatter\
pip install webdriver-manager

Run tests:\
behave -f html -o behave-report.html --tags=emag

Happy Testing!\

Troubleshoot:\
a.\
Daca nu merge cu pip incercati comanda: py -m pip install selenium\

b.\
Daca nici asa nu merge:\
File -> Settings -> Click pe Project: [nume_proiect] -> Python Interpreter -> +\
Cautati 'selenium' -> Install Package\
La fel si pentru restul librariilor 

c.\
Click pe tabul de jos 'Python Packages'\
Cautati si instalati pachetele

d.\
In ultima instanta, creati voi un proiect nou, instalati cu pip ce trebuie si copiati manual folderele si fisierele necesare. 
