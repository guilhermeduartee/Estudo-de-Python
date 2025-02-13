'''
Criar um programa que dependendo da temperatura (em celsius) do steak
ele retornara o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 46°C - Rare (selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium  (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

ponto_carne = int(input('Digite a temperatura da carne que você esta fazedo:'))

if ponto_carne < 48:
    print('Deixe mais alguns minutos na churrasqueira!')
elif ponto_carne in range(48, 53):
    print('Sua carne está elada!')
elif ponto_carne in range(54, 59):
    print('Sua carne está ao ponto para o mal!')
elif ponto_carne in range(60, 64):
    print('Sua carne está ao ponto!')    
elif ponto_carne in range(65, 70):
    print('Sua carne está ao ponto para o bem!')
elif ponto_carne >= 71:
    print('Sua carne virou carvão!')
                
    