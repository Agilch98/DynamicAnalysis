# DynamicAnalysis

A repository for evaluating dynamic loading of orthopaedic implants

## Setup

Install a web browser if you havent

```bash
sudo apt update
sudo apt install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```

Create a python Environment

```bash
python -m venv DynAnalysis
```

Activate Environment

```bash
source ./DynAnalysis/bin/activate
```

Install dependancies

```bash
pip install -r requirements.txt
```

To run code:

```bash
python ./DynamicAnalysis/PythonFiles/dynamic1/dynamic_difference_plot_200_400.py
```
