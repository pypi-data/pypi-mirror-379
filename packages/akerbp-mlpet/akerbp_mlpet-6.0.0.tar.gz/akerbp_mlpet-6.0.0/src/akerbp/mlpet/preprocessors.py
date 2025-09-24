"""
This module contains all the preprocessors available to the Dataset class of the
mlpet repo (besides the preprocessing functions found in feature_engineering and
imputers). All preprocessing functions in mlpet **MUST** follow a strict API
in order to be used in conjunction with the preprocess method of the Dataset
class.

The preprocessing API looks like this::

    def some_preprocessing_function(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        ...
        do_something
        ...
        return df

This API allows for defining a preprocessing pipeline at runtime and passing it
to the preprocess method instead of defining it prior to the initialisation of
the Dataset class.

"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import joblib
import numpy as np
import pandas as pd
import sklearn.preprocessing
from sklearn.base import BaseEstimator

import akerbp.mlpet.feature_engineering as feature_engineering
import akerbp.mlpet.imputers as imputers
import akerbp.mlpet.utilities as utilities

# ruff: noqa: N806
logger = logging.getLogger(__name__)


def set_as_nan(df_: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Replaces the provided numerical and categorical values with np.nan in the
    respective numerical and categorical columns. If numerical or categorical
    column names are not provided they will be inferred using the get_col_types
    utility function

    Args:
        df (pd.DataFrame): dataframe to apply metadata to

    Keyword Args:
        numerical_curves (List[str], optional): The numerical columns in which the
            numerical value should be replaced with np.nan.
        categorical_curves (List[str], optional): The categorical columns in which
            the numerical value should be replaced with np.nan.
        numerical_value (float/int, optional): The numerical value that should be replaced with np.nan.
        categorical_value (str, optional): The categorical value that should be replaced with np.nan.

    Returns:
        df (pd.Dataframe): The original dataframe filled with np.nan where
            requested
    """
    df = df_.copy()
    # Processing inputs
    numerical_curves: Optional[List[str]] = kwargs.get("numerical_curves", None)
    categorical_curves: Optional[List[str]] = kwargs.get("categorical_curves", None)
    numerical_value = kwargs.get("numerical_value")
    categorical_value = kwargs.get("categorical_value")
    warn = kwargs.get("warn", True)

    inferred_numeric, inferred_categorical = utilities.get_col_types(
        df, categorical_curves, warn
    )
    # Ensure user is using method the correct way
    if numerical_value is not None:
        if numerical_curves is None:
            numerical_curves = inferred_numeric
        df.loc[:, numerical_curves] = df[numerical_curves].replace(
            to_replace=numerical_value, value=np.nan
        )
    if categorical_value:
        if categorical_curves is None:
            categorical_curves = inferred_categorical
        df.loc[:, categorical_curves] = df[categorical_curves].replace(
            to_replace=categorical_value, value=np.nan
        )

    return df


