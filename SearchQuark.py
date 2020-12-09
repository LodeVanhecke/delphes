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
histNZ = ROOT.TH1F("histNZ", "Number of Z bosons in a event",18 , 0, 18)
histNQ = ROOT.TH1F("histNQ", "Number of events with quark PDG ID",12, -6, 6)
histJetPTD = ROOT.TH1F("histGenJetPTD", "P_{T} of all GenJets from D", 100, 0, 50)
histJetPTU = ROOT.TH1F("histGenJetPTU", "P_{T} of all GenJets from U", 100, 0, 50)
histJetPTS = ROOT.TH1F("histGenJetPTS", "P_{T} of all GenJets from S", 100, 0, 50)
histJetPTC = ROOT.TH1F("histGenJetPTC", "P_{T} of all GenJets from C", 100, 0, 50)
histJetPTB = ROOT.TH1F("histGenJetPTB", "P_{T} of all GenJets from B", 100, 0, 50)
hist=[histJetPTD,histJetPTU,histJetPTS,histJetPTC,histJetPTB]
histNCKaonD = ROOT.TH1F("histNCKaonD", "Number of charged kaons in D jet", 10, 0, 10)
histNCKaonU = ROOT.TH1F("histNCKaonU", "Number of charged kaons in U jet", 10, 0, 10)
histNCKaonS = ROOT.TH1F("histNCKaonS", "Number of charged kaons in S jet", 10, 0, 10)
histNCKaonC = ROOT.TH1F("histNCKaonC", "Number of charged kaons in C jet", 10, 0, 10)
histNCKaonB = ROOT.TH1F("histNCKaonB", "Number of charged kaons in B jet", 10, 0, 10)
histNCPionD = ROOT.TH1F("histNCPionD", "Number of charged pions in D jet", 10, 0, 10)
histNCPionU = ROOT.TH1F("histNCPionU", "Number of charged pions in U jet", 10, 0, 10)
histNCPionS = ROOT.TH1F("histNCPionS", "Number of charged pions in S jet", 10, 0, 10)
histNCPionC = ROOT.TH1F("histNCPionC", "Number of charged pions in C jet", 10, 0, 10)
histNCPionB = ROOT.TH1F("histNCPionB", "Number of charged pions in B jet", 10, 0, 10)

jetD = []
jetU = []
jetS = []
jetC = []
jetB = []

p1 = ROOT.TLorentzVector()
lvofjet = ROOT.TLorentzVector()

# Loop over all events
for entry in range(0, numberOfEntries):
  # Load selected branches with data from specified event
  treeReader.ReadEntry(entry)
  
  NZ = 0
  
  for m in range(0,branchParticle.GetEntries()):
    particle = branchParticle.At(m)
    if particle.PID == 23:
     if abs(branchParticle.At(particle.D1).PID) == abs(branchParticle.At(particle.D2).PID):
      histNQ.Fill(branchParticle.At(particle.D1).PID)
      histNQ.Fill(branchParticle.At(particle.D2).PID)
      NZ = NZ+1
      if abs(branchParticle.At(particle.D1).PID) == 1:
       jetD = jetD+[entry]
      if abs(branchParticle.At(particle.D1).PID) == 2:
       jetU = jetU+[entry]
      if abs(branchParticle.At(particle.D1).PID) == 3:
       jetS = jetS+[entry]
      if abs(branchParticle.At(particle.D1).PID) == 4:
       jetC = jetC+[entry]
      if abs(branchParticle.At(particle.D1).PID) == 5:
       jetB =  jetB+[entry]
      else:
       pass
     else:
      pass
    else:
      pass


  histNZ.Fill(NZ)

  #PT of jets
  # If event contains at least 1 jet
  if branchGenJet.GetEntries() > 0:
   # Take all jets in event
   for l in range(0,branchGenJet.GetEntries()):
    jet = branchGenJet.At(l)
    lvofjet.SetPtEtaPhiM(jet.PT,jet.Eta,jet.Phi,jet.Mass)
    if jet.PT > 10:
     # Plot jet transverse momentum
     if entry in jetD:
      histJetPTD.Fill(jet.PT)
     if entry in jetU:
      histJetPTU.Fill(jet.PT)
     if entry in jetS:
      histJetPTS.Fill(jet.PT)
     if entry in jetC:
      histJetPTC.Fill(jet.PT)
     if entry in jetB:
      histJetPTB.Fill(jet.PT)
     else:
      pass
    else:
     pass


   # Fill histogram with number of kaons
    if branchParticle.GetEntries() > 0:
      # Take all particles
      Kaon=0
      for l in range(0,branchParticle.GetEntries()):
       particle = branchParticle.At(l)
       # filter Kaon(K+,K-) using PDG ID
       if abs(particle.PID) == 321:
        p1.SetPtEtaPhiM(particle.PT,particle.Eta,particle.Phi,particle.Mass)
        if p1.DeltaR(lvofjet) <= 0.4:
         Kaon = Kaon + 1
        else:
         pass
       else:
        pass
      if entry in jetD:
       histNCKaonD.Fill(Kaon)
      if entry in jetU:
       histNCKaonU.Fill(Kaon)
      if entry in jetS:
       histNCKaonS.Fill(Kaon)
      if entry in jetC:
       histNCKaonC.Fill(Kaon)
      if entry in jetB:
       histNCKaonB.Fill(Kaon)
      else:
       pass

    # Fill histogram with number of pions
    if branchParticle.GetEntries() > 0:
      # Take all particles
      Pion=0
      for l in range(0,branchParticle.GetEntries()):
       particle = branchParticle.At(l)
       # filter Pion(pi+,pi-) using PDG ID
       if abs(particle.PID) == 211:
        p1.SetPtEtaPhiM(particle.PT,particle.Eta,particle.Phi,particle.Mass)
        if p1.DeltaR(lvofjet) <= 0.4:
         Pion = Pion+1
        else:
         pass
       else:
        pass
      if entry in jetD:
       histNCPionD.Fill(Pion)
      if entry in jetU:
       histNCPionU.Fill(Pion)
      if entry in jetS:
       histNCPionS.Fill(Pion)
      if entry in jetC:
       histNCPionC.Fill(Pion)
      if entry in jetB:
       histNCPionB.Fill(Pion)
      else:
       pass


