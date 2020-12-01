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
histGenJetPT = ROOT.TH1F("histGenJetPT", "P_{T} of all GenJets", 100, 0, 70)
histParticlePT = ROOT.TH1F("HistparticlePT", "P_{T} of all kaons", 100, 0, 50)
histNJet = ROOT.TH1F("histNJet", "Number of jets in a event",18 , 0, 18)
histAngle = ROOT.TH1F("histAngle", "Angle between Kaon and Jet",100 , 0, 2*math.pi)
histMK = ROOT.TH1F("histMK", "Invariant mass of two kaons",100 , 0, 100)
histMJ = ROOT.TH1F("histMJ", "Total invariant mass of jets in a event",100 , 0, 100)
histMJ2 = ROOT.TH1F("histMJ2", "Max invariant mass of two jets in a event",100 , 0, 100)

# Loop over all events
for entry in range(0, numberOfEntries):
  # Load selected branches with data from specified event
  treeReader.ReadEntry(entry)

  histNJet.Fill(branchGenJet.GetEntries())
  
  p1=ROOT.TLorentzVector()
  p2=ROOT.TLorentzVector()
  lvofjet=ROOT.TLorentzVector()
  lvofjet2=ROOT.TLorentzVector()
  jets=ROOT.TLorentzVector()
  
  jetsM=[]
  
  # If event contains at least 1 jet
  if branchGenJet.GetEntries() > 0:
    # Take all jets in event
    for i in range(0,branchGenJet.GetEntries()):
     jet = branchGenJet.At(i)
     if jet.PT>10:
      # Plot jet transverse momentum
      histGenJetPT.Fill(jet.PT)
      # Set Lv of jet
      lvofjet.SetPtEtaPhiM(jet.PT,jet.Eta,jet.Phi,jet.Mass)
      # Total Lv of all jets in event
      jets=jets+lvofjet
      # Loop over all jets in event
      for j in range(0+i,branchGenJet.GetEntries()):
       # Filter same jets
       if j==i:
        pass
       if j!=i:
        jet2 = branchGenJet.At(j)
        lvofjet2.SetPtEtaPhiM(jet2.PT,jet2.Eta,jet2.Phi,jet2.Mass)
        # Invariant mass of two jets
        jetsM=jetsM+[(lvofjet+lvofjet2).M()]
      # Plotting the angle between kaons and jet
      if branchParticle.GetEntries() > 0:
       for l in range(0,branchParticle.GetEntries()):
        particle = branchParticle.At(l)
        # filter Kaon(K+,K-) using PDG ID
        if abs(particle.PID)==321:
         p1.SetPtEtaPhiM(particle.PT,particle.Eta,particle.Phi,particle.Mass)
         histAngle.Fill(p1.Vect().Angle(lvofjet.Vect()))
     else:
      break

  # Fill histogram with PT of all kaons
  if branchParticle.GetEntries() > 0:
    # Take all particles
    for l in range(0,branchParticle.GetEntries()):
     particle = branchParticle.At(l)
     # filter Kaon(K+,K-) using PDG ID
     if abs(particle.PID)==321:
      p1.SetPtEtaPhiM(particle.PT,particle.Eta,particle.Phi,particle.Mass)
      histParticlePT.Fill(particle.PT)
      # Take all particles for the second time
      #for m in range(0,branchParticle.GetEntries()):
      # particle2 = branchParticle.At(m)
      # if m==l:
      #  pass
      # if m!=l:
      #  if abs(particle2.PID)==321:
      #   p2.SetPtEtaPhiM(particle2.PT,particle2.Eta,particle2.Phi,particle2.Mass)
      #   # Plot invariant mass of all kaon combinations
      #   #histMK.Fill((p1+p2).M())
      #   break

  try:
   # Plot max invariant mass of two jets in event
   histMJ2.Fill(max(jetsM))
  except:
   pass
  # Plot total invariant mass of jets in event
  histMJ.Fill(jets.M())
# Show resulting histogram
c1=ROOT.TCanvas('c1','P_{T} of all GenJets')
histGenJetPT.Draw()
c2=ROOT.TCanvas('c2','P_{T} of all kaons')
histParticlePT.Draw()
c3=ROOT.TCanvas('c3','Number of jets in a event')
histNJet.Draw()
c4=ROOT.TCanvas('c4','Angle between Kaon and Jet')
histAngle.Draw()
#c5=ROOT.TCanvas('c5','Invariant mass of two kaons')
#histMK.Draw()
c6=ROOT.TCanvas('c6','Total invariant mass of jets in a event')
histMJ.Draw()
c7=ROOT.TCanvas('c7','Max invariant mass of two jets in a event')
histMJ2.Draw()

input("Press Enter to continue...")

