import chardet

def detect_csv_encoding(file_path):
    # Open the file in binary mode to read bytes
    with open(file_path, 'rb') as f:
        # Read a reasonable sample size (e.g., the first 10,000 bytes)
        # to make a reliable guess without reading the whole file
        raw_data = f.read(10000) 
        result = chardet.detect(raw_data)
        return result['encoding']

file_path = 'D:\HANDS ON\DATA\ML Algorithms\Global_Sales_Messy_Data.csv'
detected_encoding = detect_csv_encoding(file_path)
print(f"Detected encoding: {detected_encoding}")
