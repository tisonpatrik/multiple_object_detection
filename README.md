## Dataset

The dataset used for this project, especially for data preprocessing, can be downloaded from [here](https://www.kaggle.com/datasets/biancaferreira/african-wildlife). This dataset contains images of African wildlife and was instrumental in the development and testing of this multiple object detection system.


## Installation

Follow these steps to install the project:

## Prerequisites

This application was developed and tested on a Linux/WSL2 environment. Functionality on other operating systems has not been tested and is not guaranteed.

1. Operating System: Linux / WSL2
2. Python 3.10.12: We recommend using `pyenv` for managing Python versions. If `pyenv` is not installed, you can install it following the instructions [here](https://github.com/pyenv/pyenv#installation). After installing `pyenv`, you can install Python 3.10.12 using `pyenv install 3.10.12`.
3. Pipenv: If not installed, you can install it using `pip install pipenv`.

## Installation

1. Clone the repository: `git clone https://github.com/username/multiple_object_detection.git`
2. Navigate to the project directory: `cd multiple_object_detection`
3. Set the local Python version to 3.10.12 using `pyenv local 3.10.12`.
4. Create a new virtual environment using pipenv: `pipenv --python $(pyenv which python)`
5. Install the required dependencies: `pipenv install`
6. Ensure that `Jupyter Notebook` and `CUDA 12.1` are installed and properly configured on your system.

## Configuration

For data preprocessing and model training, you need to have a `config.json` file in the root of the project with the following structure:

```json
{
    "path": "path/to/raw/data",
    "labeltrainpath": "path/to/train/labels",
    "imgtrainpath": "path/to/train/images",
    "labeltestpath": "path/to/test/labels",
    "imgtestpath": "path/to/test/images",
    "labelvalpath": "path/to/validation/labels",
    "imgvalpath": "path/to/validation/images"
}
```
Replace the path/to/... placeholders with the actual paths on your system. Here's what each field represents:

`path`: The path to the raw data folder.
`labeltrainpath`: The path to the folder where the training labels will be stored.
`imgtrainpath`: The path to the folder where the training images will be stored.
`labeltestpath`: The path to the folder where the test labels will be stored.
`imgtestpath`: The path to the folder where the test images will be stored.
`labelvalpath`: The path to the folder where the validation labels will be stored.
`imgvalpath`: The path to the folder where the validation images will be stored.

This configuration file is used to specify the locations of the raw data and where to store the processed data for training, testing, and validation.

## Usage

1. Activate the virtual environment: `pipenv shell`

2. For data pre-processing, run Jupyter Notebook in the root of the project.

3. For training a new model, run the `run.py` file in the root of the project: `python run.py`

4. To run the application for video processing: `streamlit run app.py`

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
This project is licensed under the MIT License.