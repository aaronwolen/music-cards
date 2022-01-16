import argparse
import os.path
from typing import List
from evdev import InputDevice, list_devices


def discover_devices() -> List[InputDevice]:
    """Discover all devices"""
    print("Discovering devices...")
    devices = [InputDevice(fn) for fn in list_devices()]
    for dev in devices:
        print(f"...found '{dev.name}'")
    return devices


def main():
    """Configure music card reader"""
    p = argparse.ArgumentParser()
    p.add_argument(
        "-c",
        "--config-dir",
        help="Configuration directory where deviceName.txt will be written",
        default="config",
    )
    args = p.parse_args()

    if not os.path.isdir(args.config_dir):
        print(f"Config directory '{args.config_dir}' does not exist")
        sys.exit(1)

    devices = discover_devices()
    print("\nChoose the reader from devices list:")
    i = 1
    for dev in devices:
        print(f"  {i}. {dev.name}")
        i += 1

    dev_id = int(input("\nDevice Number: ")) - 1

    config_file = os.path.join(args.config_dir, "deviceName.txt")
    with open(config_file, "w") as f:
        f.write(devices[dev_id].name)
        f.close()
    print(f"\nSelection recorded in '{config_file}'.")


if __name__ == "__main__":
    main()
