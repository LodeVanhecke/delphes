import sys
import ROOT
import math
import numpy as np
import root_numpy
import PIL.Image as Image

try:
  input = raw_input
except:
  pass

if len(sys.argv) < 2:
  print(" Usage: Example1.py input_file")
  sys.exit(1)


ROOT.gSystem.Load("/home/user/delphes/libDelphes")

try:
  ROOT.gInterpreter.Declare('#include "/home/user/delphes/classes/DelphesClasses.h"')
  ROOT.gInterpreter.Declare('#include "/home/user/delphes/external/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass


inputFile = "/home/user/delphes/"+sys.argv[1]

# Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchGenJet = treeReader.UseBranch("GenJet")
branchParticle  = treeReader.UseBranch("Particle")

# Read file
file = ROOT.TFile(sys.argv[1][:-5] +'_out.root','RECREATE')

ArrayCKaonL = []
ArrayCKaonS = []

# Loop over all events
for entry in range(0, 50):
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

 # Book histograms
 histJetCKaonLq = ROOT.TH2F("histJetCKaonLq","", 50, -0.5, 0.5, 50, -0.5, 0.5)
 histJetCKaonLqbar = ROOT.TH2F("histJetCKaonLqbar","", 50, -0.5, 0.5, 50, -0.5, 0.5)
 histJetCKaonSq = ROOT.TH2F("histJetCKaonSq","", 50, -0.5, 0.5, 50, -0.5, 0.5)
 histJetCKaonSqbar = ROOT.TH2F("histJetCKaonSqbar","", 50, -0.5, 0.5, 50, -0.5, 0.5)

 # Fill histograms
 for i in range(0,branchParticle.GetEntries()):
  p1 = ROOT.TLorentzVector()
  particle2 = branchParticle.At(i)
  p1.SetPtEtaPhiM(particle2.PT,particle2.Eta,particle2.Phi,particle2.Mass)
  if particle2.PT > 10:
   if p1.DeltaR(Jetqlv) < p1.DeltaR(Jetqbarlv):
    if p1.DeltaR(Jetqlv) <= 0.5:
     if abs(particle2.PID) == 321:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetCKaonLq.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetCKaonSq.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
     else:
      continue
    else:
     continue
   if p1.DeltaR(Jetqlv) > p1.DeltaR(Jetqbarlv):
    if p1.DeltaR(Jetqbarlv) <= 0.5:
     if abs(particle2.PID) == 321:
      if q.PID == 1 or q.PID == 2:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetCKaonLqbar.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetCKaonSqbar.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     else:
      continue
    else:
     continue
   else:
    continue
  else:
   continue

 # Convert histograms to numpy arrays
 if q.PID == 1 or q.PID == 2:
  ArrayCKaonLqbar = root_numpy.hist2array(histJetCKaonLq)
  ArrayCKaonLq = root_numpy.hist2array(histJetCKaonLqbar)
  ArrayCKaonL += [ArrayCKaonLq] + [ArrayCKaonLqbar]
  histJetCKaonLq.Write()
  histJetCKaonLqbar.Write()
 if q.PID == 3:
  ArrayCKaonSqbar = root_numpy.hist2array(histJetCKaonSq)
  ArrayCKaonSq = root_numpy.hist2array(histJetCKaonSqbar)
  ArrayCKaonS += [ArrayCKaonSq] + [ArrayCKaonSqbar]
  histJetCKaonSq.Write()
  histJetCKaonSqbar.Write()

 # Delete histograms (Runtime)
 histJetCKaonLq.Delete()
 histJetCKaonLqbar.Delete()
 histJetCKaonSq.Delete()
 histJetCKaonSqbar.Delete()

# Convert list to numpy array
ArrayCKaonL = np.array(ArrayCKaonL)
ArrayCKaonS = np.array(ArrayCKaonS)

# Save numpy arrays as PIL iamges
for el in range(ArrayCKaonL.shape[0]):
 pil_image = Image.fromarray((ArrayCKaonL[el]*255).astype(np.uint8))
 pil_image =  pil_image.convert('RGB')
 pil_image.save('./Images/L/'+str(el)+'.png','PNG')
for el in range(ArrayCKaonS.shape[0]):
 pil_image = Image.fromarray((ArrayCKaonS[el]*255).astype(np.uint8))
 pil_image =  pil_image.convert('RGB')
 pil_image.save('./Images/S/'+str(el)+'.png','PNG')

# Sum of all PIL Images
ArrayCKaonLSum = np.sum(ArrayCKaonL,axis = 0)
pil_image2 = Image.fromarray((ArrayCKaonLSum*255).astype(np.uint8))
pil_image2 = pil_image2.convert('RGB')
pil_image2.save('./Images/L/'+'histJetCKaonL'+'.png','PNG')
ArrayCKaonSSum = np.sum(ArrayCKaonS,axis = 0)
pil_image2 = Image.fromarray((ArrayCKaonSSum*255).astype(np.uint8))
pil_image2 = pil_image2.convert('RGB')
pil_image2.save('./Images/S/'+'histJetCKaonS'+'.png','PNG')


file.Close()
