#!/usr/bin/env python3
"""Compress and copy images from Andrew's Demo to FAQ_test/attachments."""
import os
from PIL import Image

SRC = r"D:/ObsidianDB/Andrew's Demo/Knowledge Base ERM FEPOS/FAQ_test/attachments"
DST = r"D:/ObsidianDB/FAQTest/FAQ_test/attachments"
MAX_WIDTH = 1000
JPEG_QUALITY = 65

total_in = total_out = count = errors = 0
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp'}

for root, dirs, files in os.walk(SRC):
    for f in files:
        src_path = os.path.join(root, f)
        rel = os.path.relpath(src_path, SRC)
        dst_path = os.path.join(DST, rel)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        size_in = os.path.getsize(src_path)
        total_in += size_in
        ext = os.path.splitext(f)[1].lower()

        if ext not in IMAGE_EXTS:
            with open(src_path, 'rb') as fin, open(dst_path, 'wb') as fout:
                fout.write(fin.read())
            total_out += size_in
            count += 1
            continue

        try:
            img = Image.open(src_path)
            if img.mode in ('RGBA', 'P', 'LA'):
                if ext == '.png':
                    pass  # Keep PNG as RGBA
                else:
                    img = img.convert('RGB')

            w, h = img.size
            if w > MAX_WIDTH:
                ratio = MAX_WIDTH / w
                img = img.resize((MAX_WIDTH, int(h * ratio)), Image.LANCZOS)

            if ext in ('.jpg', '.jpeg'):
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                img.save(dst_path, 'JPEG', quality=JPEG_QUALITY, optimize=True)
            elif ext == '.png':
                # Convert PNG screenshots to JPEG for massive size reduction
                if img.mode in ('RGBA', 'PA', 'LA'):
                    # Has transparency - keep as compressed PNG
                    img.save(dst_path, 'PNG', optimize=True)
                else:
                    # No transparency - convert to JPEG
                    jpg_path = os.path.splitext(dst_path)[0] + '.jpg'
                    img.convert('RGB').save(jpg_path, 'JPEG', quality=85, optimize=True)
                    dst_path = jpg_path
            elif ext == '.bmp':
                dst_path = os.path.splitext(dst_path)[0] + '.png'
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                img.save(dst_path, 'PNG', optimize=True)
            else:
                img.save(dst_path, optimize=True)

            size_out = os.path.getsize(dst_path)
            total_out += size_out
            count += 1

            if count % 200 == 0:
                print(f'  {count} images... ({total_in/1024/1024:.0f}MB -> {total_out/1024/1024:.0f}MB)')
        except Exception as e:
            with open(src_path, 'rb') as fin, open(dst_path, 'wb') as fout:
                fout.write(fin.read())
            total_out += size_in
            errors += 1

print(f'\nDone: {count} files, {total_in/1024/1024:.0f}MB -> {total_out/1024/1024:.0f}MB')
print(f'Compression: {(1-total_out/total_in)*100:.0f}% reduction, {errors} errors')
