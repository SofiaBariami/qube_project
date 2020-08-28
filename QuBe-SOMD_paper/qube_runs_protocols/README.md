Configure file for the runs with the QuBe forcefield

```
nmoves = 20000
ncycles = 75
buffered coordinates frequency = 5000
save coordinates = True
timestep = 2 * femtosecond
constraint = hbonds-notperturbed
hydrogen mass repartitioning factor = 1.0
cutoff type = nocutoff
cutoff distance = 10*angstrom
barostat = True
andersen = True
energy frequency = 250
precision = mixed
minimise = True
equilibrate = True
equilibration iterations = 20000
center solute = True
reaction field dielectric = 82.0
minimal coordinate saving = True
combining rules = geometric
lambda array =  0.00, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00
verbose = True
platform = CUDA
```
