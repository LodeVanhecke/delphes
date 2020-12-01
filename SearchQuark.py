import sys
import ROOT
import math

try:
  input = raw_input
except:
  pass

if len(sys.argv) < 2:
  print(" Usage: Example1.py input_file")
  sys.exit(1)

ROOT.gSystem.Load("/user/lvanhecke/delphes/libDelphes")

try:
  ROOT.gInterpreter.Declare('#include "/user/lvanhecke/delphes/classes/DelphesClasses.h"')
  ROOT.gInterpreter.Declare('#include "/user/lvanhecke/delphes/external/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass

inputFile = "../data/"+sys.argv[1]

# Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchGenJet = treeReader.UseBranch("GenJet")
branchParticle  = treeReader.UseBranch("Particle")
branchGenParticle = treeReader.UseBranch("GenParticle")

# Book histograms
histGenJetPT = ROOT.TH1F("histGenJetPT", "P_{T} of all GenJets", 100, 0, 70)
histNZ = ROOT.TH1F("histNZ", "Number of Z bosons in a event",18 , 0, 18)

# Loop over all events
for entry in range(0, numberOfEntries):
  # Load selected branches with data from specified event
  treeReader.ReadEntry(entry)
  
  NZ=0
  
  for m in range(0,branchGenParticle.GetEntries()):
    particle = branchGenParticle.At(m)
    if particle.PID==23:
     print(particle.D1.PID)
     print(particle.D2.PID)
     NZ=NZ+1
    else:
      break
  
  histNZ.Fill(NZ)
 
c1=ROOT.TCanvas('c3','Number of Z bosons in a event')
histNZ.Draw()
c1.SaveAs("histNZ.pdf")

input("Press Enter to continue...")
