import requests

def get_public_ip():
    url = "https://api.ipify.org/?format=json"
    response = requests.get(url)
    data = response.json()
    public_ip = data.get("ip")
    return public_ip




def main():
    public_ip = get_public_ip()
    print("Your Public IP:", public_ip)

   

if __name__ == "__main__":
    main()