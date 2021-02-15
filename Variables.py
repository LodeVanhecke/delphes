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
histNZ = ROOT.TH1F("histNZ", "Number of Z bosons in a event",18 , 0, 18)
histNQ = ROOT.TH1F("histNQ", "Number of events with quark PDG ID",12, -6, 6)

#histJetPTD = ROOT.TH1F("histGenJetPTD", "P_{T} of all GenJets from D", 100, 0, 50)
histJetPTL = ROOT.TH1F("histGenJetPTL", "P_{T} of all GenJets from L", 100, 0, 50)
histJetPTS = ROOT.TH1F("histGenJetPTS", "P_{T} of all GenJets from S", 100, 0, 50)
histJetPTC = ROOT.TH1F("histGenJetPTC", "P_{T} of all GenJets from C", 100, 0, 50)
histJetPTB = ROOT.TH1F("histGenJetPTB", "P_{T} of all GenJets from B", 100, 0, 50)
#hist=[histJetPTL,histJetPTS,histJetPTC,histJetPTB]

#histJetCD = ROOT.TH1F("histJetCD", "Total charge of D jet", 20, -10, 10)
histJetCL = ROOT.TH1F("histJetCL", "Total charge of L jet", 20, -10, 10)
histJetCS = ROOT.TH1F("histJetCS", "Total charge of S jet", 20, -10, 10)
histJetCC = ROOT.TH1F("histJetCC", "Total charge of C jet", 20, -10, 10)
histJetCB = ROOT.TH1F("histJetCB", "Total charge of B jet", 20, -10, 10)

#histNCKaonD = ROOT.TH1F("histNCKaonD", "Number of charged kaons in D jet", 10, 0, 10)
histNCKaonL = ROOT.TH1F("histNCKaonL", "Number of charged kaons in L jet", 10, 0, 10)
histNCKaonS = ROOT.TH1F("histNCKaonS", "Number of charged kaons in S jet", 10, 0, 10)
histNCKaonC = ROOT.TH1F("histNCKaonC", "Number of charged kaons in C jet", 10, 0, 10)
histNCKaonB = ROOT.TH1F("histNCKaonB", "Number of charged kaons in B jet", 10, 0, 10)

histCKaonPTL = ROOT.TH1F("histCKaonPTL", "P_{T} of charged kaons in L jet", 100, 0, 50)
histCKaonPTS = ROOT.TH1F("histCKaonPTS", "P_{T} of charged kaons in S jet", 100, 0, 50)
histCKaonPTC = ROOT.TH1F("histCKaonPTC", "P_{T} of charged kaons in C jet", 100, 0, 50)
histCKaonPTB = ROOT.TH1F("histCKaonPTB", "P_{T} of charged kaons in B jet", 100, 0, 50)

#histNNKaonD = ROOT.TH1F("histNNKaonD", "Number of neutral kaons in D jet", 10, 0, 10)
histNNKaonL = ROOT.TH1F("histNNKaonL", "Number of neutral kaons in L jet", 10, 0, 10)
histNNKaonS = ROOT.TH1F("histNNKaonS", "Number of neutral kaons in S jet", 10, 0, 10)
histNNKaonC = ROOT.TH1F("histNNKaonC", "Number of neutral kaons in C jet", 10, 0, 10)
histNNKaonB = ROOT.TH1F("histNNKaonB", "Number of neutral kaons in B jet", 10, 0, 10)

histNKaonPTL = ROOT.TH1F("histNKaonPTL", "P_{T} of neutral kaons in L jet", 100, 0, 50)
histNKaonPTS = ROOT.TH1F("histNKaonPTS", "P_{T} of neutral kaons in S jet", 100, 0, 50)
histNKaonPTC = ROOT.TH1F("histNKaonPTC", "P_{T} of neutral kaons in C jet", 100, 0, 50)
histNKaonPTB = ROOT.TH1F("histNKaonPTB", "P_{T} of neutral kaons in B jet", 100, 0, 50)

#histNCPionD = ROOT.TH1F("histNCPionD", "Number of charged pions in D jet", 10, 0, 10)
histNCPionL = ROOT.TH1F("histNCPionL", "Number of charged pions in L jet", 10, 0, 10)
histNCPionS = ROOT.TH1F("histNCPionS", "Number of charged pions in S jet", 10, 0, 10)
histNCPionC = ROOT.TH1F("histNCPionC", "Number of charged pions in C jet", 10, 0, 10)
histNCPionB = ROOT.TH1F("histNCPionB", "Number of charged pions in B jet", 10, 0, 10)

histCPionPTL = ROOT.TH1F("histCPionPTL", "P_{T} of charged pions in L jet", 100, 0, 50)
histCPionPTS = ROOT.TH1F("histCPionPTS", "P_{T} of charged pions in S jet", 100, 0, 50)
histCPionPTC = ROOT.TH1F("histCPionPTC", "P_{T} of charged pions in C jet", 100, 0, 50)
histCPionPTB = ROOT.TH1F("histCPionPTB", "P_{T} of charged pions in B jet", 100, 0, 50)

#histNNPionD = ROOT.TH1F("histNNPionD", "Number of neutral pions in D jet", 10, 0, 10)
histNNPionL = ROOT.TH1F("histNNPionL", "Number of neutral pions in L jet", 10, 0, 10)
histNNPionS = ROOT.TH1F("histNNPionS", "Number of neutral pions in S jet", 10, 0, 10)
histNNPionC = ROOT.TH1F("histNNPionC", "Number of neutral pions in C jet", 10, 0, 10)
histNNPionB = ROOT.TH1F("histNNPionB", "Number of neutral pions in B jet", 10, 0, 10)

