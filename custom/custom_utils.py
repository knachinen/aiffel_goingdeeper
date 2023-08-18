import pickle
import logging
import os
import datetime

def ensure_directory_exists(directory: str) -> None:
    """
    Ensures a directory exists, creates it if it doesn't.

    Parameters:
    - directory: The directory path.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_var(var, name: str = "var") -> None:
    """
    Saves a variable to a pickle file.
    
    Parameters:
    - var: The variable to be saved.
    - name (optional): The name of the pickle file (without extension). Defaults to "var".
    """
    ensure_directory_exists('save')
    file_path = os.path.join('save', f'{name}.pkl')
    
    # Check if the file already exists
    if os.path.exists(file_path):
        # Rename it by appending the current timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        new_name = f"{name}_{timestamp}.pkl"
        new_file_path = os.path.join('save', new_name)
        os.rename(file_path, new_file_path)
        logging.info(f'Renamed existing file to: {new_file_path}')

    try:
        with open(file_path, 'wb') as f:
            pickle.dump(var, f)
            
        file_size = os.path.getsize(file_path) / (1024 ** 2)  # Get size in MB
        logging.info(f'Saved: {file_path} (Size: {file_size:.2f} MB)')
    except Exception as e:
        logging.error(f"Error saving variable to {file_path}: {e}")

def load_var(name: str = "var"):
    """
    Loads a variable from a pickle file.
    
    Parameters:
    - name (optional): The name of the pickle file (without extension). Defaults to "var".
    
    Returns:
    - Loaded variable.
    """
    ensure_directory_exists('save')
    file_path = os.path.join('save', f'{name}.pkl')
    
    try:
        with open(file_path, 'rb') as f:
            var = pickle.load(f)
        
        file_size = os.path.getsize(file_path) / (1024 ** 2)  # Get size in MB
        logging.info(f'Loaded: {file_path} (Size: {file_size:.2f} MB)')
        return var
    except Exception as e:
        logging.error(f"Error loading variable from {file_path}: {e}")
        return None
