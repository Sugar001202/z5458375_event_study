import yfinance as yf

def yf_prc_to_csv(tic, start_date, end_date, file_path):
    # 你的代码逻辑，使用yfinance下载股票数据并保存到CSV文件
    data = yf.download(tic, start=start_date, end=end_date)
    data.to_csv(file_path)
