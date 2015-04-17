import argparse

def main(parser):
    args = parser.parse_args()
    inputPath = args.input
    outputPath = args.output
    print inputPath
    print outputPath

def get_cleaner():
    usage = """There is only one argument which is the path to the subtitle file youu want to clean"""
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('input', default='subtitle', help=('path to the subtitle file'))
    parser.add_argument('output', default='subtitle.txt', help=('path to the output file'))
    return parser

if __name__ == '__main__':
    main(get_cleaner())
