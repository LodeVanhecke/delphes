echo "========== Initialize the env variables =========="

source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_93python3 x86_64-slc6-gcc7-opt
source /cvmfs/grid.cern.ch/emi3ui-latest/etc/profile.d/setup-ui-example.sh

echo "========== Change to the working directory =========="
cd ./delphes/
pwd
echo ""

echo "========== Runnning Delphes =========="

python3 Image5.py ee_Z_qq_LO_Batch106_Mg5v266_PY8243_Delp341.root
