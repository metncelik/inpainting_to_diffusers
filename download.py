from requests import get
import sys

print("downloading...")

r = get(f"{sys.argv[1]}", allow_redirects=True)
open(sys.argv[2],"wb").write(r.content)

print("done!")