def remove_outliers(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Returns the dataframe after applying the curve specific cutoff values if
    the threshold (th) of the number of outliers is passed. The following
    curves and corresponding cutoff values are used (if they exist in the
    provided curves list):

        - GR: low cutoff: 0, high cutoff: 250 gAPI
        - RMIC: low cutoff: 0, high cutoff: 100 above which set to 100
        - RMED: low cutoff: 0, high cutoff: 100 above which set to 100
        - RDEP: low cutoff: 0, high cutoff: 100 above which set to 100
        - RSHA: low cutoff: 0, high cutoff: 100 above which set to 100
        - NEU: low cutoff: -0.5, high cutoff: 1 (replaced with np.nan) v/v
        - PEF: high cutoff: 10 (replaced with np.nan)

    If not otherwise specified above, values above/below the cutoffs are replaced
    with the corresponding cutoff value.

    Args:
        df (pd.DataFrame): dataframe to remove outliers

    Keyword Args:
        outlier_curves (list): The curves to remove outliers for using the above rules
        threshold (float, optional): threshold of number of samples that are outliers.
            Used for displaying warnings of too many samples removed. Defaults to 0.05.

    Returns:
        pd.DataFrame: dataframe without outliers
    """
    th = kwargs.get("threshold", 0.05)
    outlier_curves = kwargs.get("outlier_curves", None)

    if outlier_curves is not None:
        with np.errstate(divide="ignore", invalid="ignore"):
            if "GR" in outlier_curves:
                outliers = df[(df.GR < 0) | (df.GR > 250)]
                valid_GR = df.GR.notna().sum()
                if len(outliers) / valid_GR > th:
                    logger.warning(
                        f"GR has more than {th * 100}% of its values lower"
                        " than 0 or higher than 250. Replacing them with either 0"
                        " or 250. Note: This column name is the name after it has"
                        " been mapped using the provided mappings.yaml! So it could"
                        " be another column from your original data that triggered"
                        " this warning and instead was mapped to the name printed above.",
                        stacklevel=2,
                    )
                df.GR = df.GR.clip(lower=0, upper=250)

            for resistivity in ["RMIC", "RSHA", "RMED", "RDEP"]:
                if resistivity in outlier_curves:
                    outliers = df[resistivity] > 100
                    valid_res = df[resistivity].notna().sum()
                    if outliers.sum() / valid_res > th:
                        logger.warning(
                            f"{resistivity} has more than {th * 100}% of its values higher"
                            " than 100. Note: This column names is the name after it has"
                            " been mapped using the provided mappings.yaml! So it could"
                            " be another column from your original data that triggered"
                            " this warning and instead was mapped to the name printed above.",
                            stacklevel=2,
                        )
                    df.loc[outliers, resistivity] = 100
                    # Remove negative values
                    df.loc[df[resistivity] < 0, resistivity] = np.nan

            if "NEU" in outlier_curves:
                outliers = (df.NEU < -0.5) | (df.NEU > 1)
                valid_NEU = df.NEU.notna().sum()
                ratio = outliers.sum() / valid_NEU
                if ratio > th:
                    logger.warning(
                        f"NEU has {ratio * 100}% of its values higher than 1"
                        " or lower than -0.5. The threshold for this warning is"
                        f" {th * 100}%",
                        stacklevel=2,
                    )
                df.loc[outliers, "NEU"] = np.nan

            if "PEF" in outlier_curves:
                outliers = df.PEF > 10
                valid_PEF = df.PEF.notna().sum()
                if outliers.sum() / valid_PEF > th:
                    logger.warning(
                        f"PEF has more than {th * 100}% of its values higher than 10",
                        stacklevel=2,
                    )
                df.loc[outliers, "PEF"] = np.nan
                # Remove negative PEF values
                df.loc[df.PEF < 0, "PEF"] = np.nan

    return df


def remove_small_negative_values(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Replaces small negative values with np.NaN in all the numeric columns. The
    small negative values are determined by defining a nan_threshold. If the
    negative value is smaller than the threshold it is set to nan. Naturally,
    this operation is only done on numeric columns.

    Args:
        df (pd.DataFrame): dataframe to be preprocessed
        numerical_curves (List[str]): The column names for which small negative values should
            be replaced with NaNs. If not provided, this list is generated using
            the get_col_types utility function
        nan_threshold (float, optional): The threshold determing the smallest
            acceptable negative value. Defaults to None

    Returns:
        pd.DataFrame: preprocessed dataframe
    """
    nan_threshold = kwargs.get("nan_threshold")
    numerical_curves = kwargs.get("numerical_curves", None)
    if numerical_curves is None:
        # Only interested in numerical columns so no need to flood console with
        # warnings related to categorical curves
        numerical_curves, _ = utilities.get_col_types(df, warn=False)
    if nan_threshold is not None:
        # remove small negative values
        for col in numerical_curves:
            df.loc[df[col] <= nan_threshold, col] = np.NaN
    return df


def fill_zloc_from_depth(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Fill missing values in Z_LOC column with values from the DEPTH_MD column

    Args:
        df (pd.DataFrame): The dataframe containing both Z_LOC and DEPTH_MD columns

    Returns:
        pd.DataFrame: The original dataframe with the Z_LOC column filled where
            possible.
    """
    # fill the missing Z_LOC values with regards to DEPTH_MD(always present)
    if ("Z_LOC" in df.columns) and ("DEPTH_MD" in df.columns):
        df.loc[:, "Z_LOC"] = df["Z_LOC"].fillna(-(df["DEPTH_MD"] - 20))
    return df


def fillna_with_fillers(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Fills all NaNs in numeric columns with a num_filler and all NaNs in
    categorical columns with a cat_filler. All four of these variables are
    passed as kwargs.

    If a num_filler and/or cat_filler is passed without corresponding column
    names, column types are inferred using the get_col_type utility function.

    Args:
        df (pd.DataFrame): The dataframe to be preprocessed

    Keyword Args:
        num_filler (float): The numeric value to fill nans with in the numeric
        numerical_curves (List[str]): The column names for all numeric columns
            where the NaNs will be filled with the num_filler
        cat_filler (float): The numeric value to fill nans with in the numeric
        categorical_curves (List[str]): The column names for all numeric columns
            where the NaNs will be filled with the num_filler
    Returns:
        pd.DataFrame: Preprocessed dataframe
    """
    # Process kwargs
    num_filler = kwargs.get("num_filler")
    cat_filler = kwargs.get("cat_filler")
    numerical_curves = kwargs.get("numerical_curves", None)
    categorical_curves = kwargs.get("categorical_curves", None)
    warn = kwargs.get("warn", True)
    inferred_numeric, inferred_categorical = utilities.get_col_types(
        df, categorical_curves, warn
    )

    if numerical_curves is None:
        numerical_curves = inferred_numeric
    if categorical_curves is None:
        categorical_curves = inferred_categorical
    # Fill missing rows with num and cat filler
    if num_filler is not None:
        df.loc[:, numerical_curves] = df[numerical_curves].fillna(num_filler)
    if cat_filler is not None:
        df.loc[:, categorical_curves] = df[categorical_curves].fillna(cat_filler)
    return df


def encode_columns(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Encodes categorical columns. Only available for:
        - MEMBER column - categories are encoded using the members_map
            provided in the kwargs.
        - FORMATION column - categories are encoded using the formations_map
            provided in the kwargs.
        - GROUP column - categories are encoded using the groups_map
            provided in the kwargs
        - SYSTEM column - categories are encoded using the systems_map
            provided in the kwargs

    Note: All names are normalized prior to mapping using the utility function
        normalize_group_formation_system and all categories that weren't mapped
        are encoded with missing_encoding_value.

    Args:
        df (pd.DataFrame): dataframe to which apply encoding of categorical variables

    Keyword Args:
        columns_to_encode (list): which columns to encode. Default to no columns being
            encoded. If no columns are passed the get_col_types utility function
            is used to determine the categorical columns
        members_map (dict): A mapping dictionary mapping member names to
            corresponding numbers. Defaults to an empty dictionary (ie no encoding).
        formations_map (dict): A mapping dictionary mapping formation names to
            corresponding numbers. Defaults to an empty dictionary (ie no encoding).
        groups_map (dict): A mapping dictionary mapping group names to
            corresponding numbers. Defaults to an empty dictionary (ie no encoding).
        systems_map (dict): A mapping dictionary mapping system names to
            corresponding numbers. Defaults to an empty dictionary (ie no encoding).
        missing_encoding_value (float): The value to fill encode categories for which
            no match was found in the provided mappings. Defaults to -1.0.

    Returns:
        pd.DataFrame: dataframe with categorical columns encoded
    """
    columns_to_encode: Optional[List[str]] = kwargs.get("columns_to_encode", None)
    members_map: Optional[Dict[str, float]] = kwargs.get("members_map", None)
    formations_map: Optional[Dict[str, float]] = kwargs.get("formations_map", None)
    groups_map: Optional[Dict[str, float]] = kwargs.get("groups_map", None)
    systems_map: Optional[Dict[str, float]] = kwargs.get("systems_map", None)
    missing_encoding_value: float = kwargs.get("missing_encoding_value", -1.0)
    warn = kwargs.get("warn", True)

    if columns_to_encode is None:
        _, columns_to_encode = utilities.get_col_types(df, warn=warn)

    if "MEMBER" in columns_to_encode and members_map is not None:
        df["MEMBER"] = df["MEMBER"].map(members_map)
        df["MEMBER"] = df["MEMBER"].fillna(missing_encoding_value)
        df["MEMBER"] = df["MEMBER"].astype(float)
    if "FORMATION" in columns_to_encode and formations_map is not None:
        df["FORMATION"] = df["FORMATION"].map(formations_map)
        df["FORMATION"] = df["FORMATION"].fillna(missing_encoding_value)
        df["FORMATION"] = df["FORMATION"].astype(float)
    if "GROUP" in columns_to_encode and groups_map is not None:
        df["GROUP"] = df["GROUP"].map(groups_map)
        df["GROUP"] = df["GROUP"].fillna(missing_encoding_value)
        df["GROUP"] = df["GROUP"].astype(float)
    if "SYSTEM" in columns_to_encode and systems_map is not None:
        df["SYSTEM"] = df["SYSTEM"].map(systems_map)
        df["SYSTEM"] = df["SYSTEM"].fillna(missing_encoding_value)
        df["SYSTEM"] = df["SYSTEM"].astype(float)

    return df


def onehot_encode_columns(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Onehot encodes all columns provided via the columns_to_onehot_encode kwarg.

    Note: NaNs are not encoded. They are separated into an individual NaN column
        and that column is automatically dropped.

    Args:
        df (pd.DataFrame): dataframe to which apply onehot encoding of categorical variables

    Keyword Args:
        columns_to_onehot_encode (list): which columns to encode. Default to no columns being
            encoded. If no columns are passed, this method raises a warning and
            does nothing.
        categories_to_keep (list): A list of categories to keep. If None, all categories
            are kept. The categories are all prefixed with their corresponding column name and an
            underscore. For example, if the column name is "GROUP" and the category is "CROMER KNOLL GP", the
            category name would be "GROUP_CROMER KNOLL GP".

    Returns:
        pd.DataFrame: dataframe with categorical columns encoded
    """
    columns_to_onehot_encode: Optional[List[str]] = kwargs.get(
        "columns_to_onehot_encode", None
    )
    categories_to_keep: Optional[List[str]] = kwargs.get("categories_to_keep", None)
    if columns_to_onehot_encode is not None:
        encoded = pd.get_dummies(
            df[columns_to_onehot_encode],
            columns=columns_to_onehot_encode,
            dummy_na=False,
            dtype=int,
        )
        cols_to_keep = (
            encoded.columns if categories_to_keep is None else categories_to_keep
        )
        for col in cols_to_keep:
            if col not in encoded.columns:
                logger.warning(
                    f"{col} could not be found after one hot encoding. "
                    "Initialising it with all np.nans! Make sure to check the "
                    "categories_to_keep argument!",
                    stacklevel=2,
                )
                encoded[col] = np.nan
        df = pd.concat([df, encoded[cols_to_keep]], axis=1)
        return df, {"onehot_columns": cols_to_keep}
    else:
        logger.warning(
            "No columns to onehot encode provided. Doing nothing.",
            UserWarning,
            stacklevel=2,
        )
        return df


def select_columns(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Returns a dataframe with only curves chosen by user, filtered from the original dataframe

    Args:
        df (pd.DataFrame): dataframe to filter

    Keyword Args:
        curves_to_select (list): which curves should be kept. Defaults to None.
        label_column (str): The name of the label column to keep if also desired. Defaults to None
        id_column (str): The name of the id column to keep if also desired. Defaults to None

    Returns:
        pd.DataFrame: dataframe with relevant curves
    """
    curves_to_select: Optional[List[str]] = kwargs.get("curves_to_select", None)
    label_column: Optional[str] = kwargs.get("label_column", None)
    id_column: Optional[str] = kwargs.get("id_column", None)

    if curves_to_select is not None:
        curves_to_keep = list(set(curves_to_select))
        if label_column is not None and label_column in df.columns:
            curves_to_keep += [label_column]
        if id_column is not None and id_column in df.columns:
            curves_to_keep += [id_column]

        df = df.loc[:, curves_to_keep]

    return df


def drop_columns(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Returns a dataframe with the requested curves dropped

    Args:
        df (pd.DataFrame): dataframe to filter

    Keyword Args:
        curves_to_drop (list): The curves to be dropped. Defaults to None.

    Returns:
        pd.DataFrame: dataframe with requested curves dropped
    """
    curves_to_drop: Optional[List[str]] = kwargs.get("curves_to_drop", None)

    if curves_to_drop is not None:
        curves_to_drop = list(set(curves_to_drop))
        df = df.drop(columns=curves_to_drop)

    return df


def fill_columns(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Fills missing values in the dataframe according to the fill mapping provided.

    Args:
        df (pd.DataFrame): dataframe to fill
        columns_to_fill (dict): which columns to fill where the keys
            are the main columns to be filled in with values from the columns
            listed in the values. Defaults to None.
        missing_value (float): The value that is used to represent missing values. Defaults to np.nan

    Returns:
        pd.DataFrame: dataframe with columns filled according to the provided mapping
    """
    columns_to_fill: Optional[Dict[str, List[str]]] = kwargs.get(
        "columns_to_fill", None
    )
    missing_value: Optional[float] = kwargs.get("missing_value", None)

    if missing_value is None:
        missing_value = np.nan

    if columns_to_fill is not None:
        for main_column, columns_to_fill_with in columns_to_fill.items():
            df[main_column] = df[main_column].replace(missing_value, np.nan)
            for column_to_fill_with in columns_to_fill_with:
                df[main_column] = df[main_column].fillna(df[column_to_fill_with])
            df[main_column] = df[main_column].fillna(missing_value)

    return df


def normalize_curves(
    df: pd.DataFrame, **kwargs
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, Dict[str, Any]]]:
    """
    Normalizes dataframe columns.

    We choose one well to be a "key well" and normalize all other wells to
    its low and high values. This process requires the kwarg 'id_column' to be
    passed so that wells can be grouped by their ID.

    For each curve to be normalized, high and low quantiles are calculated
    per well (the high and low percentage keyword arguments dictate this).

    If the user provides key wells, key wells calculation is not perfomed.

    Args:
        df (pd.DataFrame): dataframe with columns to normalize

    Keyword Args:
        curves_to_normalize (list): List of curves (column names) to normalize.
            Defaults to None (i.e. no curves being normalized).
        id_column (str): The name of the well ID column. This keyword argument
            **MUST** be provided to use this method.
        low_perc (float): low quantile to use as min value. Defaults to 5%
        high_perc (float): high quantile to use as max value. Defaults to 95%
        user_key_wells (dict): dictionary with curves as keys and min/max values
             and key well as values
        save_key_wells (bool): whether to save keys wells dictionary in
            folder_path. Defaults to False
        folder_path (str): The folder to save the key wells dictionary in.
            Defaults to "" so an error will be raised is saving is set to True
            but no folder_path is provided.

    Returns:
        tuple(pd.DataFrame, dict): pd.DataFrame with normalized values and dictionary with key wells
            that were used to normalize the curves_to_normalize
    """
    curves_to_normalize: Optional[List[str]] = kwargs.get("curves_to_normalize", None)
    id_column: Optional[str] = kwargs.get("id_column", None)
    low_perc: float = kwargs.get("low_perc", 0.05)
    high_perc: float = kwargs.get("high_perc", 0.95)
    user_key_wells: Optional[Dict[str, Dict[str, Union[str, float]]]] = kwargs.get(
        "user_key_wells", None
    )
    save_key_wells: bool = kwargs.get("save_key_wells", False)
    folder_path: str = kwargs.get("folder_path", "")

    if curves_to_normalize is not None:
        if id_column is None:
            id_column = "DUMMY_WELL_ID_COLUMN"
            df[id_column] = "UNKNOWN WELL"
            if user_key_wells is None:
                raise ValueError(
                    "Unable to normalize curves because no well ID column name was "
                    "provided and no user_key_wells were provided!"
                )
            else:
                logger.warning(
                    "No id column was provided. Perfoming normalization "
                    "by assuming all the data is one well!",
                    stacklevel=2,
                )

        # Calculate necessary quantiles for determining key wells and performing
        # normalization later on
        wells_data = df.loc[:, curves_to_normalize + [id_column]].groupby(id_column)
        high_quantiles = wells_data.quantile(high_perc)
        low_quantiles = wells_data.quantile(low_perc)

        if user_key_wells is None:
            # Need to determine key wells
            key_wells = (high_quantiles - low_quantiles).idxmax()
            # Convert key_wells into save format
            key_wells = {
                k: {
                    "curve": k,
                    "well_name": v,
                    "ref_low": low_quantiles[k][v],
                    "ref_high": high_quantiles[k][v],
                }
                for k, v in key_wells.to_dict().items()
            }
        else:
            # Check if key wells is provided as a dict with the same format
            if not isinstance(user_key_wells, dict):
                raise ValueError(
                    "Other methods to provide key wells are not implemented yet!"
                )
            if user_key_wells.keys() != set(curves_to_normalize):
                raise ValueError(
                    "Curves included in the key wells dictionary inconsistent with curves_to_normalize",
                    user_key_wells.keys(),
                    curves_to_normalize,
                )
            key_wells = user_key_wells

        # Normalize all wells
        for c in curves_to_normalize:
            key_well = key_wells[c]
            df.loc[:, "low_p"] = df[id_column].map(low_quantiles[c])
            df.loc[:, "high_p"] = df[id_column].map(high_quantiles[c])
            # normalize all other wells using key well as reference
            df.loc[:, c] = df.apply(
                lambda x: utilities.normalize(
                    x[c],  # noqa: B023
                    key_well["ref_low"],  # noqa: B023
                    key_well["ref_high"],  # noqa: B023
                    x["low_p"],
                    x["high_p"],
                ),
                axis=1,
            )

        # Perform post normalization cleanup
        df = df.drop(columns=["low_p", "high_p"])
        if id_column == "DUMMY_WELL_ID_COLUMN":
            df = df.drop(columns=[id_column])

        if save_key_wells:
            if folder_path:
                # save key wells to where model is
                joblib.dump(
                    key_wells,
                    Path(folder_path) / "key_wells.joblib",
                )
            else:
                raise ValueError(
                    "Save key wells was set to true but no folder_path kwarg was "
                    "passed to the method!"
                )

        return (df, {"user_key_wells": key_wells})
    else:
        logger.warning(
            "No curves were passed to curves_to_normalize so no normalization "
            "was performed!",
            stacklevel=2,
        )
        return df


def scale_curves(
    df: pd.DataFrame, **kwargs
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, Dict[str, BaseEstimator]]]:
    """
    Scales specified columns

    Args:
        df (pd.DataFrame): dataframe containing columns to scale

    Keyword Args:
        curves_to_scale (list): list of curves (column names) to scale
        scaler_method (str): string of any sklearn scalers. Defaults to RobustScaler
        scaler_kwargs (dict): dictionary of any kwargs to pass to the sklearn scaler
        scaler (BaseEstimator): a pre-fitted sklearn scaler object to apply directly
            to the curves_to_scale. If this kwarg is provided none of the other
            kwargs **BESIDES** curves_to_scale is needed.
        save_scaler (bool): whether to save scaler in folder_path or not. Defaults
            to False.
        folder_path (str): Which folder to save the scalers in. Defaults to no
            path so a path needs to be provided if the save_scaler kwarg is set
            to True.

    Returns:
        tuple(pd.DataFrame, dict): scaled columns and the scaler object that was used to scale the
            scaled columns stored in a dict.
    """
    curves_to_scale: Optional[List[str]] = kwargs.get("curves_to_scale", None)
    scaler_method: str = kwargs.get("scaler_method", "RobustScaler")
    scaler_kwargs: Dict[str, Any] = kwargs.get("scaler_kwargs", {})
    scaler: Optional[BaseEstimator] = kwargs.get("scaler", None)
    save_scaler: bool = kwargs.get("save_scaler", False)
    folder_path: str = kwargs.get("folder_path", "")

    if curves_to_scale is not None:
        if scaler is None:
            try:
                scaler = getattr(sklearn.preprocessing, scaler_method)
            except AttributeError as ae:
                raise ValueError(
                    "The requested scaler_method could not be found in the "
                    "sklearn.preprocessing library!"
                ) from ae
            scaler = scaler(**scaler_kwargs)
            scaler.fit(df[curves_to_scale])
            # save scaler to same path as model
            if save_scaler:
                if folder_path:
                    joblib.dump(
                        scaler,
                        Path(folder_path) / "scaler.joblib",
                    )
                else:
                    raise ValueError(
                        "Save_scaler was set to true but no folder_path kwarg was "
                        "passed to the method!"
                    )
        df.loc[:, curves_to_scale] = scaler.transform(df[curves_to_scale])

        return (df, {"scaler": scaler})

    return df


def process_wells(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Performs preprocessing per well

    This a convenience function that will perform several preprocessing steps
    per well if an id_column is provided in the kwargs. Otherwise it will treat
    the entire df as one well and preprocess it according to the same pipeline as
    the per well treatment.

    The preprocessing pipeline performed is as follows:

        1. imputation (if the 'imputer' kwarg is set)
        2. feature engineering:

            - Rolling features created using the add_rolling_features function
                (if the 'rolling_features' kwarg is set)
            - Gradient features created using the add_gradient_features function
                (if the 'gradient_features' kwarg is set)
            - Sequential features created using the add_sequential_features function
                (if the 'sequential_features' kwarg is set)

    The kwargs for each method discussed above must also be provided to this
    method. Please refer to the specific methods to determine which kwargs to
    provide

    Args:
        df (pd.DataFrame): dataframe of data to be preprocessed

    Keyword Args:
        id_column (str): The well ID column name to use to groupby well ID
        imputation_type (str): Which imputer to use. Can be one of the following two
            options:

                1. 'iterative' - runs the iterative_impute method from the
                    imputers module. Please refer to that method to read up on
                    all necessary kwargs to use that method properly
                2. 'simple' - runs the simple_impute method from the
                    imputers module. Please refer to that method to read up on
                    all necessary kwargs to use that method properly

    Returns:
        pd.Dataframe: dataframe of preprocessed data
    """

    def _preprocessing_pipeline(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        # Process kwargs to determine what to do
        imputation_type: str = kwargs.get("imputation_type", "")

        # impute features
        if imputation_type == "iterative":
            df, _ = imputers.iterative_impute(df, **kwargs)
        if imputation_type == "simple":
            df, _ = imputers.simple_impute(df, **kwargs)

        # add rolling features
        if "rolling_features" in kwargs:
            df = feature_engineering.add_rolling_features(df, **kwargs)

        # add gradient features
        if "gradient_features" in kwargs:
            df = feature_engineering.add_gradient_features(df, **kwargs)

        # add sequential features
        if "sequential_features" in kwargs:
            df = feature_engineering.add_sequential_features(df, **kwargs)

        return df

    id_column: Optional[str] = kwargs.get("id_column", None)
    # Process per well if id_column exists otherwise process as one big set
    if id_column in df.columns:
        well_names = df[id_column].unique()
        res_df = pd.DataFrame()
        for well in well_names:
            well_df = df.loc[df[id_column] == well, :].copy()
            well_df = _preprocessing_pipeline(well_df, **kwargs)
            res_df = pd.concat([res_df, well_df])
        df = res_df.copy()
    else:
        logger.warning(
            "Not possible to process per well as well ID is not in dataset. "
            "Preprocessing was done considering all data is from the same well.",
            stacklevel=2,
        )
        df = _preprocessing_pipeline(df, **kwargs)

    return df


def remove_noise(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    Removes noise by applying a median rolling window on each curve.

    Warning:
        Both kwargs are required for this function. If they are not provided,
        no noise filtering is performed and the df is returned untouched

    Args:
        df (pd.DataFrame): dataframe to which apply median filtering

    Keyword Args:
        noisy_curves (list): list of curves (columns) to apply noise removal with median filter
            if none are provided, median filtering will be applied to all
            numerical columns. Numerical columns are identified using the
            get_col_types utility function
        noise_removal_window (int): the window size to use when applying median filtering

    Returns:
        pd.DataFrame: dataframe after removing noise
    """
    # Processing inputs
    noisy_curves: Optional[List[str]] = kwargs.get("noisy_curves", None)
    noise_removal_window = kwargs.get("noise_removal_window")

    if noisy_curves is None:
        # Only interested in numerical columns so no need to flood console with
        # warnings related to categorical curves
        noisy_curves, _ = utilities.get_col_types(df, warn=False)
        logger.warning(
            "No noisy_curves were defined for the remove_noise function! "
            "Proceeding with removing noise in all detected numeric columns.",
            stacklevel=2,
        )

    if noise_removal_window is not None:
        df.loc[:, noisy_curves] = (
            df[noisy_curves]
            .rolling(noise_removal_window, center=True, min_periods=1)
            .median()
        )
    else:
        logger.warning(
            "No noise filtering was applied because one of the keyword arguments"
            " was not passed!",
            stacklevel=2,
        )

    return df


def apply_calibration(
    df_measured: pd.DataFrame,
    df_predicted: pd.DataFrame,
    curves: List[str],
    location_curves: List[str],
    level: str,
    mode: str,
    id_column: str,
    distance_thres: float = 9999.0,
    calib_map: Optional[pd.DataFrame] = None,
    standardize_level_names: bool = True,
) -> pd.DataFrame:
    """
    Applies calibration to predicted curves, removing biases with the help of measured
    curves, either in the same well or closest wells

    Args:
        df_measured (pd.DataFrame): original dataframe with measured values
        df_predicted (pd.DataFrame): datframe with predicted values, same column names
        curves (List[str]): curves to which apply calibration
        location_curves (List[str]): which curves to use for distance to get closest wells
        level (str): which grouping type to apply calibration (poer group, per formation)
        mode (str): type of value aggregation (mean, median, mode)
        id_column (str): well id
        distance_thres (float, optional): threshold for a well to be considered close enough.
        Defaults to 9999.0.
        calib_map (pd.DataFrame, optional): calibration map for the level. Defaults to None.
        standardize_level_names (bool optional): whether to standardize formation
        or group names. Defaults to True.

    Returns:
        pd.DataFrame: dataframe with calibrated values
    """
    # Make sure all necessary columns are in given dfs
    for df, df_name in zip(
        [df_measured, df_predicted, calib_map],
        ["df_measured", "df_predicted", "calibration map"],
        strict=False,
    ):
        missing_curves = [
            c
            for c in curves + location_curves + [level, id_column]
            if c not in df.columns
        ]
        if len(missing_curves) > 0:
            raise ValueError(
                f"Missing necessary curves in dataframe '{df_name}': {missing_curves}"
            )

    # either get calibration from cdf if None or work on given map
    if calib_map is None:
        # TODO get calibration map from CDF
        raise ValueError("Getting calibration map from CDF is not yet implemented!")

    # standardize level names if either group or formation
    if standardize_level_names and level in ["FORMATION", "GROUP"]:
        df_measured[level] = utilities.standardize_lsu_names(df_measured[level])
        df_predicted[level] = utilities.standardize_lsu_names(df_predicted[level])
        calib_map[level] = utilities.standardize_lsu_names(calib_map[level])

    calib_meas = utilities.get_calibration_values(
        df_measured,
        curves=curves,
        location_curves=location_curves,
        level=level,
        mode=mode,
        id_column=id_column,
        distance_thres=distance_thres,
        calibration_map=calib_map,
    )
    calib_pred = utilities.get_calibration_values(
        df_predicted,
        curves=curves,
        location_curves=location_curves,
        level=level,
        mode=mode,
        id_column=id_column,
        distance_thres=distance_thres,
        calibration_map=calib_map,
    )

    df_calibrated = df_predicted.copy()
    for well in df_predicted[id_column].unique():
        logger.info(well)
        df_m = df_predicted[df_predicted[id_column] == well]
        for c in curves:
            diffs = {
                i: calib_pred[well][c][i] - calib_meas[well][c][i]
                for i in df_m[level].unique()
            }
            for g, v in diffs.items():
                if np.isnan(v):
                    continue
                df_calibrated.loc[
                    (df_calibrated[level] == g) & (df_calibrated[id_column] == well), c
                ] = (
                    df_calibrated.loc[
                        (df_calibrated[level] == g)
                        & (df_calibrated[id_column] == well),
                        c,
                    ]
                    - v
                )
    return df_calibrated
