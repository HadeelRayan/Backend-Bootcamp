import json
import os


class SiteDataError(Exception):
    """Custom exception for site data errors."""
    pass


def load_sites_data(json_file_path):
    """Load site data from a JSON file.

    Args:
        json_file_path (str): Path to the JSON file containing sites data.

    Returns:
        dict: A dictionary containing the sites data.

    Raises:
        SiteDataError: If the file cannot be read or data is invalid.
    """
    if not os.path.exists(json_file_path):
        raise SiteDataError(f"File not found: {json_file_path}")

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            sites_data = json.load(file)
    except Exception as e:
        raise SiteDataError(f"Failed to load or parse the sites data file: {e}")

    if not isinstance(sites_data, dict):
        raise SiteDataError("Sites data is not in expected format (expected a dictionary).")

    return sites_data


def get_site_info(sites_data, site_name):
    """Retrieve information for a specific site.

    Args:
        sites_data (dict): The loaded sites data dictionary.
        site_name (str): The name of the site to retrieve information for.

    Returns:
        dict: A dictionary containing the site information.

    Raises:
        KeyError: If the site name is not found in the sites data.
    """
    return sites_data[site_name]
