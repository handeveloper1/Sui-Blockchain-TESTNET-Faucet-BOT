import requests
from concurrent.futures import ThreadPoolExecutor
import random



oglist = [
"0xeee4ad07a4102a73b61544b4d2b5eab8dec2542dc8cb7f3a33036089a6382d66"
]



def send_request():
    wallet = random.choice(oglist)

    url = 'https://faucet.testnet.sui.io/v1/gas'
    headers = {
        "Sec-Ch-Ua-Platform": "\"Windows\"",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
                     "Sec-Ch-Ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"", "Content-Type": "application/json",
                     "Sec-Ch-Ua-Mobile": "?0", "Accept": "*/*",
                     "Origin": "chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil", "Sec-Fetch-Site": "none",
                     "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate, br",
                     "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i"}
    data = {
        "FixedAmountRequest": {
            "recipient": wallet
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"{wallet} - {response.status_code} | Response: {response.json()}")



def main():
    with ThreadPoolExecutor(max_workers=30) as executor:
        try:
            while True:

                executor.submit(send_request)
        except KeyboardInterrupt:
            print("Shutting down...")


# Run the main function
if __name__ == "__main__":
    main()
