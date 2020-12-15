
mkdir input_vac
mkdir input_solv

cd input_vac
cp /PATH/TO/FILE//MOL.pdb .
cp /PATH/TO/FILE//MOL.xml .
cp /PATH/TO/FILE/qube_to_prmRst.py .
cp /PATH/TO/FILE/remove_solty.py .

~/sire.app/bin/ipython 
run ./qube_to_prmRst.py -x MOL.xml -p MOL.pdb
quit()
rm qube_to_prmRst.py

python remove_solty.py

mv MOL.rst7 SYSTEM.crd

cp /PATH/TO/FILE/morph_step*.py .

python morph_step1.py 
python morph_step2.py 

rm morph_step*
rm remove_solty.py


cd ../input_solv
cp ../MOL.* .
cp /PATH/TO/FILE/qube_to_prmRst.py .
cp /PATH/TO/FILE/remove_solty.py .

~/sire.app/bin/ipython 
run ./qube_to_prmRst.py -x MOL.xml -p MOL.pdb
quit()
rm qube_to_prmRst.py


~/biosimspace.app/bin/ipython
run ./solvate.py --input MOL.prm7 MOL.rst7 --output MOL_sol --water tip3p --box_dim 26
run ./amberequilibration.py --input MOL_sol.prm7 MOL_sol.rst7 --output MOL
quit()


python remove_solty.py

mv MOL.rst7 SYSTEM.crd

cp /PATH/TO/FILE/morph_step*.py .

python morph_step1.py 
python morph_step2.py 

rm morph_step*

cd ..
mkdir FEP
cd FEP

mkdir solv
mkdir vaccum
cd solv/
mkdir discharge
mkdir vanish 
cd discharge/
mkdir input 
mkdir output 
cd ../vanish/
mkdir input 
mkdir output 
cd ../../vaccum/
mkdir discharge 
mkdir vanish 
cd discharge/
mkdir input 
mkdir output
cd ../vanish/
mkdir output
mkdir input 
cd input/

cp ../../../../input_vac/SYSTEM.* .
cp SYSTEM.* ../../discharge/input/
cp ../../../../input_vac/MORPH.pert.vanish MORPH.pert
cp ../../../../input_vac/MORPH.pert.discharge ../../discharge/input/MORPH.pert
cp /PATH/TO/FILE/sim.cfg .
cp sim.cfg ../../discharge/input
cd ../output/
cp /PATH/TO/FILE/run_FEP_locally.sh .
nohup bash run_FEP_locally.sh &

cd ../../../solv/vanish/input/
cp ../../../../input_solv/SYSTEM.* .
cp SYSTEM.* ../../discharge/input/
cp ../../../../input_solv/MORPH.pert.vanish MORPH.pert
cp ../../../../input_solv/MORPH.pert.discharge ../../discharge/input/MORPH.pert
cp /PATH/TO/FILE/sim.cfg .
cp sim.cfg ../../discharge/input
cd ../output/
cp /PATH/TO/FILE/run_FEP_locally.sh .
nohup bash run_FEP_locally.sh &




