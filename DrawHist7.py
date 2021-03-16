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
  c.BuildLegend(1,1,1,1)
  c.SaveAs(filename)

def Cosmetic2(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  c.Divide(2,2,0.01,0.01)
  ROOT.gStyle.SetOptStat(0)
  for i in range(len(hist)):
    hist[i].GetXaxis().SetTitle(xtitle)
    hist[i].GetYaxis().SetTitle(ytitle)
    hist[i].SetFillColor(i+1)
    hist[i].SetLineWidth(1)
   # hist[i].SetTitle("")
    if error == True:
     if norm == True:
      c.cd(i+1)
      hist[i].DrawNormalized('e colz')
     else:
      c.cd(i+1)
      hist[i].Draw('e colz')
    else:
     if norm == True:
      c.cd(i+1)
      hist[i].DrawNormalized('colz')
     else:
      c.cd(i+1)
      hist[i].Draw('colz')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
 # c.BuildLegend()
  c.SaveAs(filename)


def Cosmetic3(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  ROOT.gStyle.SetOptStat(0)
  for i in range(len(hist)):
    hist[i].GetXaxis().SetTitle(xtitle)
    hist[i].GetYaxis().SetTitle(ytitle)
    hist[i].GetXaxis().SetRangeUser(-0.4,0.4)
    hist[i].GetYaxis().SetRangeUser(-0.4,0.4)
    hist[i].SetFillColorAlpha(i+1,0.70)
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



file = ROOT.TFile(sys.argv[1],"READ")


histJetL = [file.Get('histJetCKaonL')]+[file.Get('histJetNKaonL')]+[file.Get('histJetCPionL')]+[file.Get('histJetNPionL')]+[file.Get('histJetElecL')]+[file.Get('histJetMuonL')]+[file.Get('histJetProtL')]+[file.Get('histJetNeutL')]+[file.Get('histJetPhotL')]
Cosmetic3(histJetL,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,True,'histJetL_'+sys.argv[1][:-5]+'.png')

histJetS = [file.Get('histJetCKaonS')]+[file.Get('histJetNKaonS')]+[file.Get('histJetCPionS')]+[file.Get('histJetNPionS')]+[file.Get('histJetElecS')]+[file.Get('histJetMuonS')]+[file.Get('histJetProtS')]+[file.Get('histJetNeutS')]+[file.Get('histJetPhotS')]
Cosmetic3(histJetS,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,True,'histJetS_'+sys.argv[1][:-5]+'.png')

histJetC = [file.Get('histJetCKaonC')]+[file.Get('histJetNKaonC')]+[file.Get('histJetCPionC')]+[file.Get('histJetNPionC')]+[file.Get('histJetElecC')]+[file.Get('histJetMuonC')]+[file.Get('histJetProtC')]+[file.Get('histJetNeutC')]+[file.Get('histJetPhotC')]
Cosmetic3(histJetC,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,True,'histJetC_'+sys.argv[1][:-5]+'.png')

histJetB = [file.Get('histJetCKaonB')]+[file.Get('histJetNKaonB')]+[file.Get('histJetCPionB')]+[file.Get('histJetNPionB')]+[file.Get('histJetElecB')]+[file.Get('histJetMuonB')]+[file.Get('histJetProtB')]+[file.Get('histJetNeutB')]+[file.Get('histJetPhotB')]
Cosmetic3(histJetB,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,True,'histJetB_'+sys.argv[1][:-5]+'.png')
