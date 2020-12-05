# Mapping your blind spot

TODO: add more details.

1. Run `conditions/generate_mapping_adaptive.py` to generate a set of sample points to test. Initially, I suggest the paramters `-3 0 4 100`. (This does `100` samples uniformly from a disk centered at `-3 0` with radius `4`.)
2. Run `map.psyexp` in PsychoPy. Press `f` if you do not see the spot, and press `j` if you do.
3. Run `show_map.py` and enter the appropriate test subject details. (e.g. `james -1` to show `james`' right eye.)
4. If you want to collect more samples, re-run `conditions/generate_mapping_adaptive.py` with new settings to generate different sample locations. Repeat until the blind spot has been adequately mapped.
