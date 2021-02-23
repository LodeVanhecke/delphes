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

def Cosmetic2(hist,xtitle,ytitle,error,norm,logx,logy,filename):
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
      hist[i].DrawNormalized('same e box1')
     else:
      hist[i].Draw('same e box1')
    else:
     if norm == True:
      hist[i].DrawNormalized('same box1')
     else:
      hist[i].Draw('same box1')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend()
  c.SaveAs(filename)



file = ROOT.TFile(sys.argv[1],"READ")


histNJet = [file.Get('histNJetL')]+[file.Get('histNJetS')]+[file.Get('histNJetC')]+[file.Get('histNJetB')]
Cosmetic(histNJet,'Number of jets in event','',False,True,False,False,'histNJet_'+sys.argv[1][:-5]+'.png')



histCKaon = [file.Get('histCKaonL')]+[file.Get('histCKaonS')]+[file.Get('histCKaonC')]+[file.Get('histCKaonB')]
Cosmetic2(histNCKaon,'Angle/pseudoRap of charged kaons in jet','',False,True,False,True,'histCKaon_'+sys.argv[1][:-5]+'.png')
