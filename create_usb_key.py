#!/usr/bin/env python3
"""Create a 32-byte usb.key file on a selected drive or path.

Usage:
  python create_usb_key.py --drive E:
  python create_usb_key.py --out E:/usb.key
"""
import os
import argparse
import sys

def main():
    p = argparse.ArgumentParser(description='Create usb.key (32 random bytes)')
    p.add_argument('--drive', '-d', help='Drive letter or path (e.g. E: or E:\\)')
    p.add_argument('--out', '-o', help='Full output path for usb.key (overrides --drive)')
    args = p.parse_args()

    if args.out:
        out_path = args.out
    else:
        drive = args.drive
        if not drive:
            drive = input('Drive letter (e.g. E:): ').strip()
        # normalize simple letter like E to E:
        if len(drive) == 1 and drive.isalpha():
            drive = drive.upper() + ':'
        out_path = os.path.join(drive, 'usb.key')

    if os.path.exists(out_path):
        ans = input(f'{out_path} exists. Overwrite? (y/N): ').strip().lower()
        if ans != 'y':
            print('Aborted.')
            sys.exit(1)

    try:
        data = os.urandom(32)
        # ensure parent dir exists
        parent = os.path.dirname(out_path)
        if parent and not os.path.exists(parent):
            print(f'Path does not exist: {parent}')
            sys.exit(1)
        with open(out_path, 'wb') as f:
            f.write(data)
        print('Created usb.key at', out_path)
    except Exception as e:
        print('Failed to create usb.key:', e)
        sys.exit(1)

if __name__ == '__main__':
    main()
