@echo off
echo [%date% %time%]: START

echo [%date% %time%]: creating env with python 3.8 version
conda create --prefix ./env python=3.8 -y

echo [%date% %time%]: activating the environment
call conda activate ./env

echo [%date% %time%]: installing the dev requirements
pip install -r requirements.txt

echo [%date% %time%]: END
