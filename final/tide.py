import requests
from bs4 import BeautifulSoup

URL = "https://www.cwa.gov.tw/V8/C/Tide/TideData/T902001.htm"
TARGET_STATION = "金城"

def fetch_kinmen_tide_stable():
    resp = requests.get(URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 找表格（觀察後該頁只有一個主要表格）
    table = soup.find("table")
    if not table:
        print("找不到潮汐資料表格")
        return None

    rows = table.find_all("tr")

    data = []
    for tr in rows[1:]:  # 跳過標題列
        cols = [td.get_text(strip=True) for td in tr.find_all("td")]
        # 觀察此表的欄位順序與意義
        # 範例欄位：日期, 農曆, 乾潮1時間, 乾潮1高度, 滿潮1時間, 滿潮1高度, 乾潮2時間, 乾潮2高度, 滿潮2時間, 滿潮2高度
        if len(cols) < 10:
            continue
        # 此網頁是只針對金城站資料
        data.append({
            "日期": cols[0],
            "農曆": cols[1],
            "乾潮1時間": cols[2],
            "乾潮1高度": cols[3],
            "滿潮1時間": cols[4],
            "滿潮1高度": cols[5],
            "乾潮2時間": cols[6],
            "乾潮2高度": cols[7],
            "滿潮2時間": cols[8],
            "滿潮2高度": cols[9],
        })

    return data

def print_tide(data):
    if not data:
        print("找不到金城站的潮汐資料")
        return
    print(f"金門縣金城潮汐資料，共 {len(data)} 天")
    for day in data[:5]:  # 印前五筆
        print(f"日期: {day['日期']} (農曆 {day['農曆']})")
        print(f"  乾潮1：{day['乾潮1時間']}，高度 {day['乾潮1高度']}")
        print(f"  滿潮1：{day['滿潮1時間']}，高度 {day['滿潮1高度']}")
        print(f"  乾潮2：{day['乾潮2時間']}，高度 {day['乾潮2高度']}")
        print(f"  滿潮2：{day['滿潮2時間']}，高度 {day['滿潮2高度']}")
        print()

if __name__ == "__main__":
    try:
        tide_data = fetch_kinmen_tide_stable()
        print_tide(tide_data)
    except Exception as e:
        print("錯誤:", e)

