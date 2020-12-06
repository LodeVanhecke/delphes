
import sys
import ROOT

def Cosmetic(hist,xtitle,ytitle,norm,logx,logy,filename):
  c=ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  hist[0].GetXaxis().SetTitle(xtitle)
  hist[0].GetYaxis().SetTitle(ytitle)
  for i in range(len(hist)):
    hist[i].SetLineColor(i+1)
    hist[i].SetLineWidth(3)
    hist[i].SetTitle("")
    if norm==True:
     hist[i].DrawNormalized('same')
    else:
     hist[i].Draw('same')
  c.BuildLegend()
  c.SaveAs(filename)

file = ROOT.TFile(sys.argv[1],"READ")
histJet = [file.Get('histGenJetD')]+[file.Get('histGenJetU')]+[file.Get('histGenJetS')]+[file.Get('histGenJetC')]+[file.Get('histGenJetB')]
Cosmetic(histJet,'PT','number of jets',True,False,False,'histJet.png') 

histParticle = [file.Get('histParticleD')]+[file.Get('histParticleU')]+[file.Get('histParticleS')]+[file.Get('histParticleC')]+[file.Get('histParticleB')]
Cosmetic(histParticle,'Number of kaons per event','',True,False,False,'histParticle.png')
