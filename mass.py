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
branchTrack = treeReader.UseBranch("Track")

# Book histograms
file = ROOT.TFile(sys.argv[1][:-5] +'_out.root','RECREATE')

histMJetL = ROOT.TH1F("histMJetL", "Total invariant mass of jets in a event from L",100 , 0, 100)
histMJetS = ROOT.TH1F("histMJetS", "Total invariant mass of jets in a event from S",100 , 0, 100)
histMJetC = ROOT.TH1F("histMJetC", "Total invariant mass of jets in a event from C",100 , 0, 100)
histMJetB = ROOT.TH1F("histMJetB", "Total invariant mass of jets in a event from B",100 , 0, 100)

histM2JetL = ROOT.TH1F("histM2JetL", "Max invariant mass of two jets in a event from L",100 , 0, 100)
histM2JetS = ROOT.TH1F("histM2JetS", "Max invariant mass of two jets in a event from S",100 , 0, 100)
histM2JetC = ROOT.TH1F("histM2JetC", "Max invariant mass of two jets in a event from C",100 , 0, 100)
histM2JetB = ROOT.TH1F("histM2JetB", "Max invariant mass of two jets in a event from B",100 , 0, 100)

jetL = []
jetD = []
jetU = []
jetS = []
jetC = []
jetB = []


# Loop over all events
for entry in range(0, numberOfEntries):
 # Load selected branches with data from specified event
 treeReader.ReadEntry(entry)
 NZ = 0
 jetsM = []
 jets=ROOT.TLorentzVector() 
 lvofjet2=ROOT.TLorentzVector()
 lvofjet = ROOT.TLorentzVector()

 for m in range(0,branchParticle.GetEntries()):
   particle = branchParticle.At(m)
   if particle.PID == 23:
    if abs(branchParticle.At(particle.D1).PID) == abs(branchParticle.At(particle.D2).PID):
     NZ = NZ+1
     if abs(branchParticle.At(particle.D1).PID) == 1:
      jetD = jetD+[entry]
      jetL = jetL+[entry]
     if abs(branchParticle.At(particle.D1).PID) == 2:
      jetU = jetU+[entry]
      jetL = jetL+[entry]
     if abs(branchParticle.At(particle.D1).PID) == 3:
      jetS = jetS+[entry]
     if abs(branchParticle.At(particle.D1).PID) == 4:
      jetC = jetC+[entry]
     if abs(branchParticle.At(particle.D1).PID) == 5:
      jetB = jetB+[entry]
     else:
      pass
    else:
     pass
   else:
    pass


 # PT of jets
 # If event contains at least 1 jet
 if branchGenJet.GetEntries() > 0:
  # Take all jets in event
  for i in range(0,branchGenJet.GetEntries()):
   jet = branchGenJet.At(i)
   lvofjet.SetPtEtaPhiM(jet.PT,jet.Eta,jet.Phi,jet.Mass)
  
   # Total lv of all jets in event
   jets = jets+lvofjet
   # Loop over all jets in event
   for j in range(i,branchGenJet.GetEntries()):
    # Filter same jets
    if j==i:
     pass
    if j!=i:
     jet2 = branchGenJet.At(j)
     lvofjet2.SetPtEtaPhiM(jet2.PT,jet2.Eta,jet2.Phi,jet2.Mass)
     # Invariant mass of two jets
     jetsM = jetsM+[(lvofjet+lvofjet2).M()]
    else:
     pass

 # Plot total invariant mass of jets in event
 # Plot max invariant mass of two jets in event
 if entry in jetL:
  histMJetL.Fill(jets.M())
  try:
   histM2JetL.Fill(max(jetsM))
  except:
   pass
 if entry in jetS:
  histMJetS.Fill(jets.M())
  try:
   histM2JetS.Fill(max(jetsM))
  except:
   pass
 if entry in jetC:
  histMJetC.Fill(jets.M())
  try:
   histM2JetC.Fill(max(jetsM))
  except:
   pass
 if entry in jetB:
  histMJetB.Fill(jets.M())
  try:
   histM2JetB.Fill(max(jetsM))
  except:
   pass
 else:
  pass

file.Write()
