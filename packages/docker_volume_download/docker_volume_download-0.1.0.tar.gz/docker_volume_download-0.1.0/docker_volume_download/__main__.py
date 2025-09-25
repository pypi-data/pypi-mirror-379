import argparse
from docker_volume_download import download_volume, upload_to_drive
from .config import save_config, load_conf_path
import os


def main():
    parser = argparse.ArgumentParser(description="Download Docker volume and optionally upload to Google Drive")
    parser.add_argument("-d", "--download", nargs=2, metavar=("VOLUME", "LOCATION"),
                        help="Download <VOLUME> into <LOCATION>")
    parser.add_argument("-u", "--upload", action="store_true",
                        help="Upload the created tar.gz file to Google Drive")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--conf", "-c", type=str,
                        help="Path to Google API service account credentials.json")
    parser.add_argument("--folder", "-f", type=str,
                        help="Path to Google Drive folder")


    args = parser.parse_args()

    if args.version:
        from importlib.metadata import version
        print(version("docker_volume_download"))
        return

    if args.conf or args.folder:
        if args.conf:
            if not os.path.exists(args.conf):
                print(f"❌ Provided config file does not exist: {args.conf}")
                return
            save_config(conf_path=args.conf)

        elif args.folder:
            save_config(folder_id=args.folder)
        print(f"⚙️ Configuration saved: {args.conf or args.folder}")
        return


    # GET conf File Value
    conf_path = load_conf_path("conf_path")
    if not conf_path:
        print("❌ No configuration found. Use --conf or -c <path> to set credentials.")
        return

    # GET conf Folder ID
    folder_id = load_conf_path("folder_id") or None

    if args.download:
        volume, location = args.download
        path = download_volume(volume, location)
        print(f"✅ Volume '{volume}' saved to {path}")

        if args.upload:
            link = upload_to_drive(path, conf_path,folder_id)
            print(f"☁️ Uploaded to Google Drive: {link}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
