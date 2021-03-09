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
      hist[i].DrawNormalized('same e hist')
     else:
      hist[i].Draw('same e hist')
    else:
     if norm == True:
      hist[i].DrawNormalized('same hist')
     else:
      hist[i].Draw('same hist')
    if logx == True:
     c.SetLogx()
    if logy == True:
     c.SetLogy()
  c.BuildLegend(1,1,1,1)
  c.SaveAs(filename)

def Cosmetic2(hist,xtitle,ytitle,error,norm,logx,logy,filename):
  c = ROOT.TCanvas()
  c.Divide(2,1,0.01,0.01)
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
    hist[i].SetFillColorAlpha(i+1,0.80)
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


histJetCKaon = [file.Get('histJetCKaonL')]+[file.Get('histJetCKaonS')]
Cosmetic3(histJetCKaon,'DeltaPhi of charged kaons in jet','DeltaTheta of charged kaons in jet',False,False,False,False,'histJetCKaon_'+sys.argv[1][:-5]+'.pdf')

histJetNKaon = [file.Get('histJetNKaonL')]+[file.Get('histJetNKaonS')]
Cosmetic3(histJetNKaon,'DeltaPhi of neutral kaons in jet','DeltaTheta of neutral kaons in jet',False,False,False,False,'histJetNKaon_'+sys.argv[1][:-5]+'.pdf')

histJetCPion = [file.Get('histJetCPionL')]+[file.Get('histJetCPionS')]
Cosmetic3(histJetCPion,'DeltaPhi of charged pions in jet','DeltaTheta of charged pions in jet',False,False,False,False,'histJetCPion_'+sys.argv[1][:-5]+'.pdf')

histJetNPion = [file.Get('histJetNPionL')]+[file.Get('histJetNPionS')]
Cosmetic3(histJetNPion,'DeltaPhi of neutral pions in jet','DeltaTheta of neutral pions in jet',False,False,False,False,'histJetNPion_'+sys.argv[1][:-5]+'.pdf')

histJetElec = [file.Get('histJetElecL')]+[file.Get('histJetElecS')]
Cosmetic3(histJetElec,'DeltaPhi of electrons\positrons in jet','DeltaTheta of electrons\positrons in jet',False,False,False,False,'histJetElec_'+sys.argv[1][:-5]+'.pdf')

histJetMuon = [file.Get('histJetMuonL')]+[file.Get('histJetMuonS')]
Cosmetic3(histJetMuon,'DeltaPhi of muons in jet','DeltaTheta of muons in jet',False,False,False,False,'histJetMuon_'+sys.argv[1][:-5]+'.pdf')

histJetProt = [file.Get('histJetProtL')]+[file.Get('histJetProtS')]
Cosmetic3(histJetProt,'DeltaPhi of protons in jet','DeltaTheta of protons in jet',False,False,False,False,'histJetProt_'+sys.argv[1][:-5]+'.pdf')

histJetNeut = [file.Get('histJetNeutL')]+[file.Get('histJetNeutS')]
Cosmetic3(histJetNeut,'DeltaPhi of neutrons in jet','DeltaTheta of neutrons in jet',False,False,False,False,'histJetNeut_'+sys.argv[1][:-5]+'.pdf')

histJetPhot = [file.Get('histJetPhotL')]+[file.Get('histJetPhotS')]
Cosmetic3(histJetPhot,'DeltaPhi of photons in jet','DeltaTheta of photons in jet',False,False,False,False,'histJetPhot_'+sys.argv[1][:-5]+'.pdf')


histJetL = [file.Get('histJetCKaonL')]+[file.Get('histJetNKaonL')]+[file.Get('histJetCPionL')]+[file.Get('histJetNPionL')]+[file.Get('histJetElecL')]+[file.Get('histJetMuonL')]+[file.Get('histJetProtL')]+[file.Get('histJetNeutL')]+[file.Get('histJetPhotL')]
Cosmetic3(histJetL,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetL_'+sys.argv[1][:-5]+'.pdf')

histJetS = [file.Get('histJetCKaonS')]+[file.Get('histJetNKaonS')]+[file.Get('histJetCPionS')]+[file.Get('histJetNPionS')]+[file.Get('histJetElecS')]+[file.Get('histJetMuonS')]+[file.Get('histJetProtS')]+[file.Get('histJetNeutS')]+[file.Get('histJetPhotS')]
Cosmetic3(histJetS,'DeltaPhi of particles in jet','DeltaTheta of particles in jet',False,False,False,False,'histJetS_'+sys.argv[1][:-5]+'.pdf')

