# Extract Phone Numbers from JSON File
### Executor: [Eldar Dragomir](https://t.me/oheldarkaa)

### Description:
>I have a large JSON file with contact information.
>
>We need the phone numbers and all contact information extracted from the file and put into an excel spreadsheet or google sheet in organized columns.
>
>Need by May 4th, 2022._ 

### File:

+ [drop box link](https://www.dropbox.com/s/sqb261fmxxf9fmg/Reonomy_Retail.json?dl=0)

---
# Hot to use

## *Go into folder.*

> `cd .\upwork-extract-phone-numbers-from-json-\`

## *Create virual environment and activate it.*

For windows:
```
python -m venv env
./env/Scripts/activate
```
For linux:
```
python -m venv env
source ./python_env/bin/activate
```

I have used **Python 3.9.6** for this project.

## *Then install all needed libraries.*

> `pip install -r requirements.txt`

--- 

## *After that you can run the script through the console:*

```
python transformer.py
```

## *Or start Jupyer Notebook and open there:*

```
pip install jupyter
jupyter notebook
```
open link in console

open transformer.ipynb

start kernel and run all cells

After all done, you will get the file in root folder: 

`extract-phone-numbers-from-json.xlsx`

---
## *Scripts*
+ **transformer.py** - generates output file (extract-phone-numbers-from-json.xlsx) with phones and emails

---
## *Short description how it's working.*

It reads file as json, creating new objects and saves as xlsx.