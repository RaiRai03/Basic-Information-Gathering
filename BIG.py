def get_ip_info(host):
    # Simulated IP address mapping for demonstration
    ip_mapping = {
        "example.com": "93.184.216.34",
        "localhost": "127.0.0.1",
        "openai.com": "104.18.1.0",
        "google.com": "172.217.0.0"
    }
    
    # Retrieve the IP address based on the hostname
    ip = ip_mapping.get(host)
    
    # Provide detailed output
    if ip:
        print(f"Hostname: {host}")
        print(f"IP address: {ip}")
        print("This IP address is associated with the specified hostname.")
    else:
        print("Hostname could not be resolved.")
        print("Please check the hostname or try a different one.")

# User Input
host = input("Enter the hostname: ")
get_ip_info(host)