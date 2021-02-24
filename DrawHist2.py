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
    hist[i].SetFillColor(i+1)
    hist[i].SetLineWidth(1)
    hist[i].SetTitle("")
    if error == True:
     if norm == True:
      hist[i].DrawNormalized('same e box')
     else:
      hist[i].Draw('same e box')
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


histNJet = [file.Get('histNJetL')]+[file.Get('histNJetS')]+[file.Get('histNJetC')]+[file.Get('histNJetB')]
Cosmetic(histNJet,'Number of jets in event','',False,False,False,False,'histNJet_'+sys.argv[1][:-5]+'.png')



histCKaon = [file.Get('histCKaonL')]+[file.Get('histCKaonS')]+[file.Get('histCKaonC')]+[file.Get('histCKaonB')]
Cosmetic2(histCKaon,'DeltaPhi of charged kaons in jet','DeltaEta of charged kaons in jet',False,True,False,False,'histCKaon_'+sys.argv[1][:-5]+'.png')

histNKaon = [file.Get('histNKaonL')]+[file.Get('histNKaonS')]+[file.Get('histNKaonC')]+[file.Get('histNKaonB')]
Cosmetic2(histNKaon,'DeltaPhi of neutral kaons in jet','DeltaEta of neutral kaons in jet',False,True,False,False,'histNKaon_'+sys.argv[1][:-5]+'.png')


histCPion = [file.Get('histCPionL')]+[file.Get('histCPionS')]+[file.Get('histCPionC')]+[file.Get('histCPionB')]
Cosmetic2(histCPion,'DeltaPhi of charged pions in jet','DeltaEta of charged pions in jet',False,True,False,False,'histCPion_'+sys.argv[1][:-5]+'.png')

histNPion = [file.Get('histNPionL')]+[file.Get('histNPionS')]+[file.Get('histNPionC')]+[file.Get('histNPionB')]
Cosmetic2(histNPion,'DeltaPhi of neutral pions in jet','DeltaEta of neutral pions in jet',False,True,False,False,'histNPion_'+sys.argv[1][:-5]+'.png')


histElec = [file.Get('histElecL')]+[file.Get('histElecS')]+[file.Get('histElecC')]+[file.Get('histElecB')]
Cosmetic2(histElec,'DeltaPhi of electrons/positrons in jet','DeltaEta of electrons/positrons in jet',False,True,False,False,'histElec_'+sys.argv[1][:-5]+'.png')


histMuon = [file.Get('histMuonL')]+[file.Get('histMuonS')]+[file.Get('histMuonC')]+[file.Get('histMuonB')]
Cosmetic2(histMuon,'DeltaPhi of muons (pos and neg) in jet','DeltaEta of muons (pos and neg) in jet',False,True,False,False,'histMuon_'+sys.argv[1][:-5]+'.png')


histProt = [file.Get('histProtL')]+[file.Get('histProtS')]+[file.Get('histProtC')]+[file.Get('histProtB')]
Cosmetic2(histProt,'DeltaPhi of protons in jet','DeltaEta of protons in jet',False,True,False,False,'histProt_'+sys.argv[1][:-5]+'.png')


histNeut = [file.Get('histNeutL')]+[file.Get('histNeutS')]+[file.Get('histNeutC')]+[file.Get('histNeutB')]
Cosmetic2(histNeut,'DeltaPhi of neutrons in jet','DeltaEta of neutrons in jet',False,True,False,False,'histNeut_'+sys.argv[1][:-5]+'.png')
