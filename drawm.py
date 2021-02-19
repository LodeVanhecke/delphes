import sys
import ROOT

def Cosmetic(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  hist[0].GetXaxis().SetTitle(xtitle)
  hist[0].GetYaxis().SetTitle(ytitle)
  for i in range(len(hist)):
    hist[i].SetLineColor(i+1)
    hist[i].SetLineWidth(1)
    hist[i].SetTitle("")
    if error == True:
     if norm == True:
      hist[i].DrawNormalized('same e')
     else:
      hist[i].Draw('same e')
    else:
     if norm == True:
      hist[i].DrawNormalized('same')
     else:
      hist[i].Draw('same')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend()
  c.SaveAs(filename)

file = ROOT.TFile(sys.argv[1],"READ")




histMJet = [file.Get('histMJetL')]+[file.Get('histMJetS')]+[file.Get('histMJetC')]+[file.Get('histMJetB')]
Cosmetic(histMJet,'Total invariant mass of jets in a event','',False,False,False,False,'histMJet_'+sys.argv[1][:-5]+'.png')

histM2Jet = [file.Get('histM2JetL')]+[file.Get('histM2JetS')]+[file.Get('histM2JetC')]+[file.Get('histM2JetB')]
Cosmetic(histM2Jet,'Max invariant mass of two jets in a event','',False,False,False,False,'histM2Jet_'+sys.argv[1][:-5]+'.png')
