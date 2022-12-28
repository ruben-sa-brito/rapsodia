from datetime import datetime, timedelta
from reportlab.pdfgen import canvas

class generate():
    def __init__(self, nome) -> None:
        self.cnv = canvas.Canvas("pdfs/"+nome + '.pdf')
    def generate_parcs(self, ida, nome, datavenc, n_mes, valor):
        cont = 0
        vencs = list()
        lines_c = [0, -208, -416, -632]
        day = int(datavenc[0:2])
        datavenc = datetime(year = int(datavenc[6:10]), month= int(datavenc[3:5]), day = int(datavenc[0:2]))
        
        
        while cont <= n_mes:
            
            if datavenc.day == day:
                if datavenc.month < 10:
                    vencs.append(str(datavenc.day)+'/'+'0'+str(datavenc.month)+'/'+str(datavenc.year))
                else:
                    vencs.append(str(datavenc.day)+'/'+str(datavenc.month)+'/'+str(datavenc.year))    
                cont+=1
            datavenc += timedelta(days=1)
            
                
        
        cont = 0
        cont2 = 0 
        while cont2+1 <= n_mes:
            if cont == 0:
                self.cnv.setFont(psfontname= 'Times-Roman' ,size=10)
                self.cnv.line(0,208, 50, 208)
                self.cnv.line(550,208, 600, 208)
                self.cnv.line(0,416, 50, 416)
                self.cnv.line(550,416, 600, 416)
                self.cnv.line(0,632,50, 632)
                self.cnv.line(550,632,600, 632)
            
            if cont2 < 10:
                mes = '0'+str(cont2+1)   
                self.first_line(ida, nome, vencs[cont2],mes, valor, lines_c[cont])
            else:
                self.first_line(ida, nome, vencs[cont2],cont2+1, valor, lines_c[cont])    
            
            cont +=1
            if cont == 4:
                cont = 0
                self.cnv.showPage()
            cont2 += 1    
        self.cnv.save()    
            

    def first_line(self, ida, nome, datavenc, n_mens, valor,y):
        cont = 0
        x = 0
        while cont <=1:
            if cont ==1:
                x = 300
            self.cnv.drawString(152+x, 800+y, 'INFORMÁTICA' )
            self.cnv.drawString(150+x, 790+y, 'TURMA-CRATO' )
            self.cnv.drawString(20+x, 820+y, f'id: {ida}' )
            self.cnv.drawImage('icons\img.jpg',40+x, 780+y, 60, 30)  # imagem da empresa
            self.cnv.rect(35+x, 740+y, 240, 25) # aluno
            self.cnv.setFont(psfontname= 'Times-Roman' ,size=8)
            self.cnv.drawString(37+x, 758+y, 'Aluno ' )
            
            self.cnv.rect(35+x, 710+y, 240, 25) # mensalidade/ vencimento/ valor
            self.cnv.drawString(37+x, 728+y, 'Nº Mensalidade' )
            self.cnv.line(115+x,710+y, 115+x,735+y )
            self.cnv.drawString(117+x, 728+y, 'Vencimento' )
            self.cnv.line(195+x,710+y, 195+x,735+y )
            self.cnv.drawString(197+x, 728+y, 'Valor' )
            self.cnv.setFont(psfontname= 'Times-Roman' ,size=9)
            self.cnv.drawString(35+x, 669+y, 'Data___/___/_____' )
            self.cnv.drawString(170+x, 669+y, '___________________' )
            self.cnv.drawString(170+x, 658+y, '          Assinatura' )
            self.cnv.setFont(psfontname= 'Times-Roman' ,size=10)
            self.cnv.drawString(37+x, 746+y, nome)
            self.cnv.drawString(37+x, 714+y, str(n_mens) )
            self.cnv.drawString(117+x, 714+y, datavenc )
            self.cnv.drawString(197+x, 714+y, f'R$ {valor}0' )
            if cont == 0:
                self.cnv.line(300,664+y, 300,795+y ) #linha divisória
            cont+=1
