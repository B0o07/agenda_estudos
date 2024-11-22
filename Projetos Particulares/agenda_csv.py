import csv
from datetime import datetime, timedelta

# Função para gerar o cronograma de eventos
def gerar_cronograma(inicio, fim_faculdade, aulas_cs50, estudo_pmesp, data_prova_pmesp, fim_cs50):
    cronograma = []
    
    # Função para adicionar eventos no cronograma
    def adicionar_evento(nome, data_inicio, hora_inicio, data_fim, hora_fim, descricao):
        cronograma.append([nome, data_inicio.strftime('%m/%d/%Y'), hora_inicio, data_fim.strftime('%m/%d/%Y'), hora_fim, descricao, "", "False", "True"])

    # Dados gerais
    data_inicio = datetime.strptime(inicio, '%d/%m/%Y')
    data_fim_faculdade = datetime.strptime(fim_faculdade, '%d/%m/%Y')
    data_fim_cs50 = datetime.strptime(fim_cs50, '%d/%m/%Y')
    data_prova = datetime.strptime(data_prova_pmesp, '%d/%m/%Y')

    # Definir as datas de férias
    inicio_férias_1 = datetime.strptime('15/12/2024', '%d/%m/%Y')
    fim_férias_1 = datetime.strptime('31/01/2025', '%d/%m/%Y')
    inicio_férias_2 = datetime.strptime('01/07/2025', '%d/%m/%Y')
    fim_férias_2 = datetime.strptime('15/08/2025', '%d/%m/%Y')

    # Gerando eventos diários
    dia_atual = data_inicio
    while dia_atual <= data_fim_faculdade:
        # Pular as férias para a faculdade, mas não os estudos de CS50 e PMESP
        if (inicio_férias_1 <= dia_atual <= fim_férias_1) or (inicio_férias_2 <= dia_atual <= fim_férias_2):
            # Não adicionar eventos para a faculdade durante as férias, mas manter os de CS50 e PMESP
            if not (dia_atual.weekday() == 0 or dia_atual.weekday() == 1 or dia_atual.weekday() == 2 or dia_atual.weekday() == 3 or dia_atual.weekday() == 4 or dia_atual.weekday() == 5):
                dia_atual += timedelta(days=1)
                continue

        # Segunda-feira
        if dia_atual.weekday() == 0:  # Segunda-feira
            if not (inicio_férias_1 <= dia_atual <= fim_férias_1 or inicio_férias_2 <= dia_atual <= fim_férias_2):
                adicionar_evento("Faculdade (ADS) - Estudo", dia_atual, "17:00", dia_atual, "18:00", "Estudo de conteúdo para faculdade (Foco em Análise e Desenvolvimento de Sistemas).")
            if dia_atual <= data_prova:
                adicionar_evento("Estudo PMESP", dia_atual, "18:00", dia_atual, "19:00", "Estudo de PMESP (Legislação e Conhecimentos Gerais).")
        # Terça-feira
        elif dia_atual.weekday() == 1:
            if not (inicio_férias_1 <= dia_atual <= fim_férias_1 or inicio_férias_2 <= dia_atual <= fim_férias_2):
                adicionar_evento("Faculdade (ADS) - Estudo", dia_atual, "17:00", dia_atual, "18:00", "Estudo de conteúdo para faculdade (Foco em Análise e Desenvolvimento de Sistemas).")
            if dia_atual <= data_prova:
                adicionar_evento("Estudo PMESP", dia_atual, "18:00", dia_atual, "19:00", "Estudo de PMESP (Matemática e Raciocínio Lógico).")
            if dia_atual <= data_fim_cs50:
                adicionar_evento("CS50 - Lógica de Programação", dia_atual, "19:00", dia_atual, "20:00", "Estudo de CS50 (Lógica de Programação e Algoritmos).")
        # Quarta-feira
        elif dia_atual.weekday() == 2:
            if not (inicio_férias_1 <= dia_atual <= fim_férias_1 or inicio_férias_2 <= dia_atual <= fim_férias_2):
                adicionar_evento("Faculdade (ADS) - Estudo", dia_atual, "17:00", dia_atual, "18:00", "Estudo de conteúdo para faculdade (Foco em Análise e Desenvolvimento de Sistemas).")
            if dia_atual <= data_prova:
                adicionar_evento("Estudo PMESP", dia_atual, "18:00", dia_atual, "19:00", "Estudo de PMESP (Direitos Humanos, Noções de Direito).")
            adicionar_evento("Aula de Guitarra", dia_atual, "19:00", dia_atual, "20:00", "Aula de Guitarra.")
        # Quinta-feira
        elif dia_atual.weekday() == 3:
            if dia_atual <= data_prova:
                adicionar_evento("Estudo PMESP", dia_atual, "17:00", dia_atual, "18:00", "Estudo de PMESP (Informática e Conhecimentos Específicos).")
            if not (inicio_férias_1 <= dia_atual <= fim_férias_1 or inicio_férias_2 <= dia_atual <= fim_férias_2):
                adicionar_evento("Faculdade (ADS) - Estudo", dia_atual, "18:00", dia_atual, "19:00", "Estudo de conteúdo para faculdade (Foco em Análise e Desenvolvimento de Sistemas).")
        # Sexta-feira
        elif dia_atual.weekday() == 4:
            if dia_atual <= data_prova:
                adicionar_evento("Estudo PMESP", dia_atual, "17:00", dia_atual, "18:00", "Estudo de PMESP (Simulados e Revisão).")
            if not (inicio_férias_1 <= dia_atual <= fim_férias_1 or inicio_férias_2 <= dia_atual <= fim_férias_2):
                adicionar_evento("Faculdade (ADS) - Estudo", dia_atual, "18:00", dia_atual, "19:00", "Estudo de conteúdo para faculdade (Foco em Análise e Desenvolvimento de Sistemas).")
        # Sábado
        elif dia_atual.weekday() == 5:
            if dia_atual <= data_prova:
                adicionar_evento("Revisão PMESP", dia_atual, "17:00", dia_atual, "19:00", "Revisão para PMESP.")
            if not (inicio_férias_1 <= dia_atual <= fim_férias_1 or inicio_férias_2 <= dia_atual <= fim_férias_2):
                adicionar_evento("Faculdade (ADS) - Estudo", dia_atual, "19:00", dia_atual, "20:00", "Estudo de conteúdo para faculdade (Foco em Análise e Desenvolvimento de Sistemas).")
        
        dia_atual += timedelta(days=1)

    return cronograma

# Definir datas e parâmetros
inicio_faculdade = '22/11/2024'
fim_faculdade = '30/06/2027'  # Fim da faculdade em junho de 2027
aulas_cs50 = 8  # Faltam 8 aulas de CS50 até 31/12
data_prova_pmesp = '16/02/2025'  # Próxima prova PMESP
fim_cs50 = '31/12/2024'  # Fim do estudo de CS50

# Gerar cronograma
cronograma = gerar_cronograma(inicio_faculdade, fim_faculdade, aulas_cs50, 'Estudo PMESP', data_prova_pmesp, fim_cs50)

# Salvar o cronograma em um arquivo CSV
nome_arquivo = 'cronograma.csv'
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["Subject", "Start Date", "Start Time", "End Date", "End Time", "Description", "Location", "All Day Event", "Private"])
    for evento in cronograma:
        escritor.writerow(evento)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
