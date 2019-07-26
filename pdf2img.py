import os
import sys
import argparse
from pdf2image import convert_from_path

FLAGS = None


def pdf2img(pdf_dir, img_dir):
    if not os.path.isdir(pdf_dir):
        os.mkdir(pdf_dir)
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
    for file_path in os.listdir(pdf_dir):
        file_name, ext = os.path.splitext(file_path)
        if not ext == '.pdf':
            continue
        output_path = os.path.join(img_dir, file_name)
        if not os.path.isdir(output_path):
            os.mkdir(output_path)
        print('IMAGE MAKING.....\t: ', output_path)
        pages = convert_from_path(os.path.join(pdf_dir, file_path))
        for i, page in enumerate(pages):
            page.save(os.path.join(output_path, str(i+1) + '.png'), 'PNG')


def main():
    pdf2img(FLAGS.pdf_dir, FLAGS.img_dir)


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(sys.argv[0]))

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--pdf_dir',
        type=str,
        default=os.path.join(current_path, 'pdf'),
        help='The pdf documents directory to be transferred to img')

    parser.add_argument(
        '--img_dir',
        type=str,
        default=os.path.join(current_path, 'img'),
        help='The img documents transferred directory')
    FLAGS, unparsed = parser.parse_known_args()

    main()
