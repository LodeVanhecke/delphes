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



histMaxCKaonL = ROOT.TH2F("histMaxCKaonL", "Angle/pseudoRap of max charged kaons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxCKaonS = ROOT.TH2F("histMaxCKaonS", "Angle/pseudoRap of max charged kaons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxCKaonC = ROOT.TH2F("histMaxCKaonC", "Angle/pseudoRap of max charged kaons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxCKaonB = ROOT.TH2F("histMaxCKaonB", "Angle/pseudoRap of max charged kaons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)

histMaxNKaonL = ROOT.TH2F("histMaxNKaonL", "Angle/pseudoRap of max neutral kaons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNKaonS = ROOT.TH2F("histMaxNKaonS", "Angle/pseudoRap of max neutral kaons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNKaonC = ROOT.TH2F("histMaxNKaonC", "Angle/pseudoRap of max neutral kaons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNKaonB = ROOT.TH2F("histMaxNKaonB", "Angle/pseudoRap of max neutral kaons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histMaxCPionL = ROOT.TH2F("histMaxCPionL", "Angle/pseudoRap of max charged pions in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxCPionS = ROOT.TH2F("histMaxCPionS", "Angle/pseudoRap of max charged pions in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxCPionC = ROOT.TH2F("histMaxCPionC", "Angle/pseudoRap of max charged pions in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxCPionB = ROOT.TH2F("histMaxCPionB", "Angle/pseudoRap of max charged pions in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)

histMaxNPionL = ROOT.TH2F("histMaxNPionL", "Angle/pseudoRap of max neutral pions in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNPionS = ROOT.TH2F("histMaxNPionS", "Angle/pseudoRap of max neutral pions in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNPionC = ROOT.TH2F("histMaxNPionC", "Angle/pseudoRap of max neutral pions in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNPionB = ROOT.TH2F("histMaxNPionB", "Angle/pseudoRap of max neutral pions in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histMaxElecL = ROOT.TH2F("histMaxElecL", "Angle/pseudoRap of max electrons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxElecS = ROOT.TH2F("histMaxElecS", "Angle/pseudoRap of max electrons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxElecC = ROOT.TH2F("histMaxElecC", "Angle/pseudoRap of max electrons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxElecB = ROOT.TH2F("histMaxElecB", "Angle/pseudoRap of max electrons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histMaxMuonL = ROOT.TH2F("histMaxMuonL", "Angle/pseudoRap of max muons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxMuonS = ROOT.TH2F("histMaxMuonS", "Angle/pseudoRap of max muons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxMuonC = ROOT.TH2F("histMaxMuonC", "Angle/pseudoRap of max muons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxMuonB = ROOT.TH2F("histMaxMuonB", "Angle/pseudoRap of max muons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histMaxProtL = ROOT.TH2F("histMaxProtL", "Angle/pseudoRap of max protons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxProtS = ROOT.TH2F("histMaxProtS", "Angle/pseudoRap of max protons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxProtC = ROOT.TH2F("histMaxProtC", "Angle/pseudoRap of max protons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxProtB = ROOT.TH2F("histMaxProtB", "Angle/pseudoRap of max protons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histMaxNeutL = ROOT.TH2F("histMaxNeutL", "Angle/pseudoRap of max neutrons in L jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNeutS = ROOT.TH2F("histMaxNeutS", "Angle/pseudoRap of max neutrons in S jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNeutC = ROOT.TH2F("histMaxNeutC", "Angle/pseudoRap of max neutrons in C jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)
histMaxNeutB = ROOT.TH2F("histMaxNeutB", "Angle/pseudoRap of max neutrons in B jet", 1000, -0.6, 0.6, 1000, -0.6, 0.6)


histDCKaonL = ROOT.TH2F("histDCKaonL", "dx/dy of charged kaons in L jet", 1000, -10, 10, 1000, -10, 10)
histDCKaonS = ROOT.TH2F("histDCKaonS", "dx/dy of charged kaons in S jet", 1000, -10, 10, 1000, -10, 10)
histDCKaonC = ROOT.TH2F("histDCKaonC", "dx/dy of charged kaons in C jet", 1000, -10, 10, 1000, -10, 10)
histDCKaonB = ROOT.TH2F("histDCKaonB", "dx/dy of charged kaons in B jet", 1000, -10, 10, 1000, -10, 10)

histDNKaonL = ROOT.TH2F("histDNKaonL", "dx/dy of neutral kaons in L jet", 1000, -10, 10, 1000, -10, 10)
histDNKaonS = ROOT.TH2F("histDNKaonS", "dx/dy of neutral kaons in S jet", 1000, -10, 10, 1000, -10, 10)
histDNKaonC = ROOT.TH2F("histDNKaonC", "dx/dy of neutral kaons in C jet", 1000, -10, 10, 1000, -10, 10)
histDNKaonB = ROOT.TH2F("histDNKaonB", "dx/dy of neutral kaons in B jet", 1000, -10, 10, 1000, -10, 10)


histDCPionL = ROOT.TH2F("histDCPionL", "dx/dy of charged pions in L jet", 1000, -10, 10, 1000, -10, 10)
histDCPionS = ROOT.TH2F("histDCPionS", "dx/dy of charged pions in S jet", 1000, -10, 10, 1000, -10, 10)
histDCPionC = ROOT.TH2F("histDCPionC", "dx/dy of charged pions in C jet", 1000, -10, 10, 1000, -10, 10)
histDCPionB = ROOT.TH2F("histDCPionB", "dx/dy of charged pions in B jet", 1000, -10, 10, 1000, -10, 10)

histDNPionL = ROOT.TH2F("histDNPionL", "dx/dy of neutral pions in L jet", 1000, -10, 10, 1000, -10, 10)
histDNPionS = ROOT.TH2F("histDNPionS", "dx/dy of neutral pions in S jet", 1000, -10, 10, 1000, -10, 10)
histDNPionC = ROOT.TH2F("histDNPionC", "dx/dy of neutral pions in C jet", 1000, -10, 10, 1000, -10, 10)
histDNPionB = ROOT.TH2F("histDNPionB", "dx/dy of neutral pions in B jet", 1000, -10, 10, 1000, -10, 10)


histDElecL = ROOT.TH2F("histDElecL", "dx/dy of electrons in L jet", 1000, -10, 10, 1000, -10, 10)
histDElecS = ROOT.TH2F("histDElecS", "dx/dy of electrons in S jet", 1000, -10, 10, 1000, -10, 10)
histDElecC = ROOT.TH2F("histDElecC", "dx/dy of electrons in C jet", 1000, -10, 10, 1000, -10, 10)
histDElecB = ROOT.TH2F("histDElecB", "dx/dy of electrons in B jet", 1000, -10, 10, 1000, -10, 10)


histDMuonL = ROOT.TH2F("histDMuonL", "dx/dy of muons in L jet", 1000, -10, 10, 1000, -10, 10)
histDMuonS = ROOT.TH2F("histDMuonS", "dx/dy of muons in S jet", 1000, -10, 10, 1000, -10, 10)
histDMuonC = ROOT.TH2F("histDMuonC", "dx/dy of muons in C jet", 1000, -10, 10, 1000, -10, 10)
histDMuonB = ROOT.TH2F("histDMuonB", "dx/dy of muons in B jet", 1000, -10, 10, 1000, -10, 10)


histDProtL = ROOT.TH2F("histDProtL", "dx/dy of protons in L jet", 1000, -10, 10, 1000, -10, 10)
histDProtS = ROOT.TH2F("histDProtS", "dx/dy of protons in S jet", 1000, -10, 10, 1000, -10, 10)
histDProtC = ROOT.TH2F("histDProtC", "dx/dy of protons in C jet", 1000, -10, 10, 1000, -10, 10)
histDProtB = ROOT.TH2F("histDProtB", "dx/dy of protons in B jet", 1000, -10, 10, 1000, -10, 10)


histDNeutL = ROOT.TH2F("histDNeutL", "dx/dy of neutrons in L jet", 1000, -10, 10, 1000, -10, 10)
histDNeutS = ROOT.TH2F("histDNeutS", "dx/dy of neutrons in S jet", 1000, -10, 10, 1000, -10, 10)
histDNeutC = ROOT.TH2F("histDNeutC", "dx/dy of neutrons in C jet", 1000, -10, 10, 1000, -10, 10)
histDNeutB = ROOT.TH2F("histDNeutB", "dx/dy of neutrons in B jet", 1000, -10, 10, 1000, -10, 10)


NL = 0
NS = 0
NC = 0
NB = 0


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
  histNJetL.Fill(NJet)
 if q.PID == 3:
  NS += 1
  histNJetS.Fill(NJet)
 if q.PID == 4:
  NC += 1
  histNJetC.Fill(NJet)
 if q.PID == 5:
  NB += 1
  histNJetB.Fill(NJet)
  
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


 for i in range(0,branchParticle.GetEntries()):
  p1 = ROOT.TLorentzVector()
  particle2 = branchParticle.At(i)
  p1.SetPtEtaPhiM(particle2.PT,particle2.Eta,particle2.Phi,particle2.Mass)
  if particle2.PT > 1:
   if p1.DeltaR(Jetqlv) < p1.DeltaR(Jetqbarlv): 
    if p1.DeltaR(Jetqlv) <= 0.5:
     if abs(particle2.PID) == 321:    
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CKaonL[2]: CKaonL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCKaonL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CKaonS[2]: CKaonS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCKaonS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CKaonC[2]: CKaonC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCKaonC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CKaonB[2]: CKaonB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCKaonB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 311:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NKaonL[2]: NKaonL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNKaonL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NKaonS[2]: NKaonS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNKaonS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NKaonC[2]: NKaonC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNKaonC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NKaonB[2]: NKaonB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNKaonB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 211:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CPionL[2]: CPionL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCPionL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CPionS[2]: CPionS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCPionS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CPionC[2]: CPionC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCPionC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > CPionB[2]: CPionB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDCPionB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 111:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NPionL[2]: NPionL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNPionL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NPionS[2]: NPionS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNPionS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NPionC[2]: NPionC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNPionC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NPionB[2]: NPionB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNPionB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 11:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecL[2]: ElecL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecS[2]: ElecS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecC[2]: ElecC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecB[2]: ElecB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 13:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonL[2]: MuonL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonS[2]: MuonS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonC[2]: MuonC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonB[2]: MuonB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if particle2.PID == 2212:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtL[2]: ProtL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtS[2]: ProtS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtC[2]: ProtC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtB[2]: ProtB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if particle2.PID == 2112:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutL[2]: NeutL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutS[2]: NeutS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutC[2]: NeutC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutB[2]: NeutB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
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
       if particle2.PT > CKaonL[2]: CKaonL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCKaonL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > CKaonS[2]: CKaonS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCKaonS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > CKaonC[2]: CKaonC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCKaonC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > CKaonB[2]: CKaonB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCKaonB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCKaonB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 311:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NKaonL[2]: NKaonL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNKaonL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NKaonS[2]: NKaonS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNKaonS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NKaonC[2]: NKaonC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNKaonC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NKaonB[2]: NKaonB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNKaonB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNKaonB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 211:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > CPionL[2]: CPionL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCPionL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > CPionS[2]: CPionS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCPionS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > CPionC[2]: CPionC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCPionC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > CPionB[2]: CPionB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histCPionB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDCPionB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 111:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NPionL[2]: NPionL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionL.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNPionL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NPionS[2]: NPionS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionS.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNPionS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NPionC[2]: NPionC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionC.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNPionC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetqbar.PT
       Eta = Jetqbarlv.Eta()-p1.Eta()
       if particle2.PT > NPionB[2]: NPionB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNPionB.Fill(p1.DeltaPhi(Jetqbarlv),Eta,PT)
       histDNPionB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 11:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecL[2]: ElecL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecS[2]: ElecS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecC[2]: ElecC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ElecB[2]: ElecB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histElecB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDElecB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if abs(particle2.PID) == 13:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonL[2]: MuonL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonS[2]: MuonS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonC[2]: MuonC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > MuonB[2]: MuonB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histMuonB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDMuonB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if particle2.PID == 2212:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtL[2]: ProtL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtS[2]: ProtS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtC[2]: ProtC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > ProtB[2]: ProtB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histProtB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDProtB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     if particle2.PID == 2112:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutL[2]: NeutL = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutL.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutL.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutS[2]: NeutS = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutS.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutS.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 4:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutC[2]: NeutC = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutC.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutC.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
      if q.PID == 5:
       PT = abs(particle2.PT)/Jetq.PT
       Eta = Jetqlv.Eta()-p1.Eta()
       if particle2.PT > NeutB[2]: NeutB = [p1.DeltaPhi(Jetqlv),Eta,PT]
       histNeutB.Fill(p1.DeltaPhi(Jetqlv),Eta,PT)
       histDNeutB.Fill(math.sin(p1.DeltaPhi(Jetqlv))*particle2.D0,math.cos(p1.DeltaPhi(Jetqlv))*particle2.D0,PT)
     else:
      continue
    else:
     continue
   else:
    continue
  else:
   continue
 
 histMaxCKaonL.Fill(CKaonL[0],CKaonL[1],CKaonL[2])
 histMaxCKaonS.Fill(CKaonS[0],CKaonS[1],CKaonS[2])
 histMaxCKaonC.Fill(CKaonC[0],CKaonC[1],CKaonC[2])
 histMaxCKaonB.Fill(CKaonB[0],CKaonB[1],CKaonB[2])

 histMaxNKaonL.Fill(NKaonL[0],NKaonL[1],NKaonL[2])
 histMaxNKaonS.Fill(NKaonS[0],NKaonS[1],NKaonS[2])
 histMaxNKaonC.Fill(NKaonC[0],NKaonC[1],NKaonC[2])
 histMaxNKaonB.Fill(NKaonB[0],NKaonB[1],NKaonB[2])

 histMaxCPionL.Fill(CPionL[0],CPionL[1],CPionL[2])
 histMaxCPionS.Fill(CPionS[0],CPionS[1],CPionS[2])
 histMaxCPionC.Fill(CPionC[0],CPionC[1],CPionC[2])
 histMaxCPionB.Fill(CPionB[0],CPionB[1],CPionB[2])

 histMaxNPionL.Fill(NPionL[0],NPionL[1],NPionL[2])
 histMaxNPionS.Fill(NPionS[0],NPionS[1],NPionS[2])
 histMaxNPionC.Fill(NPionC[0],NPionC[1],NPionC[2])
 histMaxNPionB.Fill(NPionB[0],NPionB[1],NPionB[2])

 histMaxElecL.Fill(ElecL[0],ElecL[1],ElecL[2])
 histMaxElecS.Fill(ElecS[0],ElecS[1],ElecS[2])
 histMaxElecC.Fill(ElecC[0],ElecC[1],ElecC[2])
 histMaxElecB.Fill(ElecB[0],ElecB[1],ElecB[2])

 histMaxMuonL.Fill(MuonL[0],MuonL[1],MuonL[2])
 histMaxMuonS.Fill(MuonS[0],MuonS[1],MuonS[2])
 histMaxMuonC.Fill(MuonC[0],MuonC[1],MuonC[2])
 histMaxMuonB.Fill(MuonB[0],MuonB[1],MuonB[2])

 histMaxProtL.Fill(ProtL[0],ProtL[1],ProtL[2])
 histMaxProtS.Fill(ProtS[0],ProtS[1],ProtS[2])
 histMaxProtC.Fill(ProtC[0],ProtC[1],ProtC[2])
 histMaxProtB.Fill(ProtB[0],ProtB[1],ProtB[2])

 histMaxNeutL.Fill(NeutL[0],NeutL[1],NeutL[2])
 histMaxNeutS.Fill(NeutS[0],NeutS[1],NeutS[2])
 histMaxNeutC.Fill(NeutC[0],NeutC[1],NeutC[2])
 histMaxNeutB.Fill(NeutB[0],NeutB[1],NeutB[2])


# Normalize hists

histCKaonL *= 1/NL
histCKaonS *= 1/NS
histCKaonC *= 1/NC
histCKaonB *= 1/NB

histNKaonL *= 1/NL
histNKaonS *= 1/NS
histNKaonC *= 1/NC
histNKaonB *= 1/NB

histCPionL *= 1/NL
histCPionS *= 1/NS
histCPionC *= 1/NC
histCPionB *= 1/NB

histNPionL *= 1/NL
histNPionS *= 1/NS
histNPionC *= 1/NC
histNPionB *= 1/NB

histElecL *= 1/NL
histElecS *= 1/NS
histElecC *= 1/NC
histElecB *= 1/NB

histMuonL *= 1/NL
histMuonS *= 1/NS
histMuonC *= 1/NC
histMuonB *= 1/NB

histProtL *= 1/NL
histProtS *= 1/NS
histProtC *= 1/NC
histProtB *= 1/NB

histNeutL *= 1/NL
histNeutS *= 1/NS
histNeutC *= 1/NC
histNeutB *= 1/NB


histMaxCKaonL *= 1/NL
histMaxCKaonS *= 1/NS
histMaxCKaonC *= 1/NC
histMaxCKaonB *= 1/NB

histMaxNKaonL *= 1/NL
histMaxNKaonS *= 1/NS
histMaxNKaonC *= 1/NC
histMaxNKaonB *= 1/NB

histMaxCPionL *= 1/NL
histMaxCPionS *= 1/NS
histMaxCPionC *= 1/NC
histMaxCPionB *= 1/NB

histMaxNPionL *= 1/NL
histMaxNPionS *= 1/NS
histMaxNPionC *= 1/NC
histMaxNPionB *= 1/NB

histMaxElecL *= 1/NL
histMaxElecS *= 1/NS
histMaxElecC *= 1/NC
histMaxElecB *= 1/NB

histMaxMuonL *= 1/NL
histMaxMuonS *= 1/NS
histMaxMuonC *= 1/NC
histMaxMuonB *= 1/NB

histMaxProtL *= 1/NL
histMaxProtS *= 1/NS
histMaxProtC *= 1/NC
histMaxProtB *= 1/NB

histMaxNeutL *= 1/NL
histMaxNeutS *= 1/NS
histMaxNeutC *= 1/NC
histMaxNeutB *= 1/NB


histDCKaonL *= 1/NL
histDCKaonS *= 1/NS
histDCKaonC *= 1/NC
histDCKaonB *= 1/NB

histDNKaonL *= 1/NL
histDNKaonS *= 1/NS
histDNKaonC *= 1/NC
histDNKaonB *= 1/NB

histDCPionL *= 1/NL
histDCPionS *= 1/NS
histDCPionC *= 1/NC
histDCPionB *= 1/NB

histDNPionL *= 1/NL
histDNPionS *= 1/NS
histDNPionC *= 1/NC
histDNPionB *= 1/NB

histDElecL *= 1/NL
histDElecS *= 1/NS
histDElecC *= 1/NC
histDElecB *= 1/NB

histDMuonL *= 1/NL
histDMuonS *= 1/NS
histDMuonC *= 1/NC
histDMuonB *= 1/NB

histDProtL *= 1/NL
histDProtS *= 1/NS
histDProtC *= 1/NC
histDProtB *= 1/NB

histDNeutL *= 1/NL
histDNeutS *= 1/NS
histDNeutC *= 1/NC
histDNeutB *= 1/NB


file.Write()
