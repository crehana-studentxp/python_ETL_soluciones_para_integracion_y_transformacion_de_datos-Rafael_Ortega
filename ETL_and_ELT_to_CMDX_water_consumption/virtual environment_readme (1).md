The process for creating a virtual environment for python on windows followed [this link](https://medium.com/co-learning-lounge/create-virtual-environment-python-windows-2021-d947c3a3ca78)

This is the process to follow on windows

# Creating a virtual environment for pyhon

## Step 1: Create
To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

```bash
python3 -m venv crehana_md_bi_specialist
```

## Step 2: Activate

```bash
.\crehana_md_bi_specialist\Scripts\activate
```


## Step 3: Deactivate
```bash
deactivate
```
# Installing packages

```bash
pip install pandas
```

# Installing Jupyter lab on environment

```bash
pip install ipykernel
```

```bash
pip install jupyterlab
```

```bash
pip install jupyter
```

```bash
python3 -m ipykernel install --user --name crehana_md_bi_specialist --display-name crehana_md_bi_specialist
```

## Open Jupter lab
```bash
jupyter lab
```


## Installing the requirements.txt
ponerse en la carpeta donde se encuentra el archivo requirements.txt
correr el comando 
```bash
pip install -r requirements.txt
```

## Otherwise, installing package by package
```bash
pip install matplotlib
pip install numpy
pip install pandas
pip install seaborn
pip install plotly

```