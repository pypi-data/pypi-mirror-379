import os
import docker
from datetime import datetime
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def download_volume(volume_name: str, output_path: str):
    client = docker.from_env()

    # Create a temporary container with the volume mounted
    container = client.containers.run(
        "alpine",  # lightweight base image
        "sleep 5",  # keep it alive long enough to copy
        detach=True,
        volumes={volume_name: {"bind": "/data", "mode": "ro"}}
    )

    # Create tarball of /data inside the container
    bits, stat = container.get_archive("/data")

    # Ensure output filename
    if os.path.isdir(output_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_path, f"{volume_name}_{timestamp}.tar.gz")
    else:
        output_file = output_path

    # Write the tar stream to file
    with open(output_file, "wb") as f:
        for chunk in bits:
            f.write(chunk)

    container.remove(force=True)
    client.close()

    return output_file


"""This Function Upload Docker Volumes to google drive"""
def upload_to_drive(file_path: str, conf_path: str, folder_id: str = None) -> str:
    gauth = GoogleAuth()

    # Detect if config is a service account
    import json
    with open(conf_path) as f:
        conf = json.load(f)

    if conf.get("type") == "service_account":
        gauth.settings["service_config"] = {
            "client_user_email": conf["client_email"],
            "client_json_file_path": conf_path
        }
        gauth.ServiceAuth()
    else:
        gauth.LoadClientConfigFile(conf_path)
        gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"title": os.path.basename(file_path)})
    if folder_id:
        file["parents"] = [{"id": folder_id}]
    file.SetContentFile(file_path)
    file.Upload()

    return f"https://drive.google.com/file/d/{file['id']}/view"
