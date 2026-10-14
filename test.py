import argparse

parser = argparse.ArgumentParser(description='Проверка размера директории')
parser.add_argument('path', type=str, help='path to the dir')
parser.add_argument('--limit', type=float, default=1.0, help='limit at GB')
args = parser.parse_args()

print(f"path: {args.path}, Limit: {args.limit} GB") 
