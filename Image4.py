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


histJetCKaonL = ROOT.TH2F("histJetCKaonL", "charged kaons in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetCKaonS = ROOT.TH2F("histJetCKaonS", "charged kaons in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetNKaonL = ROOT.TH2F("histJetNKaonL", "neutral kaons in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetNKaonS = ROOT.TH2F("histJetNKaonS", "neutral kaons in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetCPionL = ROOT.TH2F("histJetCPionL", "charged pions in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetCPionS = ROOT.TH2F("histJetCPionS", "charged pions in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetNPionL = ROOT.TH2F("histJetNPionL", "neutral pions in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetNPionS = ROOT.TH2F("histJetNPionS", "neutral pions in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetElecL = ROOT.TH2F("histJetElecL", "electrons in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetElecS = ROOT.TH2F("histJetElecS", "electrons in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetMuonL = ROOT.TH2F("histJetMuonL", "muons in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetMuonS = ROOT.TH2F("histJetMuonS", "muons in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetProtL = ROOT.TH2F("histJetProtL", "protons in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetProtS = ROOT.TH2F("histJetProtS", "protons in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetNeutL = ROOT.TH2F("histJetNeutL", "neutrons in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetNeutS = ROOT.TH2F("histJetNeutS", "neutrons in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)

histJetPhotL = ROOT.TH2F("histJetPhotL", "photons in L jet", 50, -0.6, 0.6, 50, -0.6, 0.6)
histJetPhotS = ROOT.TH2F("histJetPhotS", "photons in S jet", 50, -0.6, 0.6, 50, -0.6, 0.6)


histRatCKaonMuonL = ROOT.TH1F("histRatCKaonMuonL", "Ratio of charged kaons and muons in L jet", 10, 0, 10)
histRatCKaonMuonS = ROOT.TH1F("histRatCKaonMuonS", "Ratio of charged kaons and muons in S jet", 10, 0, 10)


NL = 0
NS = 0
NC = 0
NB = 0


NJetL = 0
NJetS = 0
NJetC = 0
NJetB = 0


Q = []


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
  NL += 1
 if q.PID == 3:
  NS += 1
 if q.PID == 4:
  NC += 1
 if q.PID == 5:
  NB += 1

 NCKaonq = 0
 NCKaonqbar = 0
 NNKaonq = 0
 NNKaonqbar = 0
 NCPionq = 0
 NCPionqbar = 0
 NNPionq = 0
 NNPionqbar = 0
 NElecq = 0
 NElecqbar = 0
 NMuonq = 0
 NMuonqbar = 0
 NProtq = 0
 NProtqbar = 0
 NNeutq = 0
 NNeutqbar = 0
 NPhotq = 0
 NPhotqbar = 0


 for i in range(0,branchParticle.GetEntries()):
  p1 = ROOT.TLorentzVector()
  particle2 = branchParticle.At(i)
  p1.SetPtEtaPhiM(particle2.PT,particle2.Eta,particle2.Phi,particle2.Mass)
  if particle2.PT > 10:
   if p1.DeltaR(Jetqlv) < p1.DeltaR(Jetqbarlv):
    if p1.DeltaR(Jetqlv) <= 0.5:
     if abs(particle2.PID) == 321:
      NCKaonq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetCKaonL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetCKaonS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 310 or abs(particle2.PID) == 130:
      NNKaonq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetNKaonL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetNKaonS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 211:
      NCPionq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetCPionL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetCPionS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 111:
      NNPionq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetNPionL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetNPionS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 11:
      NElecq += 1
      print(particle2.Status)
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetElecL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetElecS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 13:
      NMuonq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetMuonL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetMuonS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if particle2.PID == 2212:
      NProtq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetProtL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetProtS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if particle2.PID == 2112:
      NNeutq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetNeutL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetNeutS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if particle2.PID == 22:
      NPhotq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetPhotL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetPhotS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     else:
      continue
    else:
     continue
   if p1.DeltaR(Jetqlv) > p1.DeltaR(Jetqbarlv):
    if p1.DeltaR(Jetqbarlv) <= 0.5:
     if abs(particle2.PID) == 321:
      NCKaonqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetCKaonL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetCKaonS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if abs(particle2.PID) == 310 or abs(particle2.PID) == 130:
      NNKaonqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetNKaonL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetNKaonS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if abs(particle2.PID) == 211:
      NCPionqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetCPionL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetCPionS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if abs(particle2.PID) == 111:
      NNPionqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetNPionL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetNPionS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if abs(particle2.PID) == 11:
      NElecqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetElecL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetElecS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if abs(particle2.PID) == 13:
      NMuonqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetMuonL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetMuonS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if particle2.PID == 2212:
      NProtqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetProtL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetProtS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if particle2.PID == 2112:
      NNeutqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetNeutL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetNeutS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     if particle2.PID == 22:
      NPhotqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetPhotL.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetPhotS.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     else:
      continue
    else:
     continue
   else:
    continue
  else:
   continue

 if q.PID == 1 or q.PID == 2:
  try:
   histRatCKaonMuonL.Fill((NCKaonq/NMuonq)**-1)
  except:
   pass
  try:
   histRatCKaonMuonL.Fill((NCKaonqbar/NMuonqbar)**-1)
  except:
   pass
 if q.PID == 3:
  try:
   histRatCKaonMuonS.Fill((NCKaonq/NMuonq)**-1)
  except:
   pass
  try:
   histRatCKaonMuonS.Fill((NCKaonqbar/NMuonqbar)**-1)
  except:
   pass


 Q += [q.PID]


# Normalize hists


histJetCKaonL *= 1/NL
histJetCKaonS *= 1/NS

histJetNKaonL *= 1/NL
histJetNKaonS *= 1/NS

histJetCPionL *= 1/NL
histJetCPionS *= 1/NS

histJetNPionL *= 1/NL
histJetNPionS *= 1/NS

histJetElecL *= 1/NL
histJetElecS *= 1/NS

histJetMuonL *= 1/NL
histJetMuonS *= 1/NS

histJetProtL *= 1/NL
histJetProtS *= 1/NS

histJetNeutL *= 1/NL
histJetNeutS *= 1/NS

histJetPhotL *= 1/NL
histJetPhotS *= 1/NS


file.Write()
