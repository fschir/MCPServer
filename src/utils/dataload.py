import pandas as pd
import numpy as np
import ftplib
import os
import tempfile
from typing import List, Dict, Any
import logging
from dataclasses import dataclass

@dataclass
class FTPConfig:
    server: str = "opendata.dwd.de"
    base_path: str = "/weather/weather_reports/poi/"
    username: str = "anonymous"
    password: str = "anonymous"


def fetch_files_from_ftp(ftp_config: FTPConfig, local_dir: str) -> List[str]:

    files = []
    with ftplib.FTP(ftp_config.server) as ftp:
        ftp.login(ftp_config.username, ftp_config.password)
        ftp.cwd(ftp_config.base_path)
        ftp.retrlines('NLST', files.append)
        for file in files:
            local_path = os.path.join(local_dir, file)
            try:
                with open(local_path, 'wb') as local_file:
                    ftp.retrbinary(f'RETR {file}', local_file.write)
            except ftplib.all_errors as e:
                logging.error(f"FTP error downloading file {file}: {e}")
    
    if not files:
        raise ValueError("No files found in FTP directory.")
    return files


        
        
    

    


if __name__ == "__main__":
    ftp_config = FTPConfig()
    fetch_files_from_ftp(ftp_config, f"{os.getcwd()}/data")
    print(os.getcwd())