import pandas as pd
import requests
from pandas import json_normalize
import json
import numpy as np
import os
import sys
import statsmodels.api as sm
import seshatdatasetanalysis as sda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def download_data(url, size = None):
    
    if pd.isna(size):
        url = url
    elif isinstance(size, int):
        url = url+"?page_size="+str(size)
    df = pd.DataFrame()
    
    n_timeout = 0
    
    while True:
        try:
            try:
                response = requests.get(url, timeout=20)
            except requests.exceptions.Timeout:
                # print("Timeout occurred")
                n_timeout += 1
                if n_timeout > 10:
                    print(f"10th timeout when downloading {url}; giving up")
                    return pd.DataFrame()
                continue
            if not response.ok:
                print(f"Error downloading data from {url}: {response.status_code}")
                return pd.DataFrame()
            
            data = response.json()
            
            for polity_dict in data['results']:

                # unpack polity_dict
                flattened_dict = json_normalize(polity_dict, sep='_')
                df = pd.concat([df, flattened_dict], axis=0)

            url = data['next']
            if url is None:
                # got to the end of the dataset
                print(f"Downloaded {len(df)} rows")
                return df

        except:
            return pd.DataFrame()

def download_data_json(filepath):

    data = json.load(open(filepath))
    df = pd.DataFrame()
    for row in data:
        # unpack polity_dict
        flattened_dict = json_normalize(row, sep='_')
        df = pd.concat([df, flattened_dict], axis=0)
    return df

def fetch_urls(category):
    url = "https://seshat-db.com/api/"
    response = requests.get(url)
    data = response.json()
    variable_urs = dict()
    import seshatdatasetanalysis.mappings as mappings
    if category == 'wf':
        mapping = mappings.miltech_mapping_api
        api_category = 'wf'
    elif category == 'sc':
        mapping = mappings.social_complexity_mapping_api
        api_category = 'sc'
    elif category == 'id':
        mapping = mappings.ideology_mapping_api
        api_category = 'id'
    elif category == 'rt':
        mapping = mappings.ideology_mapping_api
        api_category = 'rt'
    elif category == 'ec':
        mapping = mappings.luxury_mapping_api
        api_category = 'ec'
    elif category == 'rel':
        mapping = mappings.religion_mapping_api
        api_category = 'general'

    used_keys = []
    for key in mapping.keys():
        used_keys.append(mapping[key].keys())
    used_keys = [api_category+'/'+key for sublist in used_keys for key in sublist]
    for key in data.keys():
        if key.split('/')[0] == api_category:
            if key in used_keys:
                variable_urs[key] = data[key]
    return variable_urs


def weighted_mean(row, mappings, category = "Metal", nan_handling = 'remove', min_vals = 0., allow_missing = False):
    keys = mappings[category].keys()
    
    for key in keys:
        if key not in row:
            if key + "_from" in row:
                row[key] = (row[key + "_from"] + row[key + "_to"]) / 2
            else:
                if not allow_missing:
                    print(key, "not in row")
    
    if allow_missing:
        keys = list(x for x in keys if x in row.index)
        if len(keys) == 0:
            raise BaseException('No values to aggregate!')
    
    entries = [mappings[category][key] for key in keys]

    values = row[keys]
    if values.isna().sum() >= len(values)*(1-min_vals):
        return np.nan
    
    if nan_handling == 'remove':
        entries = [entry for entry, value in zip(entries, values) if not np.isnan(value)]
        values = values.dropna()
    elif nan_handling == 'mean':
        values = values.infer_objects()
        values = values.fillna(values.mean())
        entries = [entry for entry, value in zip(entries, values) if not np.isnan(value)]
    elif nan_handling == 'zero':
        values = values.infer_objects()
        values = values.fillna(0)
        entries = [entry for entry, value in zip(entries, values) if not np.isnan(value)]
    elif nan_handling == 'half':
        values = values.infer_objects()
        values = values.fillna(0.5)
    
        entries = [entry for entry, value in zip(entries, values) if not np.isnan(value)]
    
    return np.average(values, weights = entries)


def get_max(row, mappings, category, allow_missing = False):

    result = -1
    for key, entry in mappings[category].items():
        if key not in row:
            if key + "_from" in row:
                if np.isnan(row[key + "_from"]):
                    continue
                value = (row[key + "_from"] + row[key + "_to"]) / 2
            else:
                if not allow_missing:
                    print(key, "not in row")
                continue
        else:
            if np.isnan(row[key]):
                continue
            value = row[key]
        if entry * value > result:
            result = entry * value

    if result == -1:
        result = np.nan
    return result

