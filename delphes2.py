import sys
import ROOT

try:
  input = raw_input
except:
  pass

if len(sys.argv) < 2:
  print(" Usage: Example1.py input_file")
  sys.exit(1)

ROOT.gSystem.Load("/home/lodev/delphes/libDelphes")

try:
  ROOT.gInterpreter.Declare('#include "/home/lodev/delphes/classes/DelphesClasses.h"')
  ROOT.gInterpreter.Declare('#include "/home/lodev/delphes/external/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass

inputFile = sys.argv[1]

# Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchGenJet = treeReader.UseBranch("GenJet")
branchParticle  = treeReader.UseBranch("Particle")

# Book histograms
histGenJetPT = ROOT.TH1F("histGenJetPT", "P_{T} of all GenJets", 100, 0, 600 )
histParticlePT = ROOT.TH1F("HistparticlePT", "P_{T} of all kaons", 100, 0, 400)
histNJet = ROOT.TH1F("histNJet", "Number of jets in a event",30 , 0,30 )
# Loop over all events
for entry in range(0, numberOfEntries):
  # Load selected branches with data from specified event
  treeReader.ReadEntry(entry)

  histNJet.Fill(branchGenJet.GetEntries())

  # If event contains at least 1 jet
  if branchGenJet.GetEntries() > 0:
    # Take all jets in event
    for i in range(0,branchGenJet.GetEntries()):
     jet = branchGenJet.At(i)

    # Plot jet transverse momentum
     histGenJetPT.Fill(jet.PT)

    # Print jet transverse momentum
    # print(jet.PT)

# If event contains at least 1 particle
  if branchParticle.GetEntries() > 0:
    # Take first particle
    for i in range(0,branchParticle.GetEntries()):
     particle = branchParticle.At(i)
     #filter Kaon(K0,K+,K-) using PDG ID
     if abs(particle.PID)==321 or abs(particle.PID)==311:
     # print(particle.PID)
    # Plot PT
      histParticlePT.Fill(particle.PT)
    # print(particle.Mass)
# Show resulting histogram

c1=ROOT.TCanvas('c1','Histogram GenJet')
histGenJetPT.Draw()
c2=ROOT.TCanvas('c2','Histogram P_{T} kaons')
histParticlePT.Draw()
c3=ROOT.TCanvas('c3','Number of jets in a event')
histNJet.Draw()

input("Press Enter to continue...")
