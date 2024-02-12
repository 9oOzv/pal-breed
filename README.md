# pal-breed

A script to calculate breeding paths to a target with specified inherited pals (up to 4 pals).

`pip install -r requirements.txt`

`python breed.py --target=<target> --names1=<pal1,pal2,pal3...> --names2=<pal1,pal2,pal3...> ...`

The paths will have at least one pal from each group.

* Given 1 or 2 name groups, the script will print breding chains containing up to 3 pals.
* Given 3 or 4 name groups, the script will print breeding chains containing up to 4 pals.
* If given 3 or 4 groups with too many pals in each, the script might crash/take too long 
  because of too many possible combinations

Results are sorted so that shortest/shallowest breed paths are at the bottom.

