import sys
import ROOT

def Cosmetic(hist,xtitle,ytitle,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  hist[0].GetXaxis().SetTitle(xtitle)
  hist[0].GetYaxis().SetTitle(ytitle)
  for i in range(len(hist)):
    hist[i].SetLineColor(i+1)
    hist[i].SetLineWidth(3)
    hist[i].SetTitle("")
    if norm == True:
     hist[i].DrawNormalized('same')
    else:
     hist[i].Draw('same')
  c.BuildLegend()
  c.SaveAs(filename)

file = ROOT.TFile(sys.argv[1],"READ")
histJet = [file.Get('histGenJetD')]+[file.Get('histGenJetU')]+[file.Get('histGenJetS')]+[file.Get('histGenJetC')]+[file.Get('histGenJetB')]
Cosmetic(histJet,'Transverse momentum','',True,False,False,'histJet_'+sys.argv[1][:-5]+'.png')

histNCKaon = [file.Get('histNCKaonD')]+[file.Get('histNCKaonU')]+[file.Get('histNCKaonS')]+[file.Get('histNCKaonC')]+[file.Get('histNCKaonB')]
Cosmetic(histNCKaon,'Number charged kaons in jet','',True,False,False,'histNCKaon_'+sys.argv[1][:-5]+'.png')
