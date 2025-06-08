import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.cwa.gov.tw/V8/C/M/Fishery/tide_30day_MOD/T902001.html"
TARGET_NAME = "金城"  # 抓金門縣金城的潮汐資料

def fetch_kinmen_tide():
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 找到日期區塊與潮汐時間
    rows = soup.select("table tr")[1:]  # 跳過標題
    result = []
    for tr in rows:
        cols = [c.get_text(strip=True) for c in tr.find_all("td")]
        if len(cols) >= 6 and TARGET_NAME in cols[0]:
            # 解析：cols 含 日期、農曆、潮差說明、乾潮1 & 時間、滿潮1 & 時間、乾潮2 & 時間、滿潮2 & 時間
            date, lunar, _, low1, low1_t, high1, high1_t, low2, low2_t, high2, high2_t = (
                cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7], cols[8], cols[9], cols[10]
            )
            result.append({
                "date": date,
                "lunar": lunar,
                "low1_time": low1_t,
                "low1_val": low1,
                "high1_time": high1_t,
                "high1_val": high1,
                "low2_time": low2_t,
                "low2_val": low2,
                "high2_time": high2_t,
                "high2_val": high2
            })
    return result

def print_tide(data):
    for d in data:
        print(f"📅 {d['date']} ({d['lunar']}):")
        print(f"  乾潮1 {d['low1_time']} 值 {d['low1_val']}")
        print(f"  滿潮1 {d['high1_time']} 值 {d['high1_val']}")
        print(f"  乾潮2 {d['low2_time']} 值 {d['low2_val']}")
        print(f"  滿潮2 {d['high2_time']} 值 {d['high2_val']}")
        print()

if __name__ == "__main__":
    try:
        tides = fetch_kinmen_tide()
        if tides:
            print(f" 潮汐資訊：金門縣金城（共{len(tides)}天資料）\n")
            print_tide(tides[:5])  # 只顯示前 5 天
        else:
            print("找不到金城站點的資料")
    except Exception as e:
        print(" 錯誤：", e)


