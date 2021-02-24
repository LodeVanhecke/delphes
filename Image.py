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

# Book histograms
file = ROOT.TFile(sys.argv[1][:-5] +'_out.root','RECREATE')

histNJetL = ROOT.TH1F("histNJetL", "Number of jets in a event from L",10 , 0, 10)
histNJetS = ROOT.TH1F("histNJetS", "Number of jets in a event from S",10 , 0, 10)
histNJetC = ROOT.TH1F("histNJetC", "Number of jets in a event from C",10 , 0, 10)
histNJetB = ROOT.TH1F("histNJetB", "Number of jets in a event from B",10 , 0, 10)


histCKaonL = ROOT.TH2F("histCKaonL", "Angle/pseudoRap of charged kaons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histCKaonS = ROOT.TH2F("histCKaonS", "Angle/pseudoRap of charged kaons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histCKaonC = ROOT.TH2F("histCKaonC", "Angle/pseudoRap of charged kaons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histCKaonB = ROOT.TH2F("histCKaonB", "Angle/pseudoRap of charged kaons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)

histNKaonL = ROOT.TH2F("histNKaonL", "Angle/pseudoRap of neutral kaons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNKaonS = ROOT.TH2F("histNKaonS", "Angle/pseudoRap of neutral kaons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNKaonC = ROOT.TH2F("histNKaonC", "Angle/pseudoRap of neutral kaons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNKaonB = ROOT.TH2F("histNKaonB", "Angle/pseudoRap of neutral kaons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histCPionL = ROOT.TH2F("histCPionL", "Angle/pseudoRap of charged pions in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histCPionS = ROOT.TH2F("histCPionS", "Angle/pseudoRap of charged pions in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histCPionC = ROOT.TH2F("histCPionC", "Angle/pseudoRap of charged pions in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histCPionB = ROOT.TH2F("histCPionB", "Angle/pseudoRap of charged pions in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)

histNPionL = ROOT.TH2F("histNPionL", "Angle/pseudoRap of neutral pions in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNPionS = ROOT.TH2F("histNPionS", "Angle/pseudoRap of neutral pions in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNPionC = ROOT.TH2F("histNPionC", "Angle/pseudoRap of neutral pions in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNPionB = ROOT.TH2F("histNPionB", "Angle/pseudoRap of neutral pions in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histElecL = ROOT.TH2F("histElecL", "Angle/pseudoRap of electrons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histElecS = ROOT.TH2F("histElecS", "Angle/pseudoRap of electrons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histElecC = ROOT.TH2F("histElecC", "Angle/pseudoRap of electrons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histElecB = ROOT.TH2F("histElecB", "Angle/pseudoRap of electrons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histMuonL = ROOT.TH2F("histMuonL", "Angle/pseudoRap of muons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMuonS = ROOT.TH2F("histMuonS", "Angle/pseudoRap of muons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMuonC = ROOT.TH2F("histMuonC", "Angle/pseudoRap of muons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMuonB = ROOT.TH2F("histMuonB", "Angle/pseudoRap of muons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histProtL = ROOT.TH2F("histProtL", "Angle/pseudoRap of protons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histProtS = ROOT.TH2F("histProtS", "Angle/pseudoRap of protons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histProtC = ROOT.TH2F("histProtC", "Angle/pseudoRap of protons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histProtB = ROOT.TH2F("histProtB", "Angle/pseudoRap of protons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histNeutL = ROOT.TH2F("histNeutL", "Angle/pseudoRap of neutrons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNeutS = ROOT.TH2F("histNeutS", "Angle/pseudoRap of neutrons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNeutC = ROOT.TH2F("histNeutC", "Angle/pseudoRap of neutrons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histNeutB = ROOT.TH2F("histNeutB", "Angle/pseudoRap of neutrons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


# Loop over all events
for entry in range(0, numberOfEntries):
 # Load selected branches with data from specified event
 treeReader.ReadEntry(entry)

 q = ROOT.GenParticle()
 qbar = ROOT.GenParticle()
 for m in range(0,branchParticle.GetEntries()):
  particle = branchParticle.At(m)
  if particle.PID==23:
   q = branchParticle.At(particle.D1)
   qbar = branchParticle.At(particle.D2)

 # Print if q and qbar are wrongfully assigned
 if q.PID<0 or qbar.PID>0:
   print("ERROR: Wrongful association of quark and anti-quark in event: ",entry)
   continue
 # Skip event if opposite quarks don't exist for some reason
 if (q.PID+qbar.PID)!=0:
   print("ERROR: Skipping event: ",entry)
   continue

 qlv = ROOT.TLorentzVector()
 qbarlv = ROOT.TLorentzVector()
 qlv.SetPtEtaPhiM(q.PT, q.Eta, q.Phi, q.Mass)
 qbarlv.SetPtEtaPhiM(qbar.PT, qbar.Eta, qbar.Phi, qbar.Mass)

 Jetq = ROOT.Jet()
 Jetqlv = ROOT.TLorentzVector()
 Jetqbar = ROOT.Jet()
 Jetqbarlv = ROOT.TLorentzVector()
 nPosq = -1
 nPosqbar = -1

 NJet = 0

 for m in range(0,branchGenJet.GetEntries()):
  jet = branchGenJet.At(m)
  if jet.PT<10:
   continue
  NJet += 1
  if NJet < 2:
   continue


 # Skip if you don't have two good jet in the event
 if NJet < 2:
  continue

 jet0 = branchGenJet.At(0)
 jet1 = branchGenJet.At(1)
 jet0lv = ROOT.TLorentzVector()
 jet1lv = ROOT.TLorentzVector()
 jet0lv.SetPtEtaPhiM(jet0.PT,jet0.Eta,jet0.Phi,jet0.Mass)
 jet1lv.SetPtEtaPhiM(jet1.PT,jet1.Eta,jet1.Phi,jet1.Mass)


 if jet0lv.DeltaR(qlv)<jet0lv.DeltaR(qbarlv):
  nPosq = 0
  nPosqbar = 1
 else:
  nPosq = 1
  nPosqbar = 0

 Jetq = branchGenJet.At(nPosq)
 Jetqlv.SetPtEtaPhiM(Jetq.PT,Jetq.Eta,Jetq.Phi,Jetq.Mass)
 Jetqbar = branchGenJet.At(nPosqbar)
 Jetqbarlv.SetPtEtaPhiM(Jetqbar.PT,Jetqbar.Eta,Jetqbar.Phi,Jetqbar.Mass)


 # Code for histograms
 if q.PID == 1 or q.PID == 2:
  histNJetL.Fill(NJet)
 if q.PID == 3:
  histNJetS.Fill(NJet)
 if q.PID == 4:
  histNJetC.Fill(NJet)
 if q.PID == 5:
  histNJetB.Fill(NJet)

 for i in range(0,branchParticle.GetEntries()):
  p1 = ROOT.TLorentzVector()
  particle2 = branchParticle.At(i)
  p1.SetPtEtaPhiM(particle2.PT,particle2.Eta,particle2.Phi,particle2.Mass)
  if p1.DeltaR(Jetqlv) < p1.DeltaR(Jetqbarlv): 
   if p1.DeltaR(Jetqlv) <= 0.5:
    if abs(particle2.PID) == 321:    
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCKaonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCKaonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCKaonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCKaonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if abs(particle2.PID) == 311:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNKaonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNKaonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNKaonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNKaonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if abs(particle2.PID) == 211:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCPionL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCPionS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCPionC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histCPionB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if abs(particle2.PID) == 111:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNPionL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNPionS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNPionC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNPionB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if abs(particle2.PID) == 11:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if abs(particle2.PID) == 13:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if particle2.PID == 2212:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if particle2.PID == 2112:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    else:
     continue
   else:
    continue
  if p1.DeltaR(Jetqlv) > p1.DeltaR(Jetqbarlv):
   if p1.DeltaR(Jetqbarlv) <= 0.5:
    if abs(particle2.PID) == 321:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCKaonL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCKaonS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCKaonC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCKaonB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
    if abs(particle2.PID) == 311:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNKaonL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNKaonS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNKaonC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNKaonB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
    if abs(particle2.PID) == 211:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCPionL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCPionS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCPionC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histCPionB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
    if abs(particle2.PID) == 111:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNPionL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNPionS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNPionC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetqbar.PT
      Eta = Jetqbarlv.Eta()-p1.Eta()
      histNPionB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
    if abs(particle2.PID) == 11:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histElecB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if abs(particle2.PID) == 13:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histMuonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if particle2.PID == 2212:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histProtB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    if particle2.PID == 2112:
     if q.PID == 1 or q.PID == 2:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 3:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 4:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
     if q.PID == 5:
      PT = abs(particle2.PT)/Jetq.PT
      Eta = Jetqlv.Eta()-p1.Eta()
      histNeutB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
    else:
     continue
   else:
    continue
  else:
   continue


file.Write()

'''
 for m in range(0,branchparticle.GetEntries()):
   for j in range(0,branchGenJetqbar.GetEntries()):
    particle = branchParticle.At(m)
    if particle.PID == 23:
     p1.SetPtEtaPhiM(branchParticle.At(particle.D1).PT,branchParticle.At(particle.D1).Eta,branchParticle.At(particle.D1).Phi,branchParticle.At(particle.D1).Mass)
     p2.SetPtEtaPhiM(branchParticle.At(particle.D2).PT,branchParticle.At(particle.D2).Eta,branchParticle.At(particle.D2).Phi,branchParticle.At(particle.D2).Mass)
     jet = branchGenJet.At(j)
     lvofjet.SetPtEtaPhiM(jet.PT,jet.Eta,jet.Phi,jet.Mass)

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
      Eta = lvofjet.Eta()-p1.Eta()
      histCKaonL.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetS:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histCKaonS.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetC:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histCKaonC.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetB:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histCKaonB.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     else:
      pass
    if abs(particle.PID) == 311:
     if jet in JetL:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNKaonL.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetS:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNKaonS.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetC:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNKaonC.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetB:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNKaonB.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     else:
      pass
    if abs(particle.PID) == 211:
     if jet in JetL:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histCPionL.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetS:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histCPionS.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetC:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histCPionC.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetB:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histCPionB.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     else:
      pass
    if abs(particle.PID) == 111:
     if jet in JetL:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNPionL.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetS:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNPionS.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetC:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNPionC.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     if jet in JetB:
      PT = abs(particle.PT)/jet.PT
      Eta = lvofjet.Eta()-p1.Eta()
      histNPionB.Fill(p1.DeltaPhi(lvofjet),Eta,PT)
     else:
      pass
    else:
     pass
   else:
    pass
'''
