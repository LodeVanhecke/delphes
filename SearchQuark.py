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
histNZ = ROOT.TH1F("histNZ", "Number of Z bosons in a event",18 , 0, 18)
histNQ = ROOT.TH1F("histNQ", "Number of events with quark PDG ID",12, -6, 6)
histJetD = ROOT.TH1F("histGenJetD", "P_{T} of all GenJets from D", 100, 0, 70)
histJetU = ROOT.TH1F("histGenJetU", "P_{T} of all GenJets from U", 100, 0, 70)
histJetS = ROOT.TH1F("histGenJetS", "P_{T} of all GenJets from S", 100, 0, 70)
histJetC = ROOT.TH1F("histGenJetC", "P_{T} of all GenJets from C", 100, 0, 70)
histJetB = ROOT.TH1F("histGenJetB", "P_{T} of all GenJets from B", 100, 0, 70)
hist=[histJetD,histJetU,histJetS,histJetC,histJetB]

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
  
  for m in range(0,branchParticle.GetEntries()):
    particle = branchParticle.At(m)
    if particle.PID==23:
     if abs(branchParticle.At(particle.D1).PID)==abs(branchParticle.At(particle.D2).PID):
      histNQ.Fill(branchParticle.At(particle.D1).PID)
      histNQ.Fill(branchParticle.At(particle.D2).PID)
      NZ=NZ+1
      if abs(branchParticle.At(particle.D1).PID)==1:
       jetD = jetD+[entry]
      if abs(branchParticle.At(particle.D1).PID)==2:
       jetU = jetU+[entry]
      if abs(branchParticle.At(particle.D1).PID)==3:
       jetS = jetS+[entry]
      if abs(branchParticle.At(particle.D1).PID)==4:
       jetC = jetC+[entry]
      if abs(branchParticle.At(particle.D1).PID)==5:
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
    if jet.PT>10:
     # Plot jet transverse momentum
     if entry in jetD:
      histJetD.Fill(jet.PT)
     if entry in jetU:
      histJetU.Fill(jet.PT)
     if entry in jetS:
      histJetS.Fill(jet.PT)
     if entry in jetC:
      histJetC.Fill(jet.PT)
     if entry in jetB:
      histJetB.Fill(jet.PT)
     else:
      pass
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

 
c1=ROOT.TCanvas('c1','Number of Z bosons in a event')
histNZ.Draw()
c1.SaveAs("histNZ.pdf")
c2=ROOT.TCanvas('c2','Number of events with quark PDG ID')
histNQ.Draw()
c2.SaveAs("histNQ.pdf")
c3=ROOT.TCanvas('c3','PT of jets from D')
histJetD.Draw()
c3.SaveAs("histJetD.pdf")
c4=ROOT.TCanvas('c4','PT of jets from U')
histJetU.Draw()
c4.SaveAs("histJetU.pdf")
c5=ROOT.TCanvas('c5','PT of jets from S')
histJetS.Draw()
c5.SaveAs("histJetS.pdf")
c6=ROOT.TCanvas('c6','PT of jets from C')
histJetC.Draw()
c6.SaveAs("histJetC.pdf")
c7=ROOT.TCanvas('c7','PT of jets from B')
histJetB.Draw()
c7.SaveAs("histJetB.pdf")
input("Press Enter to continue...")