def convert_to_year(year_str):
    """Convert string of the type '1000CE' or '1000BCE' to integer, any non string is returned as is"""
    # check if str
    if type(year_str) != str:
        return year_str
    if 'BCE' in year_str:
        return -int(year_str.split('B')[0])
    elif 'CE' in year_str:
        return int(year_str.split('C')[0])
    
def is_same(list1,list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] not in list2:
            return False
    return True

def convert_to_year(year_str):
    """Convert string of the type '1000CE' or '1000BCE' to integer, any non string is returned as is"""
    # check if str
    if type(year_str) != str:
        return year_str
    if 'BCE' in year_str:
        return -int(year_str.split('B')[0])
    elif 'CE' in year_str:
        return int(year_str.split('C')[0])


def compare(old, new, common_columns):
    # check if two have same entries
    for col in common_columns:
        if col == 'polityname' or col == 'year':
            continue
            # remove nan values
        old_col = old[col].dropna()
        new_col = new[col].dropna()
        if len(old_col) == 0 and len(new_col) == 0:
            print("no values for", col)
            continue
        if len(old_col) != len(new_col):
            print("different lengths for", col)
            print("old data")
            print(old_col)
            print("new data")
            print(new_col)
            print("\n\n")
            continue
        if not (old_col.values == new_col.values).all():
            print("same values for", col)

            continue

def standardize_column(df, column_name):
    """
    Check if all values in a column are the same. If not, set all values to the most common value.
    
    Parameters:
        df (pandas.DataFrame): The dataframe to modify
        column_name (str): The name of the column to check and potentially standardize
        
    Returns:
        pandas.DataFrame: The modified dataframe
    """
    # Check if column exists
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in dataframe")
        return df
        
    # Get unique values
    unique_values = df[column_name].unique()
    
    # If there's only one unique value (or column is empty), nothing needs to be done
    if len(unique_values) <= 1:
        print(f"All values in '{column_name}' are the same. No changes needed.")
        return df
        
    # Get the most common value using value_counts()
    most_common = df[column_name].value_counts().idxmax()
    
    print(f"Values in '{column_name}' differ. Setting all to most common value: {most_common}")
    
    # Make a copy to avoid modifying the original
    result_df = df.copy()
    result_df[column_name] = most_common
    
    return result_df

def longest_substring_finder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp] == string2[j+lcs_temp]):
                match += string2[j+lcs_temp]
                lcs_temp += 1
            if len(match) > len(answer):
                answer = match
    return answer


def fit_logit_to_variables(df, y_col, x_cols, p_max = 0.05, print_all = False):

    best_fit_found = False
    while not best_fit_found:
        Xy = df[x_cols + [y_col]].dropna()
        if len(Xy) < 2:
            print("Not enough data to fit model")
            return None
        if len(x_cols) == 0:
            print("No variables are significant")
            return None
        X = Xy[x_cols]
        y = Xy[y_col].round().astype(int)
        X = sm.add_constant(X)
        model = sm.Logit(y, X).fit()
        
        if model.pvalues[1:].max() < p_max:
            best_fit_found = True
            print("Best fit found")
            print(model.summary())
            print(model.pvalues)
            return model
            break
        
        if print_all:
            print(model.summary())
            print(model.pvalues)
        # Remove the variable with the highest p-value
        x_cols.remove(model.pvalues[1:].idxmax())
        print(f"Removing {model.pvalues[1:].idxmax()} with p-value {model.pvalues[1:].max()}")


def fit_linear_to_variables(df, y_col, x_cols, p_max = 0.05, print_all = False):

    best_fit_found = False
    while not best_fit_found:
        Xy = df[x_cols + [y_col]].dropna()
        if len(Xy) < 2:
            print("Not enough data to fit model")
            return None
        if len(x_cols) == 0:
            print("No variables are significant")
            return None
        X = Xy[x_cols]
        y = Xy[y_col]
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        
        if model.pvalues[1:].max() < p_max:
            best_fit_found = True
            print("Best fit found")
            print(model.summary())
            print(model.pvalues)
            return model
            break
        
        if print_all:
            print(model.summary())
            print(model.pvalues)
        # Remove the variable with the highest p-value
        x_cols.remove(model.pvalues[1:].idxmax())
        print(f"Removing {model.pvalues[1:].idxmax()} with p-value {model.pvalues[1:].max()}")

