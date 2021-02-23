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

histNJetL = ROOT.TH1F("histNJetL", "Number of jets in a event from L",18 , 0, 18)
histNJetS = ROOT.TH1F("histNJetS", "Number of jets in a event from S",18 , 0, 18)
histNJetC = ROOT.TH1F("histNJetC", "Number of jets in a event from C",18 , 0, 18)
histNJetB = ROOT.TH1F("histNJetB", "Number of jets in a event from B",18 , 0, 18)


histCKaonL = ROOT.TH2F("histCKaonL", "Angle/pseudoRap of charged kaons in L jet", 100, -math.pi, math.pi, 100, 0, 1000)
histCKaonS = ROOT.TH2F("histCKaonS", "Angle/pseudoRap of charged kaons in S jet", 100, -math.pi, math.pi, 100, 0, 1000)
histCKaonC = ROOT.TH2F("histCKaonC", "Angle/pseudoRap of charged kaons in C jet", 100, -math.pi, math.pi, 100, 0, 1000)
histCKaonB = ROOT.TH2F("histCKaonB", "Angle/pseudoRap of charged kaons in B jet", 100, -math.pi, math.pi, 100, 0, 1000) 


jetL = []
jetD = []
jetU = []
jetS = []
jetC = []
jetB = []

JetL = []
JetD = []
JetU = []
JetS = []
JetC = []
JetB = []


# Loop over all events
for entry in range(0, numberOfEntries):
 # Load selected branches with data from specified event
 treeReader.ReadEntry(entry)

 p1 = ROOT.TLorentzVector()
 p2 = ROOT.TLorentzVector()
 lvofjet = ROOT.TLorentzVector()

 for m in range(0,branchParticle.GetEntries()):
   for j in range(0,branchGenJet.GetEntries()):
    particle = branchParticle.At(m)
    p1.SetPtEtaPhiM(branchParticle.At(particle.D1).PT,branchParticle.At(particle.D1).Eta,branchParticle.At(particle.D1).Phi,branchParticle.At(particle.D1).Mass)
    p2.SetPtEtaPhiM(branchParticle.At(particle.D2).PT,branchParticle.At(particle.D2).Eta,branchParticle.At(particle.D2).Phi,branchParticle.At(particle.D2).Mass)
    jet = branchGenJet.At(j)
    lvofjet.SetPtEtaPhiM(jet.PT,jet.Eta,jet.Phi,jet.Mass)

    if particle.PID == 23:
     if abs(branchParticle.At(particle.D1).PID) == abs(branchParticle.At(particle.D2).PID):
      if abs(branchParticle.At(particle.D1).PID) == 1:
        jetD = jetD+[entry]
        jetL = jetL+[entry]
        if p1.DeltaR(lvofjet) <= 0.4 or p2.DeltaR(lvofjet) <= 0.4:
         JetD = JetD+[jet]
         JetL = JetL+[jet]
        else:
         pass
      if abs(branchParticle.At(particle.D1).PID) == 2:
        jetU = jetU+[entry]
        jetL = jetL+[entry]
        if p1.DeltaR(lvofjet) <= 0.4 or p2.DeltaR(lvofjet) <= 0.4:
         JetU = JetU+[jet]
         JetL = JetL+[jet]
        else:
         pass
      if abs(branchParticle.At(particle.D1).PID) == 3:
        jetS = jetS+[entry]
        if p1.DeltaR(lvofjet) <= 0.4 or p2.DeltaR(lvofjet) <= 0.4:
         JetS = JetS+[jet]
        else:
         pass
      if abs(branchParticle.At(particle.D1).PID) == 4:
        jetC = jetC+[entry]
        if p1.DeltaR(lvofjet) <= 0.4 or p2.DeltaR(lvofjet) <= 0.4:
         JetC = JetC+[jet]
        else:
         pass
      if abs(branchParticle.At(particle.D1).PID) == 5:
        jetB = jetB+[entry]
        if p1.DeltaR(lvofjet) <= 0.4 or p2.DeltaR(lvofjet) <= 0.4:
         JetB = JetB+[jet]
        else:
         pass
      else:
       pass
     else:
      pass
    else:
     pass

 NJet = 0 
  
 for i in range(0,branchGenJet.GetEntries()):
  jet = branchGenJet.At(i)
  if jet.PT > 10:
   NJet = NJet + 1
   if entry in jetL:
    histNJetL.Fill(NJet)
   if entry in jetS:
    histNJetS.Fill(NJet)
   if entry in jetC:
    histNJetC.Fill(NJet)
   if entry in jetB:
    histNJetB.Fill(NJet)
   else:
    pass


 for j in range(0,branchGenJet.GetEntries()):
  for m in range(0,branchParticle.GetEntries()):
   particle = branchParticle.At(m)
   p1.SetPtEtaPhiM(particle.PT,particle.Eta,particle.Phi,particle.Mass)
   jet = branchGenJet.At(j)
   lvofjet.SetPtEtaPhiM(jet.PT,jet.Eta,jet.Phi,jet.Mass)
   if p1.DeltaR(lvofjet) <= 0.4:
    if abs(particle.PID) == 321:    
     if jet in JetL:
      PT = abs(particle.PT)/jet.PT
      histCKaonL.Fill(p1.DeltaPhi(lvofjet),lvofjet.Eta-p1.Eta,PT)
     if jet in JetS:
      PT = abs(particle.PT)/jet.PT
      histCKaonS.Fill(p1.DeltaPhi(lvofjet),lvofjet.Eta-p1.Eta,PT)
     if jet in JetC:
      PT = abs(particle.PT)/jet.PT
      histCKaonC.Fill(p1.DeltaPhi(lvofjet),lvofjet.Eta-p1.Eta,PT)
     if jet in JetB:
      PT = abs(particle.PT)/jet.PT
      histCKaonB.Fill(p1.DeltaPhi(lvofjet),lvofjet.Eta-p1.Eta,PT)
     else:
      pass
    else:
     pass
   else:
    pass


file.Write()
