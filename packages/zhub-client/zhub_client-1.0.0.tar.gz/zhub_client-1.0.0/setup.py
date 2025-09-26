from setuptools import setup, find_packages
import os


setup(
    name='zhub_client',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # "colorama         == 0.4.6",
        # "httplib2         >= 0.15.0", 
        # "urllib3          >= 2.2.1",
        # "sqlUts           >= 1.0.8", 
        # "SQLAlchemy       >= 1.4.50", 
        # "SQLAlchemy-Utils >= 0.38.2", 
        # "python-dotenv    >= 1.0.1", 
        # "psycopg2         >= 2.9.6", 
        # "pycron           >= 3.0.0", 
        # "dateUts          >= 0.3.1", 
        # "iniUts           >= 1.2.1", 
        # "loguru           >= 0.7.2", 
        # "psutil           >= 5.9.6",
        # "requests         >= 2.32.4",
        # "vaultUts         >= 1.1.2",
    ],
    entry_points={
        # "console_scripts": [
        #     "gitup = bot_lib.cli:gitup", 
        #     "upreq = bot_lib.cli:upreq", #OK
        #     "setupy = bot_lib.cli:setupy", #OK
        #     "redeploy = bot_lib.cli:pull_redeploy", #OK
        #     "createstack = bot_lib.cli:create_stack", #OK
        #     "runprd = bot_lib.cli:run_prd", #OK
        #     "runprdstream = bot_lib.cli:run_prd_stream", #OK
        #     "botcommands = bot_lib.cli:botlib_commands",
        #     "bottasks = bot_lib.cli:bot_tasks",
        #     "taskloop = bot_lib.cli:task_loop",
        #     "clearselenoid = bot_lib.selenoid:deletar_todas"
        # ],
    },
    author='Zdek Development team',
    description='Zdek Util libraries for Pythom coding',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/ZdekPyPi/ZhubPythonClient',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',
    author_email='melque_ex@yahoo.com.br',
   license='MIT'
)
