import requests

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
        events = response.json()
        if not events:
            print("No recent activity found.")
            return
        
        print(f"Recent activity for GitHub user '{username}':\n")
        for event in events[:10]:  # Displaying the latest 10 events
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            created_at = event["created_at"]
            print(f"- [{created_at}] {event_type} in {repo_name}")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    fetch_github_activity(username)
