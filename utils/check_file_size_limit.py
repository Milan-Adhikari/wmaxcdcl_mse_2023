import os
FILE_SIZE_LIMIT = 5 * 1024 * 1024  # 5 MB

def validate_file_size_exceeded(file_path: str) -> bool:
    """
    Validate the size of a file.

    Parameters
    ----------
    file_path : str
        The path to the file.

    Returns
    -------
    bool
        True if the file size is within the limit, False otherwise.
    """
    if FILE_SIZE_LIMIT is None:
        return False
    file_size = os.stat(file_path).st_size
    if file_size > FILE_SIZE_LIMIT:
        return True
    return False