def bin_data_1D(tsd, col,  nbins = None, grid_size = 1, error = 'standard'):
    """
    Bin data in a single column into specified bins and calculate the mean and error for each bin.
    
    Parameters:
        tsd (seshatdatasetanalysis.TimeSeriesDataset or pandas.DataFrame): The dataset containing the data to bin.
        col (str): The name of the column to bin.
        bins (list): List of bin edges.
        error (str): Type of error to calculate ('standard' or 'sem').
        
    Returns:
        pandas.DataFrame: DataFrame with binned data, mean, and error.
    """
    if isinstance(tsd, sda.TimeSeriesDataset):
        df = tsd.scv_imputed
    elif isinstance(tsd, pd.DataFrame):
        df = tsd
    else:
        raise TypeError("tsd must be a TimeSeriesDataset or a pandas DataFrame")
    
    xlims = (df[col].min(), df[col].max())
    if (nbins is None) and (grid_size is None):
        nbins = 10
        grid_size = (xlims[1] - xlims[0]) // nbins
    elif (nbins is not None) and (grid_size is None):
        grid_size = (xlims[1] - xlims[0]) // nbins
    elif (nbins is None) and (grid_size is not None):
        nbins = (xlims[1] - xlims[0]) // grid_size
    nbins = int(nbins)
    bins = np.linspace(xlims[0], xlims[1], nbins + 1)
    binned_data = pd.cut(df[col], bins=bins)
    grouped = df.groupby(binned_data).agg({col: ['mean', 'count']})
    
    if error == 'standard':
        grouped['error'] = df.groupby(binned_data)[col].std()
    elif error == 'sem':
        grouped['error'] = df.groupby(binned_data)[col].sem()
    
    return grouped.reset_index()

def bin_data_2D(tsd, col_x, col_y, nbins = None, grid_size = 1, error = 'standard'):
    """
    Bin data in two columns into specified bins and calculate the mean and error for each bin.
    
    Parameters:
        tsd (seshatdatasetanalysis.TimeSeriesDataset or pandas.DataFrame): The dataset containing the data to bin.
        col_x (str): The name of the first column to bin.
        col_y (str): The name of the second column to bin.
        nbins (tuple or int, optional): Number of bins for each dimension. If int, same number of bins is used for both dimensions.
        grid_size (int, optional): Size of each bin in the grid.
        error (str): Type of error to calculate ('standard' or 'sem').
        
    Returns:
        pandas.DataFrame: DataFrame with binned data, mean, and error.
    """
    if isinstance(tsd, sda.TimeSeriesDataset):
        df = tsd.scv_imputed
    elif isinstance(tsd, pd.DataFrame):
        df = tsd
    else:
        raise TypeError("tsd must be a TimeSeriesDataset or a pandas DataFrame")
    
    xlims = (df[col_x].min(), df[col_x].max())
    ylims = (df[col_y].min(), df[col_y].max())
    if (nbins is None) and (grid_size is None):
        nbins = (10, 10)
    elif (nbins is not None) and (grid_size is None):
        if isinstance(nbins, int):
            nbins = (nbins, nbins)
        elif len(nbins) == 1:
            nbins = (nbins[0], nbins[0])
        elif len(nbins) != 2:
            raise ValueError("nbins must be an int or a tuple of two ints.")
        grid_size = (x_bins[1] - x_bins[0], y_bins[1] - y_bins[0])
    elif grid_size is not None:
        nbins = ((xlims[1] - xlims[0]) // grid_size, (ylims[1] - ylims[0]) // grid_size)
    nbins = (int(nbins[0]), int(nbins[1]))
    x_bins = np.linspace(xlims[0], xlims[1], nbins[1] + 1)
    y_bins = np.linspace(ylims[0], ylims[1], nbins[0] + 1)

    binned_data = pd.cut(df[col_x], bins=x_bins)
    binned_data_y = pd.cut(df[col_y], bins=y_bins)
    grouped = df.groupby([binned_data, binned_data_y]).agg({col_x: ['mean', 'count'], col_y: ['mean']})
    
    if error == 'standard':
        grouped['error'] = df.groupby([binned_data, binned_data_y])[col_x].std()
    elif error == 'sem':
        grouped['error'] = df.groupby([binned_data, binned_data_y])[col_x].sem()
    
    return grouped.reset_index()
