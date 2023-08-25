import requests
def get_random_activity():
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url)
    data = response.json()
    activity = data.get("activity")
    return activity

def main():
    print("Welcome! Let me suggest an activity for you:")
    activity = get_random_activity()
    print("How about:", activity)

if __name__ == "__main__":
    main()