histNPionPTL = ROOT.TH1F("histNPionPTL", "P_{T} of neutral pions in L jet", 100, 0, 50)
histNPionPTS = ROOT.TH1F("histNPionPTS", "P_{T} of neutral pions in S jet", 100, 0, 50)
histNPionPTC = ROOT.TH1F("histNPionPTC", "P_{T} of neutral pions in C jet", 100, 0, 50)
histNPionPTB = ROOT.TH1F("histNPionPTB", "P_{T} of neutral pions in B jet", 100, 0, 50)

jetL = []
jetS = []
jetC = []
jetB = []

p1 = ROOT.TLorentzVector()
lvofjet = ROOT.TLorentzVector()
t1 = ROOT.TVector3()

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
       jetL = jetL+[entry]
      if abs(branchParticle.At(particle.D1).PID) == 2:
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


  histNZ.Fill(NZ)

  #PT of jets
  # If event contains at least 1 jet
  if branchGenJet.GetEntries() > 0:
   # Take all jets in event
   for i in range(0,branchGenJet.GetEntries()):
    jet = branchGenJet.At(i)
    lvofjet.SetPtEtaPhiM(jet.PT,jet.Eta,jet.Phi,jet.Mass)
    if jet.PT > 10:
     # Plot jet transverse momentum
     if entry in jetL:
      histJetPTL.Fill(jet.PT)
   #  if entry in jetU:
   #   histJetPTU.Fill(jet.PT)
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


     # Fill histogram with number of kaons/ Charge of jet
     if branchParticle.GetEntries() > 0:
       # Take all particles
       Kaon = 0
       Kaon0 = 0
       Pion = 0
       Pion0 = 0
       Charge = 0
       ParticlePT = 0
       for l in range(0,branchParticle.GetEntries()):
        particle = branchParticle.At(l)
        p1.SetPtEtaPhiM(particle.PT,particle.Eta,particle.Phi,particle.Mass)
        if p1.DeltaR(lvofjet) <= 0.4:
         # filter Kaon(K+,K-)
         if abs(particle.PID) == 321:
          Kaon = Kaon + 1
          if entry in jetL:
           histCKaonPTL.Fill(particle.PT)
          if entry in jetS:
           histCKaonPTS.Fill(particle.PT)
          if entry in jetC:
           histCKaonPTC.Fill(particle.PT)
          if entry in jetB:
           histCKaonPTB.Fill(particle.PT)
          else:
           pass
         # filter neutral Kaon
         if abs(particle.PID) == 311:
          Kaon0= Kaon0 + 1
          if entry in jetL:
           histNKaonPTL.Fill(particle.PT)
          if entry in jetS:
           histNKaonPTS.Fill(particle.PT)
          if entry in jetC:
           histNKaonPTC.Fill(particle.PT)
          if entry in jetB:
           histNKaonPTB.Fill(particle.PT)
          else:
           pass
         # filter Pion(P+,P-)
         if abs(particle.PID) == 211:
          Pion = Pion + 1
          if entry in jetL:
           histCPionPTL.Fill(particle.PT)
          if entry in jetS:
           histCPionPTS.Fill(particle.PT)
          if entry in jetC:
           histCPionPTC.Fill(particle.PT)
          if entry in jetB:
           histCPionPTB.Fill(particle.PT)
          else:
           pass
         #filter neutral pion
         if abs(particle.PID) == 111:
          Pion0 = Pion0 + 1
          if entry in jetL:
           histNPionPTL.Fill(particle.PT)
          if entry in jetS:
           histNPionPTS.Fill(particle.PT)
          if entry in jetC:
           histNPionPTC.Fill(particle.PT)
          if entry in jetB:
           histNPionPTB.Fill(particle.PT)
          else:
           pass
         else:
          pass
        # charge
        Charge = Charge + particle.Charge*particle.PT
        ParticlePT = ParticlePT + particle.PT
       Charge = Charge/ParticlePT
       if entry in jetL:
        histNCKaonL.Fill(Kaon)
        histNNKaonL.Fill(Kaon0)
        histNCPionL.Fill(Pion)
        histNNPionL.Fill(Pion0)
        histJetCL.Fill(Charge)
      # if entry in jetU:
      #  histNCKaonU.Fill(Kaon)
      #  histNNKaonU.Fill(Kaon0)
      #  histNCPionU.Fill(Pion)
      #  histNNPionU.Fill(Pion0)
      #  histJetCU.Fill(Charge)
       if entry in jetS:
        histNCKaonS.Fill(Kaon)
        histNNKaonS.Fill(Kaon0)
        histNCPionS.Fill(Pion)
        histNNPionS.Fill(Pion0)
        histJetCS.Fill(Charge)
       if entry in jetC:
        histNCKaonC.Fill(Kaon)
        histNNKaonC.Fill(Kaon0)
        histNCPionC.Fill(Pion)
        histNNPionC.Fill(Pion0)
        histJetCC.Fill(Charge)
       if entry in jetB:
        histNCKaonB.Fill(Kaon)
        histNNKaonB.Fill(Kaon0)
        histNCPionB.Fill(Pion)
        histNNPionB.Fill(Pion0)
        histJetCB.Fill(Charge)
       else:
        pass



file.Write()
