import sys
import subprocess
import argparse
import time

def buildDocker():
    print("\nBuilding Docker Image")
    subprocess.run("docker build --no-cache -t doombox .", shell=True)

# Define container_id and ip_address as global variables
container_id = None
ip_address = None

def runDocker():
    global container_id, ip_address  # Declare them as global inside the function

    container_id = subprocess.getoutput("docker ps -aqf name=doombox_container")

    print("\nRunning Docker Image")
    # Check if the container exists
    if container_id:
        # If it exists, remove it
        subprocess.Popen(f"docker rm -f {container_id}", stdout=subprocess.PIPE, shell=True)
        time.sleep(3)
    # Start a new container
    subprocess.Popen("docker run -d --name doombox_container -p 8080:8080 doombox", stdout=subprocess.PIPE, shell=True)
    print("Initialising...")
    time.sleep(3)  # Wait for 10 seconds

    # Update container_id and ip_address
    ip_address = subprocess.getoutput("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' doombox_container")

    print(f"\nDocker container is running at IP address: {ip_address}")

def stopDocker():
    global container_id 
    container_id = subprocess.getoutput("docker ps -aqf name=doombox_container")
    
    if container_id:
        print("\nStopping Docker Container: ", container_id)
        subprocess.call("docker stop doombox_container", stdout=subprocess.PIPE, shell=True)
        subprocess.call(f"docker rm -f {container_id}", stdout=subprocess.PIPE, shell=True)
    else:
        print("\nNo DoomBox docker present")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--destroy", help="Close the Docker container", action="store_true")
    args = parser.parse_args()

    if args.destroy:
        stopDocker()
    else:
        buildDocker()
        runDocker()
        print(f"\nServer is running on http://{ip_address}:8080")

if __name__ == "__main__":
    main()
sys.exit(0)