# Branching ratios

# Down
BR_D = 100* histNQ.GetBinContent(6)/(histNQ.GetEntries()/2)
#print(BR_D)

# Up
BR_U = 100* histNQ.GetBinContent(5)/(histNQ.GetEntries()/2)
#print(BR_U)

# Strange
BR_S = 100* histNQ.GetBinContent(4)/(histNQ.GetEntries()/2)
#print(BR_S)

# Charmed
BR_C = 100* histNQ.GetBinContent(3)/(histNQ.GetEntries()/2)

# Bottum
BR_B = 100* histNQ.GetBinContent(2)/(histNQ.GetEntries()/2)
print('C=',round(BR_C*100/((BR_U+BR_C)/2+(BR_D+BR_S+BR_B)/3+BR_C+BR_B),1),round(12.03*100/54.35,1))
print('B=',round(BR_B*100/((BR_U+BR_C)/2+(BR_D+BR_S+BR_B)/3+BR_C+BR_B),1),round(15.12*100/54.35,1))

BR1 = (BR_U+BR_C)/2
BR10 = 11.6
sigma_BR10 = 0.6
print('UC=',round(BR1*100/((BR_U+BR_C)/2+(BR_D+BR_S+BR_B)/3+BR_C+BR_B),1),round(BR10*100/54.35,1))
BR2 = (BR_D+BR_S+BR_B)/3
BR20 = 15.6
sigma_BR20 = 0.4
print('DSB=',round(BR2*100/((BR_U+BR_C)/2+(BR_D+BR_S+BR_B)/3+BR_C+BR_B),1),round(BR20*100/54.35,1))

file.Write()

#c1 = ROOT.TCanvas('c1','Number of Z bosons in a event')
#ROOT.gStyle.SetOptStat(0)
#histNZ.Draw()
#c1.SaveAs("histNZ.png")
#c2 = ROOT.TCanvas('c2','Number of events with quark PDG ID')
#ROOT.gStyle.SetOptStat(0)
#histNQ.Draw()
#c2.SaveAs("histNQ.png")
#c3 = ROOT.TCanvas('c3','PT of jets from quarks')
#ROOT.gStyle.SetOptStat(0)
#histJetPTD.SetLineColor(1)
#histJetPTD.DrawNormalized('same')
#histJetPTU.SetLineColor(2)
#histJetPTU.DrawNormalized('same')
#histJetPTS.SetLineColor(3)
#histJetPTS.DrawNormalized('same')
#histJetPTC.SetLineColor(4)
#histJetPTC.DrawNormalized('same')
#histJetPTB.SetLineColor(5)
#histJetPTB.DrawNormalized('same')
#c3.BuildLegend()
#histJetPTD.SetTitle('PT of jets from quarks')
#c3.SaveAs("histJet.pdf")
