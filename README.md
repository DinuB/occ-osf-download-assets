## occ-osf-download-assets

**subject:** download occ assets and refresh to avoid errors

**programming language**: python

**reguired:** python3

**install:**
- clone the repository
- copy the **python** folder into your project folder

**options**
- download assets: ```python3 python/osf.py download```
- refresh slots(if not run can give error when performing deploy): ```python3 python/osf.py refresh-assets```

**obs:** when you run the ```python3 python/osf.py download``` command you will be asked if you want to refresh the assets, if you answer **y** you will not need to run the ```python3 python/osf.py refresh-assets``` command.
