# files-collector
Project made for Programming in Python course at University of Warsaw

# Modules structure
The code was divided into specific modules
<ul>
  <li>
    main.py - script execution, argparse arguments parsing
  </li>
  <li>
    path_generation.py - module aimed at generating appropriate paths for files to generate in
  </li>
  <li>
    day_slicer.py - simple script that generates a specific day of the week or a list of days
  </li>
  <li>
    data_generation.py - module aimed at generating random data and reading generated data
  </li>
  <li>
    creator.py - script transforming a dictionary of random data into .json or .csv files appropriately
  </li>
  <li>
    reader.py - simple script for reading .json and .csv data
  </li>
</ul>

# Code execution
In order to execute code you need to execute main.py with the following flags:
<ul>
  <li>
    -m to specify a month
  </li>
  <li>
    -d to specify a day or a range of days using first_day-last_day notation
  </li>
  <li>
    -p to specify a time of the day (r means morning, w means evening)
  </li>
  <li>
    -t to specify a mode (t to create files, o to read files)
  </li>
  <li>
    -f to specify a file format (j as .json and c as .csv)
  </li>
</ul>
