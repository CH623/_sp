import requests
from bs4 import BeautifulSoup

URL = "https://www.cwa.gov.tw/V8/C/M/Fishery/tide_30day_MOD/T902001.html"
TARGET_NAME = "金城" 

def fetch_kinmen_tide():
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    rows = soup.select("table tr")[1:]  
    result = []

    for tr in rows:
        cols = [c.get_text(strip=True) for c in tr.find_all("td")]
        if not cols:
            continue
        if TARGET_NAME in cols[0]:
            
            def get_col(i):
                return cols[i] if i < len(cols) else ""

            date = get_col(0)
            lunar = get_col(1)

            low1_val = get_col(3)
            low1_time = get_col(4)
            high1_val = get_col(5)
            high1_time = get_col(6)
            low2_val = get_col(7)
            low2_time = get_col(8)
            high2_val = get_col(9)
            high2_time = get_col(10)

            result.append({
                "date": date,
                "lunar": lunar,
                "low1_time": low1_time,
                "low1_val": low1_val,
                "high1_time": high1_time,
                "high1_val": high1_val,
                "low2_time": low2_time,
                "low2_val": low2_val,
                "high2_time": high2_time,
                "high2_val": high2_val
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
            print(f"潮汐資訊：金門縣金城\n")
            print_tide(tides[:10])  
        else:
            print("找不到金城站點的資料")
    except Exception as e:
        print(" 錯誤：", e)
