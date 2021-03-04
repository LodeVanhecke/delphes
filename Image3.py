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


histMaxCKaonL = ROOT.TH2F("histMaxCKaonL", "Angle/pseudoRap of max charged kaons in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxCKaonS = ROOT.TH2F("histMaxCKaonS", "Angle/pseudoRap of max charged kaons in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxNKaonL = ROOT.TH2F("histMaxNKaonL", "Angle/pseudoRap of max neutral kaons in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxNKaonS = ROOT.TH2F("histMaxNKaonS", "Angle/pseudoRap of max neutral kaons in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxCPionL = ROOT.TH2F("histMaxCPionL", "Angle/pseudoRap of max charged pions in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxCPionS = ROOT.TH2F("histMaxCPionS", "Angle/pseudoRap of max charged pions in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxNPionL = ROOT.TH2F("histMaxNPionL", "Angle/pseudoRap of max neutral pions in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxNPionS = ROOT.TH2F("histMaxNPionS", "Angle/pseudoRap of max neutral pions in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxElecL = ROOT.TH2F("histMaxElecL", "Angle/pseudoRap of max electrons in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxElecS = ROOT.TH2F("histMaxElecS", "Angle/pseudoRap of max electrons in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxMuonL = ROOT.TH2F("histMaxMuonL", "Angle/pseudoRap of max muons in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxMuonS = ROOT.TH2F("histMaxMuonS", "Angle/pseudoRap of max muons in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxProtL = ROOT.TH2F("histMaxProtL", "Angle/pseudoRap of max protons in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxProtS = ROOT.TH2F("histMaxProtS", "Angle/pseudoRap of max protons in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxNeutL = ROOT.TH2F("histMaxNeutL", "Angle/pseudoRap of max neutrons in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxNeutS = ROOT.TH2F("histMaxNeutS", "Angle/pseudoRap of max neutrons in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)

histMaxPhotL = ROOT.TH2F("histMaxPhotL", "Angle/pseudoRap of max photons in L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histMaxPhotS = ROOT.TH2F("histMaxPhotS", "Angle/pseudoRap of max photons in S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)


histCloseNeutL = ROOT.TH2F("histCloseNeutL", "Angle\pseudoRap of closest neutrons L jet", 500, -0.6, 0.6, 500, -0.6, 0.6)
histCloseNeutS = ROOT.TH2F("histCloseNeutS", "Angle\pseudoRap of closest neutrons S jet", 500, -0.6, 0.6, 500, -0.6, 0.6)


histJetCKaonL = ROOT.TH2F("histJetCKaonL", "charged kaons in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetCKaonS = ROOT.TH2F("histJetCKaonS", "charged kaons in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetNKaonL = ROOT.TH2F("histJetNKaonL", "neutral kaons in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetNKaonS = ROOT.TH2F("histJetNKaonS", "neutral kaons in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetCPionL = ROOT.TH2F("histJetCPionL", "charged pions in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetCPionS = ROOT.TH2F("histJetCPionS", "charged pions in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetNPionL = ROOT.TH2F("histJetNPionL", "neutral pions in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetNPionS = ROOT.TH2F("histJetNPionS", "neutral pions in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetElecL = ROOT.TH2F("histJetElecL", "electrons in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetElecS = ROOT.TH2F("histJetElecS", "electrons in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetMuonL = ROOT.TH2F("histJetMuonL", "muons in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetMuonS = ROOT.TH2F("histJetMuonS", "muons in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetProtL = ROOT.TH2F("histJetProtL", "protons in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetProtS = ROOT.TH2F("histJetProtS", "protons in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetNeutL = ROOT.TH2F("histJetNeutL", "neutrons in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetNeutS = ROOT.TH2F("histJetNeutS", "neutrons in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)

histJetPhotL = ROOT.TH2F("histJetPhotL", "photons in L jet", 100, -0.6, 0.6, 100, -0.6, 0.6)
histJetPhotS = ROOT.TH2F("histJetPhotS", "photons in S jet", 100, -0.6, 0.6, 100, -0.6, 0.6)


histRatCPionPhotL = ROOT.TH1F("histRatCPionPhotL", "Ratio of charged pions and photons in L jet", 20, 0, 10)
histRatCPionPhotS = ROOT.TH1F("histRatCPionPhotS", "Ratio of charged pions and photons in S jet", 20, 0, 10)

histRatNPionElecL = ROOT.TH1F("histRatNPionElecL", "Ratio of neutral pions and electrons/positrons in L jet", 20, 0, 10)
histRatNPionElecS = ROOT.TH1F("histRatNPionElecS", "Ratio of neutral pions and electrons/positrons in S jet", 20, 0, 10)

histRatCPionMuonL = ROOT.TH1F("histRatCPionMuonL", "Ratio of charged pions and muons in L jet", 20, 0, 10)
histRatCPionMuonS = ROOT.TH1F("histRatCPionMuonS", "Ratio of charged pions and muons in S jet", 20, 0, 10)

histRatCKaonMuonL = ROOT.TH1F("histRatCKaonMuonL", "Ratio of charged kaons and muons in L jet", 20, 0, 10)
histRatCKaonMuonS = ROOT.TH1F("histRatCKaonMuonS", "Ratio of charged kaons and muons in S jet", 20, 0, 10)

histRatNKaonCPionL = ROOT.TH1F("histRatNKaonCPionL", "Ratio of neutral kaons and charged pions in L jet", 20, 0, 10)
histRatNKaonCPionS = ROOT.TH1F("histRatNKaonCPionS", "Ratio of neutral kaons and charged pions in S jet", 20, 0, 10)


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

 
 CKaonL = [0, 0, 0]
 CKaonS = [0, 0, 0]
 CKaonC = [0, 0, 0]
 CKaonB = [0, 0, 0]
 NKaonL = [0, 0, 0]
 NKaonS = [0, 0, 0]
 NKaonC = [0, 0, 0]
 NKaonB = [0, 0, 0]
 CPionL = [0, 0, 0]
 CPionS = [0, 0, 0]
 CPionC = [0, 0, 0]
 CPionB = [0, 0, 0]
 NPionL = [0, 0, 0]
 NPionS = [0, 0, 0]
 NPionC = [0, 0, 0]
 NPionB = [0, 0, 0]
 CKaonL = [0, 0, 0]
 CKaonS = [0, 0, 0]
 CKaonC = [0, 0, 0]
 CKaonB = [0, 0, 0]
 ElecL = [0, 0, 0]
 ElecS = [0, 0, 0]
 ElecC = [0, 0, 0]
 ElecB = [0, 0, 0]
 MuonL = [0, 0, 0]
 MuonS = [0, 0, 0]
 MuonC = [0, 0, 0]
 MuonB = [0, 0, 0]
 ProtL = [0, 0, 0]
 ProtS = [0, 0, 0]
 ProtC = [0, 0, 0]
 ProtB = [0, 0, 0]
 NeutL =[0, 0, 0] 
 NeutS =[0, 0, 0]
 NeutC =[0, 0, 0]
 NeutB =[0, 0, 0]
 PhotL =[0, 0, 0]
 PhotS =[0, 0, 0]
 PhotC =[0, 0, 0]
 PhotB =[0, 0, 0]

 CloseCKaonL = [0, 0, 0]
 CloseCKaonS = [0, 0, 0]
 CloseCKaonC = [0, 0, 0]
 CloseCKaonB = [0, 0, 0]
 CloseNKaonL = [0, 0, 0]
 CloseNKaonS = [0, 0, 0]
 CloseNKaonC = [0, 0, 0]
 CloseNKaonB = [0, 0, 0]
 CloseCPionL = [0, 0, 0]
 CloseCPionS = [0, 0, 0]
 CloseCPionC = [0, 0, 0]
 CloseCPionB = [0, 0, 0]
 CloseNPionL = [0, 0, 0]
 CloseNPionS = [0, 0, 0]
 CloseNPionC = [0, 0, 0]
 CloseNPionB = [0, 0, 0]
 CloseCKaonL = [0, 0, 0]
 CloseCKaonS = [0, 0, 0]
 CloseCKaonC = [0, 0, 0]
 CloseCKaonB = [0, 0, 0]
 CloseElecL = [0, 0, 0]
 CloseElecS = [0, 0, 0]
 CloseElecC = [0, 0, 0]
 CloseElecB = [0, 0, 0]
 CloseMuonL = [0, 0, 0]
 CloseMuonS = [0, 0, 0]
 CloseMuonC = [0, 0, 0]
 CloseMuonB = [0, 0, 0]
 CloseProtL = [0, 0, 0]
 CloseProtS = [0, 0, 0]
 CloseProtC = [0, 0, 0]
 CloseProtB = [0, 0, 0]
 CloseNeutL =[100, 0, 0]
 CloseNeutS =[100, 0, 0]
 CloseNeutC =[100, 0, 0]
 CloseNeutB =[100, 0, 0]
 ClosePhotL =[100, 0, 0]
 ClosePhotS =[0, 0, 0]
 ClosePhotC =[0, 0, 0]
 ClosePhotB =[0, 0, 0]

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
  if particle2.PT > 1:
   if p1.DeltaR(Jetqlv) < p1.DeltaR(Jetqbarlv): 
    if p1.DeltaR(Jetqlv) <= 0.5:
     if abs(particle2.PID) == 321:    
      NCKaonq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > CKaonL[2]: CKaonL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetCKaonL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > CKaonS[2]: CKaonS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetCKaonS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 311:
      NNKaonq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NKaonL[2]: NKaonL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetNKaonL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NKaonS[2]: NKaonS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetNKaonS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 211:
      NCPionq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > CPionL[2]: CPionL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetCPionL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > CPionS[2]: CPionS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetCPionS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 111:
      NNPionq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NPionL[2]: NPionL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetNPionL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NPionS[2]: NPionS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetNPionS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 11:
      NElecq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ElecL[2]: ElecL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetElecL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ElecS[2]: ElecS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetElecS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if abs(particle2.PID) == 13:
      NMuonq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > MuonL[2]: MuonL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetMuonL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > MuonS[2]: MuonS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetMuonS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if particle2.PID == 2212:
      NProtq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ProtL[2]: ProtL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetProtL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ProtS[2]: ProtS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetProtS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if particle2.PID == 2112:
      NNeutq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NeutL[2]: NeutL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if abs(p1.DeltaPhi(Jetqlv)) < CloseNeutL[0]: CloseNeutL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetNeutL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NeutS[2]: NeutS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if abs(p1.DeltaPhi(Jetqlv)) < CloseNeutS[0]: CloseNeutS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetNeutS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     if particle2.PID == 22:
      NPhotq += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > PhotL[2]: PhotL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetPhotL.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > PhotS[2]: PhotS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if Q.count(q.PID) == 1: histJetPhotS.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
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
       if particle2.PT > CKaonL[2]: CKaonL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       if particle2.PT > CKaonS[2]: CKaonS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if abs(particle2.PID) == 311:
      NNKaonqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       if particle2.PT > NKaonL[2]: NKaonL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       if particle2.PT > NKaonS[2]: NKaonS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if abs(particle2.PID) == 211:
      NCPionqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       if particle2.PT > CPionL[2]: CPionL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       if particle2.PT > CPionS[2]: CPionS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if abs(particle2.PID) == 111:
      NNPionqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       if particle2.PT > NPionL[2]: NPionL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       if particle2.PT > NPionS[2]: NPionS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if abs(particle2.PID) == 11:
      NElecqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ElecL[2]: ElecL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ElecS[2]: ElecS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if abs(particle2.PID) == 13:
      NMuonqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > MuonL[2]: MuonL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > MuonS[2]: MuonS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if particle2.PID == 2212:
      NProtqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ProtL[2]: ProtL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > ProtS[2]: ProtS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if particle2.PID == 2112:
      NNeutqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NeutL[2]: NeutL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if abs(p1.DeltaPhi(Jetqlv)) < CloseNeutL[0]: CloseNeutL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > NeutS[2]: NeutS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
       if abs(p1.DeltaPhi(Jetqlv)) < CloseNeutS[0]: CloseNeutS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
     if particle2.PID == 22:
      NPhotqbar += 1
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > PhotL[2]: PhotL = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       if particle2.PT > PhotS[2]: PhotS = [p1.DeltaPhi(Jetqlv),DeltaTheta,PT]
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
   histRatCPionPhotL.Fill(NCPionq/NPhotq)
   histRatCPionPhotL.Fill(NCPionqbar/NPhotqbar)
   histRatNPionElecL.Fill(NNPionq/NElecq)
   histRatNPionElecL.Fill(NNPionqbar/NElecqbar)
   histRatCPionMuonL.Fill(NCPionq/NMuonq)
   histRatCPionMuonL.Fill(NCPionqbar/NMuonqbar)
   histRatCKaonMuonL.Fill(NCKaonq/NMuonq)
   histRatCKaonMuonL.Fill(NCKaonqbar/NMuonqbar)
   histRatNKaonCPionL.Fill(NNKaonq/NCPionq)
   histRatNKaonCPionL.Fill(NNKaonqbar/NCPionqbar)
  except:
   pass
 if q.PID == 3:
  try:
   histRatCPionPhotS.Fill(NCPionq/NPhotq)
   histRatCPionPhotS.Fill(NCPionqbar/NPhotqbar)
   histRatNPionElecS.Fill(NNPionq/NElecq)
   histRatNPionElecS.Fill(NNPionqbar/NElecqbar)
   histRatCPionMuonS.Fill(NCPionq/NMuonq)
   histRatCPionMuonS.Fill(NCPionqbar/NMuonqbar)
   histRatCKaonMuonS.Fill(NCKaonq/NMuonq)
   histRatCKaonMuonS.Fill(NCKaonqbar/NMuonqbar)
   histRatNKaonCPionS.Fill(NNKaonq/NCPionq)
   histRatNKaonCPionS.Fill(NNKaonqbar/NCPionqbar)
  except:
   pass

 Q += [q.PID]


 histMaxCKaonL.Fill(CKaonL[0],CKaonL[1],CKaonL[2])
 histMaxCKaonS.Fill(CKaonS[0],CKaonS[1],CKaonS[2])

 histMaxNKaonL.Fill(NKaonL[0],NKaonL[1],NKaonL[2])
 histMaxNKaonS.Fill(NKaonS[0],NKaonS[1],NKaonS[2])

 histMaxCPionL.Fill(CPionL[0],CPionL[1],CPionL[2])
 histMaxCPionS.Fill(CPionS[0],CPionS[1],CPionS[2])

 histMaxNPionL.Fill(NPionL[0],NPionL[1],NPionL[2])
 histMaxNPionS.Fill(NPionS[0],NPionS[1],NPionS[2])

 histMaxElecL.Fill(ElecL[0],ElecL[1],ElecL[2])
 histMaxElecS.Fill(ElecS[0],ElecS[1],ElecS[2])

 histMaxMuonL.Fill(MuonL[0],MuonL[1],MuonL[2])
 histMaxMuonS.Fill(MuonS[0],MuonS[1],MuonS[2])

 histMaxProtL.Fill(ProtL[0],ProtL[1],ProtL[2])
 histMaxProtS.Fill(ProtS[0],ProtS[1],ProtS[2])

 histMaxNeutL.Fill(NeutL[0],NeutL[1],NeutL[2])
 histMaxNeutS.Fill(NeutS[0],NeutS[1],NeutS[2])

 histMaxPhotL.Fill(PhotL[0],PhotL[1],PhotL[2])
 histMaxPhotS.Fill(PhotS[0],PhotS[1],PhotS[2])

 histCloseNeutL.Fill(CloseNeutL[0],CloseNeutL[1],CloseNeutL[2])
 histCloseNeutS.Fill(CloseNeutS[0],CloseNeutS[1],CloseNeutS[2])
 
# Normalize hists

histMaxCKaonL *= 1/NL
histMaxCKaonS *= 1/NS

histMaxNKaonL *= 1/NL
histMaxNKaonS *= 1/NS

histMaxCPionL *= 1/NL
histMaxCPionS *= 1/NS

histMaxNPionL *= 1/NL
histMaxNPionS *= 1/NS

histMaxElecL *= 1/NL
histMaxElecS *= 1/NS

histMaxMuonL *= 1/NL
histMaxMuonS *= 1/NS

histMaxProtL *= 1/NL
histMaxProtS *= 1/NS

histMaxNeutL *= 1/NL
histMaxNeutS *= 1/NS

histMaxPhotL *= 1/NL
histMaxPhotS *= 1/NS


histCloseNeutL *= 1/NL
histCloseNeutS *= 1/NS


histRatCPionPhotL *= 1/NL
histRatCPionPhotS *= 1/NS

histRatNPionElecL *= 1/NL
histRatNPionElecS *= 1/NS

histRatCPionMuonL *= 1/NL
histRatCPionMuonS *= 1/NS

histRatCKaonMuonL *= 1/NL
histRatCKaonMuonS *= 1/NS

histRatNKaonCPionL *= 1/NL
histRatNKaonCPionS *= 1/NS


file.Write()

