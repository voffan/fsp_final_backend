python.exe -Xutf8 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission -e sessions  --indent 4 -o dump.json