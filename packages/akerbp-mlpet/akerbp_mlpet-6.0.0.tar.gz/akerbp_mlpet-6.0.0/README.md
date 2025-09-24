# akerbp.mlpet

Preprocessing tools for Petrophysics ML projects at Eureka

## Installation

Install the package by running the following (requires python 3.8 or later)

        pip install akerbp.mlpet


## Quick start

For a short example of how to use the mlpet Dataset class for pre-processing data see below. Please refer to the tests folder of this repository for more examples as well as some examples of the `settings.yaml` file:

        import os
        from akerbp.mlpet import Dataset
        from akerbp.mlpet import utilities

        # Instantiate an empty dataset object using the example settings and mappings provided
        ds = Dataset(
                settings=os.path.abspath("settings.yaml"), # Absolute file paths are required
                folder_path=os.path.abspath(r"./"), # Absolute file paths are required
        )

        # Populate the dataset with data from a file (support for multiple file formats and direct cdf data collection exists)
        ds.load_from_pickle(r"data.pkl") # Absolute file paths are preferred

        # The original data will be kept in ds.df_original and will remain unchanged
        print(ds.df_original.head())

        # Split the data into train-validation sets
        df_train, df_test = utilities.train_test_split(
                df=ds.df_original,
                target_column=ds.label_column,
                id_column=ds.id_column,
                test_size=0.3,
        )

        # Preprocess the data for training according to default workflow
        # print(ds.default_preprocessing_workflow) <- Uncomment to see what the workflow does
        df_preprocessed = ds.preprocess(df_train)


The procedure will be exactly the same for any other dataset class. The only difference will be in the "settings". For a full list of possible settings keys see either the [built documentation](docs/build/html/akerbp.mlpet.html) or the akerbp.mlpet.Dataset class docstring. Make sure that the curve names are consistent with those in the dataset.

The loaded data is NOT mapped at load time but rather at preprocessing time (i.e. when preprocess is called).

## Recommended workflow for preprocessing

Due to the operations performed by certain preprocessing methods in akerbp.mlpet, the order in which the different preprocessing steps can sometimes be important for achieving the desired results. Below is a simple guide that should be followed for most use cases:
1. Misrepresented missing data should always be handled first (using `set_as_nan`)
2. This should then be followed by data cleaning methods (e.g. `remove_outliers`, `remove_noise`, `remove_small_negative_values`)
3. Depending on your use case, once the data is clean you can then impute missing values (see `imputers.py`). Note however that some features depend on the presence of missing values to provide better estimates (e.g. `calculate_VSH`)
4. Add new features (using methods from `feature_engineering.py`) or using `process_wells` from `preprocessors.py` if the features should be well specific.
5. Fill missing values if any still exist or were created during step 4. (using `fillna_with_fillers`)
6. Scale whichever features you want (using `scale_curves` from `preprocessors.py`). In some use cases this step could also come before step 5.
7. Encode the GROUP & FORMATION column if you want to use it for training. (using `encode_columns` from `preprocessors.py`)
8. Select or drop the specific features you want to keep for model training. (using `select_columns` or `drop_columns` from `preprocessors.py`)

> **_NOTE:_**  The dataset class **drops** all input columns that are not explicitly named in your settings.yaml or settings dictionary passed to the Dataset class at instantiation. This is to ensure that the data is not polluted with features that are not used. Therefore, if you have features that are being loaded into the Dataset class but are not being preprocessed, these need to be explicitly defined in your settings.yaml or settings dictionary under the keyword argument `keep_columns`.

## API Documentation

Full API documentaion of the package can be found under the [docs](docs/build/html/index.html) folder once you have run the make html command.

## For developers

- to make the API documentation, from the root directory of the project run (assuming you have installed all development dependencies)

        cd docs/
        make html

- to install mlpet in editable mode for use in another project, there are two
  possible solutions dependent on the tools being used:
   1. If the other package uses poetry, please refer to this [guide](https://github.com/python-poetry/poetry/discussions/1135#discussioncomment-145756)
   2. If you are not using poetry (using conda, pyenv or something else), just revert to using `pip install -e .` from within the root directory (Note: you need to have pip version >= 21.3).
## License

akerbp.mlpet Copyright 2021 AkerBP ASA

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
