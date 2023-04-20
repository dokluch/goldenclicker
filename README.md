Goldenclicker is an automatic golden cookie clicker for the cookieclicker game https://orteil.dashnet.org/cookieclicker/beta/

It uses a pre-trained Yolov5 model that detects golden and red cookies.

I wrote this overnight as a fun project.
There is no Docker image, since making screenshots means that you have to give elevated priveleges to the Docker image, which I don't like.

Feel free to experiment with the code. Write me if you need a training data and istructions to train your own model.



# Installation instructions

First, clone this repository to a folder on your machine:
```
git clone https://github.com/dokluch/goldenclicker.git
cd goldenclicker
```

Now install all dependencies

## Straight to Python

Make sure you have Python installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

Open a terminal or command prompt and navigate to the directory where your project's requirements.txt file is located.

Run the following command to install the requirements:

```
pip install -r requirements.txt
```

This will install all the required packages and their dependencies.

## Using venv
Open a terminal or command prompt and navigate to the directory where you want to create a virtual environment for your project.

Run the following command to create a new virtual environment:

```
python -m venv goldenclicker
```

This will create a new virtual environment with the name "goldenclicker".

Activate the virtual environment by running the following command:

On Windows: `.\goldenclicker\Scripts\activate.bat`

On Linux/MacOS: `source goldenclicker/bin/activate`
Once the virtual environment is activated, navigate to the directory where your project's requirements.txt file is located.

Run the following command to install the requirements:

```
pip install -r requirements.txt
```

This will install all the required packages and their dependencies inside the virtual environment.

## Using conda
Make sure you have conda installed on your system. You can download and install the latest version of conda from the official website: https://docs.conda.io/projects/conda/en/latest/user-guide/install/

Open a terminal or command prompt and navigate to the directory where your project's requirements.txt file is located.

Run the following command to create a new conda environment:

```
conda create --name goldenclicker python=3.10 -y
```

This will create a new conda environment with the name "goldenclicker" and Python 3 installed.

Activate the conda environment by running the following command:

```
conda activate goldenclicker
```

Once the conda environment is activated, run the following command to install the requirements:

```
conda install --file requirements.txt
```

This will install all the required packages and their dependencies inside the conda environment.

# Acknowledgement
- Yolov5 code by Ultralytics https://github.com/ultralytics/yolov5
- Yolov5 Opencv inference code by doleron https://github.com/doleron/yolov5-opencv-cpp-python

# License
MIT License