# This Repository is used study and practice MLops
```shell
step 1: Check version python and create environment with conda
Open Anaconda PowerShell Prompt
# check version python in computer local
> python --version
# create environment with Anaconda PowerShell Prompt
> conda create -n env_name python=version
```

```shell
step 2: check list environment is created and activate in env
# check list env is created
> conda info --envs
# to activate environment
> conda activate env_name 
```

```shell
step 3: pip install package and check list name packages is downloaded and version's it
# pip install package
> pip install streamlit
> pip install gradio
# check list name package is downloaded and version's it
> conda list
```

```shell
step 4: Join Visual Studio Code and run application
# Join Visual Studio Code
> code .
# run application
- run app streamlit
> streamlit run file.py
- run app gradio
> gradio file.py
or
> python file.py
```

```shell
step bonus
# change directory
> cd name_dir
# to check list directory in partition of drive
> dir
```
