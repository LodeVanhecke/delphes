import sys
import ROOT
import math
import numpy as np
import root_numpy
import PIL.Image as Image

def Cosmetic(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  for i in range(len(hist)):
    hist[i].GetXaxis().SetTitle(xtitle)
    hist[i].GetYaxis().SetTitle(ytitle)
    hist[i].GetXaxis().SetRangeUser(-0.5,0.5)
    hist[i].GetYaxis().SetRangeUser(-0.5,0.5)
    hist[i].SetFillColor(2)
    hist[i].SetLineWidth(1)
    hist[i].SetTitle("")
    if error == True:
     if norm == True:
      hist[i].DrawNormalized('e same box')
     else:
      hist[i].Draw('e same box')
    else:
     if norm == True:
      hist[i].DrawNormalized('same box')
     else:
      hist[i].Draw('same box')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend()
  c.SaveAs(filename)

def Cosmetic3(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  hist.GetXaxis().SetTitle(xtitle)
  hist.GetYaxis().SetTitle(ytitle)
  hist.GetXaxis().SetRangeUser(-0.5,0.5)
  hist.GetYaxis().SetRangeUser(-0.5,0.5)
  hist.SetFillColor(2)
  hist.SetLineWidth(1)
  hist.SetTitle("")
  if error == True:
   if norm == True:
    hist.DrawNormalized('e same box')
   else:
    hist.Draw('e same box')
  else:
   if norm == True:
    hist.DrawNormalized('same box')
   else:
    hist.Draw('same box')
  if logx == True:
   c.SetLogx()
  if logy == True:
   c.SetLogy()
  c.BuildLegend()
  c.SaveAs(filename)

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


NL = 0
NS = 0
NC = 0
NB = 0

Array = []

histJetCKaon = []

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

 # Code for histograms
 if q.PID == 1 or q.PID == 2:
  NL += 1
 if q.PID == 3:
  NS += 1
 if q.PID == 4:
  NC += 1
 if q.PID == 5:
  NB += 1

 # Book histograms
 histJetCKaonq = ROOT.TH2F("histJetCKaonq","", 50, -0.5, 0.5, 50, -0.5, 0.5)
 histJetCKaonqbar = ROOT.TH2F("histJetCKaonqbar","", 50, -0.5, 0.5, 50, -0.5, 0.5)

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
       histJetCKaonq.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetq.PT
       DeltaTheta = Jetqlv.Theta()-p1.Theta()
       histJetCKaonq.Fill(p1.DeltaPhi(Jetqlv),DeltaTheta,PT)
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
       histJetCKaonqbar.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
      if q.PID == 3:
       PT = abs(particle2.PT)/Jetqbar.PT
       DeltaTheta = Jetqbarlv.Theta()-p1.Theta()
       histJetCKaonqbar.Fill(p1.DeltaPhi(Jetqbarlv),DeltaTheta,PT)
     else:
      continue
    else:
     continue
   else:
    continue
  else:
   continue

 #Convert histogram to numpy array
 ArrayCKaonqbar = root_numpy.hist2array(histJetCKaonq)
 ArrayCKaonq = root_numpy.hist2array(histJetCKaonqbar)
 ArrayCKaon += [ArrayqCKaonq] + [ArrayCKaonqbar]

 histJetCKaon += [histJetCKaonq] + [histJetCKaonqbar]

# histJetCKaon.Write()

 histJetCKaonq.Write()
 histJetCKaonqbar.Write()

 try:
  Cosmetic3(histJetCKaonq,'','',False,False,False,False,'./Images/'+'histJetCKaonq'+str(len(Array)-2)+'.png')
 except:
  pass
 try:
  Cosmetic3(histJetCKaonqbar,'','',False,False,False,False,'./Images/'+'histJetCKaonqbar'+str(len(Array)-1)+'.png')
 except:
  pass

 histJetCKaonq.Delete()
 histJetCKaonqbar.Delete()

try:
 Cosmetic(histJetCKaon,'','',False,False,False,False,'./Images/'+'histJetCKaon')
except:
 pass

Array = np.array(Array)

#for i in Array[5]:
# for j in i:
#  print(j,end='\t')
# print()

print(Array.shape)

for el in range(Array.shape[0]):
 pil_image = Image.fromarray((Array[el]*255).astype(np.uint8))
 pil_image =  pil_image.convert('RGB')
 pil_image.save('./Images/'+str(el)+'.png','PNG')

ArraySum = np.sum(Array,axis = 0)
pil_image2 = Image.fromarray((ArraySum*255).astype(np.uint8))
pil_image2 = pil_image2.convert('RGB')
pil_image2.save('./Images/'+'histJetCKaon'+'.png','PNG')

file.Close()
