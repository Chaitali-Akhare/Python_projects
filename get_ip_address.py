import socket

def get_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        return ip_address
    except socket.gaierror:
        return "Unable to get IP Address...."

website_url = input("Enter Website URL: ")
ip_address = get_ip_address(website_url)
print("The IP address of {} is : {}".format(website_url, ip_address))
