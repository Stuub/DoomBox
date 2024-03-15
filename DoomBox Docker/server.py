import sys
import subprocess
import argparse
import time

# Class to encapsulate the Docker container operations
class DockerContainer:
    def __init__(self):
        # Initialize container_id and ip_address
        self.container_id = None
        self.ip_address = None

    def build(self):
        # Build the Docker image
        print("\nBuilding Docker Image")
        subprocess.run("docker build --no-cache -t doombox .", shell=True)

    def run(self):
        # Get the container_id of the existing Docker container
        self.container_id = subprocess.getoutput("docker ps -aqf name=doombox_container")

        print("\nRunning Docker Image")
        # Check if the container exists
        if self.container_id:
            # If it exists, remove it
            subprocess.Popen(f"docker rm -f {self.container_id}", stdout=subprocess.PIPE, shell=True)
            time.sleep(3)
        # Start a new container
        subprocess.Popen("docker run -d --name doombox_container -p 80:80 doombox", stdout=subprocess.PIPE, shell=True)
        print("Initialising...")
        time.sleep(10)  # Wait for the Docker container to initialize

        # Update container_id and ip_address
        self.ip_address = subprocess.getoutput("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' doombox_container")

        print(f"\nDocker container is running at IP address: {self.ip_address}")

    def stop(self):
        # Get the container_id of the existing Docker container
        self.container_id = subprocess.getoutput("docker ps -aqf name=doombox_container")

        if self.container_id:
            # If the container exists, stop and remove it to prevent conflicts
            print("\nStopping Docker Container: ", self.container_id)
            subprocess.call("docker stop doombox_container", stdout=subprocess.PIPE, shell=True)
            subprocess.call(f"docker rm -f {self.container_id}", stdout=subprocess.PIPE, shell=True)
        else:
            print("\nNo DoomBox docker present")

def main():
    # Handle user command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--destroy", help="Close the Docker container", action="store_true")
    args = parser.parse_args()

    # Create a DockerContainer object
    container = DockerContainer()

    if args.destroy:
        # If the --destroy option is specified, stop the Docker container
        container.stop()
    else:
        # Otherwise, build and run the Docker container
        container.build()
        container.run()
        print(f"\nServer is running on http://{container.ip_address}:8080")

if __name__ == "__main__":
    # If the script is run directly, call the main() function
    main()

sys.exit(0)