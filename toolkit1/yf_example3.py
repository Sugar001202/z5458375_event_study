"""
Module: yf_example3.py

Purpose: Downloads stock price data for Qantas for a specified year and saves the information to a CSV file.
"""

import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year) :
    """
    Downloads Qantas stock prices for a given year and saves the data to a CSV file.

    Parameters:
    - year: Integer, the year for which stock prices should be downloaded.
    """
    # Define the period for the given year
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    # File name and path setup
    file_name = f"qan_prc_{year}.csv"
    file_path = os.path.join(cfg.DATA_DIR, file_name)

    # Downloading the data using yf_example2's yf_prc_to_csv function
    yf_example2.yf_prc_to_csv(tic='QAN.AX', start_date=start_date, end_date=end_date, file_path=file_path)


if __name__ == "__main__" :
    # Test case: Download Qantas stock price data for the year 2020
    qan_prc_to_csv(2020)
