# Multiple object detection

## Prerequisites

This application was developed and tested on a Linux/WSL2 environment. Functionality on other operating systems has not been tested and is not guaranteed.

1. Operating System: Linux / WSL2
2. Python 3.10.12: We recommend using `pyenv` for managing Python versions. If `pyenv` is not installed, you can install it following the instructions [here](https://github.com/pyenv/pyenv#installation). After installing `pyenv`, you can install Python 3.10.12 using `pyenv install 3.10.12`.
3. Recomended enviroment manager is [pipenv](https://pipenv.pypa.io/en/latest/), but its not mandatory.
4. Follow this instructions

## Try detection with app

### Installation and usage

1. Clone the repository
2. Navigate to the project directory
3. Set the local Python version to 3.10.12
4. Create and activate new virtual environment
5. Install the required dependencies: `pipenv install` or `pip install -r requirements.txt`
6. To run the application for video processing: `streamlit run app.py`


## Try train your own model

At first, you need have collected some dataset. How should looks annotations, check official docs from [ultralytics](https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format). Images do not have to be in the same resolution, or format. The only thing you need to pay attention to is that a file with annotations (dog.txt) is available in the same folder for each image (dog.png) 

### Dataset

1. Create in root directory this structure: `data/dataset`
2. Inside of `dataset` directory add images (supported formats are `jpg` and `png`) and anotations (`txt`) files
3. Into `data` directory insert `obj.names` file
3. Be sure that you can run `Jupyter Notebooks` on your machine
4. Open `data_processing.ipynb` and run it.
5. Script will create some new directories in `data` directory and will do some magic there

### Training

1. Be sure that your machine is supported and you have installed `CUDA 12.1`.
2. Run `train.py` script
3. Go to sleep, or make coffee bcs this will take some time....
4. If training will be success, new model will be created and sreamlit app will find it and will use this model as default. 


## Contributing
Contributions are welcome! Please feel free to submit a pull request.

### Setting Up in Visual Studio Code

If you are using Visual Studio Code as your IDE, you may need to specify the path to the Python interpreter in the `.code-workspace` file..

Here's how you can do it:

1. Open the `.code-workspace` file in your workspace.
2. Look for the `settings` object
3. Inside the `settings` object, add or modify the `python.defaultInterpreterPath` property. The value should be the absolute path to the Python interpreter you want to use.

## License
This project is licensed under the MIT License.