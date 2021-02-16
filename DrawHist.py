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

histNJet = [file.Get('histNJet')]
Cosmetic(histNJet,'Number of jets in event','',False,True,False,False,'histNJet_'+sys.argv[1][:-5]+'.png')

histMJet = [file.Get('histMJet')]
Cosmetic(histMJet,'Total invariant mass of jets in a event','',False,True,False,False,'histMJet_'+sys.argv[1][:-5]+'.png')

histM2Jet = [file.Get('histM2Jet')]
Cosmetic(histM2Jet,'Max invariant mass of two jets in a event','',False,True,False,False,'histM2Jet_'+sys.argv[1][:-5]+'.png')


histJetPT = [file.Get('histJetPTL')]+[file.Get('histJetPTS')]+[file.Get('histJetPTC')]+[file.Get('histJetPTB')]
Cosmetic(histJetPT,'Transverse momentum','',False,True,False,False,'histJetPT_'+sys.argv[1][:-5]+'.png')


histNCKaon = [file.Get('histNCKaonL')]+[file.Get('histNCKaonS')]+[file.Get('histNCKaonC')]+[file.Get('histNCKaonB')]
Cosmetic(histNCKaon,'Number charged kaons in jet','',False,True,False,True,'histNCKaon_'+sys.argv[1][:-5]+'.png')

histCKaonPT = [file.Get('histCKaonPTL')]+[file.Get('histCKaonPTS')]+[file.Get('histCKaonPTC')]+[file.Get('histCKaonPTB')]
Cosmetic(histCKaonPT,'Transverse momentum of charged kaons','',False,True,False,True,'histCKaonPT_'+sys.argv[1][:-5]+'.png')


histNNKaon = [file.Get('histNNKaonL')]+[file.Get('histNNKaonS')]+[file.Get('histNNKaonC')]+[file.Get('histNNKaonB')]
Cosmetic(histNNKaon,'Number neutral kaons in jet','',False,True,False,True,'histNNKaon_'+sys.argv[1][:-5]+'.png')

histNKaonPT = [file.Get('histNKaonPTL')]+[file.Get('histNKaonPTS')]+[file.Get('histNKaonPTC')]+[file.Get('histNKaonPTB')]
Cosmetic(histNKaonPT,'Transverse momentum of neutral kaons','',False,True,False,True,'histNKaonPT_'+sys.argv[1][:-5]+'.png')


histNCPion = [file.Get('histNCPionL')]+[file.Get('histNCPionS')]+[file.Get('histNCPionC')]+[file.Get('histNCPionB')]
Cosmetic(histNCPion,'Number charged pions in jet','',False,True,False,True,'histNCPion_'+sys.argv[1][:-5]+'.png')

histCPionPT = [file.Get('histCPionPTL')]+[file.Get('histCPionPTS')]+[file.Get('histCPionPTC')]+[file.Get('histCPionPTB')]
Cosmetic(histCPionPT,'Transverse momentum of charged pions','',False,True,False,True,'histCPionPT_'+sys.argv[1][:-5]+'.png')


histNNPion = [file.Get('histNNPionL')]+[file.Get('histNNPionS')]+[file.Get('histNNPionC')]+[file.Get('histNNPionB')]
Cosmetic(histNNPion,'Number neutral pions in jet','',False,True,False,True,'histNNPion_'+sys.argv[1][:-5]+'.png')

histNPionPT = [file.Get('histNPionPTL')]+[file.Get('histNPionPTS')]+[file.Get('histNPionPTC')]+[file.Get('histNPionPTB')]
Cosmetic(histNPionPT,'Transverse momentum of neutral pions','',False,True,False,True,'histNPionPT_'+sys.argv[1][:-5]+'.png')


histJetC = [file.Get('histJetCL')]+[file.Get('histJetCS')]+[file.Get('histJetCC')]+[file.Get('histJetCB')]
Cosmetic(histJetC,'Charge of jet','',False,True,False,False,'histJetC_'+sys.argv[1][:-5]+'.png')
